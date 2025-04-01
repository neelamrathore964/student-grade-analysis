from flask import Flask, render_template, request, redirect, url_for
from database.db_connection import get_db_connection
import uuid

app = Flask(__name__)

# def generate_student_id():
#     return str(uuid.uuid4())[:10]  

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Get total number of students
    cursor.execute('SELECT COUNT(*) FROM students')
    total_students = cursor.fetchone()['COUNT(*)']

    # Get count of students with distinction (average grade >= 70)
    cursor.execute('''
        SELECT COUNT(*) FROM students 
        WHERE student_id IN (SELECT student_id FROM grades GROUP BY student_id HAVING AVG(module_grade) >= 70)
    ''')
    distinction_count = cursor.fetchone()['COUNT(*)']

    # Get count of students with merit (average grade >= 60 and < 70)
    cursor.execute('''
        SELECT COUNT(*) FROM students 
        WHERE student_id IN (SELECT student_id FROM grades GROUP BY student_id HAVING AVG(module_grade) >= 60 AND AVG(module_grade) < 70)
    ''')
    merit_count = cursor.fetchone()['COUNT(*)']

    # Get count of students with pass (average grade >= 40 and < 60)
    cursor.execute('''
        SELECT COUNT(*) FROM students 
        WHERE student_id IN (SELECT student_id FROM grades GROUP BY student_id HAVING AVG(module_grade) >= 40 AND AVG(module_grade) < 60)
    ''')
    pass_count = cursor.fetchone()['COUNT(*)']

    conn.close()

    return render_template('index.html', total_students=total_students, distinction_count=distinction_count, merit_count=merit_count, pass_count=pass_count)


# View all students
@app.route('/students')
def students():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students')
    students = cursor.fetchall()
    conn.close()
    return render_template('students_list.html', students=students)


def generate_student_id():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Get the last inserted student_id
    cursor.execute("SELECT student_id FROM students ORDER BY student_id DESC LIMIT 1;")
    last_id = cursor.fetchone()

    if last_id and 'student_id' in last_id:
        # Extract numeric part and increment by 1
        last_number = int(last_id['student_id'][3:])  # Remove 'STU' prefix and convert to int
        new_number = last_number + 1
    else:
        new_number = 1  # If no record exists, start with 1

    # Format the new ID with leading zeros
    new_id = f"STU{new_number:03}"
    conn.close()
    return new_id


# Add new student
@app.route('/students/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        # Insert the new student into the database
        student_id = generate_student_id()
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        dob = request.form['dob']
        email = request.form['email']
        course_enrolled = request.form['course_enrolled']
        year_of_study = request.form['year_of_study']
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO students (student_id,first_name, last_name, dob, email, course_enrolled, year_of_study)
                        VALUES (%s,%s, %s, %s, %s, %s, %s)''', (student_id,first_name, last_name, dob, email, course_enrolled, year_of_study))
        conn.commit()
        conn.close()

        return redirect(url_for('students'))
    return render_template('add_student.html')

@app.route('/students/<student_id>')
def student_details(student_id):
    # Connect to the database
    conn = get_db_connection()
    cursor = conn.cursor()

    # Fetch the student's basic details
    cursor.execute('SELECT * FROM students WHERE student_id = %s', (student_id,))
    student = cursor.fetchone()

    # Fetch the student's grades
    cursor.execute('SELECT * FROM grades WHERE student_id = %s', (student_id,))
    grades = cursor.fetchall()

    # Calculate average grade for the student
    if grades:
        avg_grade = sum(grade['module_grade'] for grade in grades) / len(grades)
    else:
        avg_grade = None

    # Determine classification
    if avg_grade is not None:
        if avg_grade >= 70:
            status = 'Distinction'
        elif avg_grade >= 60:
            status = 'Merit'
        elif avg_grade >= 40:
            status = 'Pass'
        else:
            status = 'Fail'
    else:
        status = 'No Grades'

    conn.close()

    return render_template('student_detail.html', student=student, grades=grades, avg_grade=avg_grade, status=status)

# Edit student details
@app.route('/students/edit/<student_id>', methods=['GET', 'POST'])
def edit_student(student_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    if request.method == 'GET':
        cursor.execute('SELECT * FROM students WHERE student_id = %s', (student_id,))
        student = cursor.fetchone()
        conn.close()
        return render_template('edit_student.html', student=student)
    
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        dob = request.form['dob']
        email = request.form['email']
        course_enrolled = request.form['course_enrolled']
        year_of_study = request.form['year_of_study']
        
        cursor.execute('''UPDATE students SET first_name = %s, last_name = %s, dob = %s, email = %s, 
                          course_enrolled = %s, year_of_study = %s WHERE student_id = %s''',
                       (first_name, last_name, dob, email, course_enrolled, year_of_study, student_id))
        conn.commit()
        conn.close()

        return redirect(url_for('students'))

# Delete student
@app.route('/students/delete/<student_id>')
def delete_student(student_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM grades WHERE student_id = %s', (student_id,))
    cursor.execute('DELETE FROM students WHERE student_id = %s', (student_id,)) 
    conn.commit()
    conn.close()
    return redirect(url_for('students'))

@app.route('/grades/add', methods=['GET', 'POST'])
def add_grades():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students')
    students = cursor.fetchall()
    conn.close()

    student_id = request.args.get('student_id')  # Get student_id from the URL, if available

    if request.method == 'POST':
        student_id = request.form['student_id']  # Form submission will have student_id
        module_name = request.form['module_name']
        module_grade = int(request.form['module_grade'])
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO grades (student_id, module_name, module_grade)
                        VALUES ( %s, %s, %s)''',
                        (student_id, module_name, module_grade))
        conn.commit()
        conn.close()

        return redirect(url_for('students'))

    return render_template('add_grades.html', students=students, student_id=student_id)

# Edit grades for a student
@app.route('/grades/edit/<id>', methods=['GET', 'POST'])
def edit_grades(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    if request.method == 'GET':
        cursor.execute('SELECT * FROM grades WHERE id = %s', (id,))
        grade = cursor.fetchone()
        student_id = grade['student_id']
        cursor.execute('SELECT * FROM students WHERE student_id=%s',(student_id))
        students = cursor.fetchone()
        
        conn.close()
        return render_template('edit_grades.html', grade=grade, student=students)

    if request.method == 'POST':
        cursor.execute('SELECT * FROM grades WHERE id = %s', (id,))
        grade = cursor.fetchone()
        student_id = grade['student_id']
        module_name = request.form['module_name']
        module_grade = request.form['module_grade']

        cursor.execute('''UPDATE grades SET id = %s, module_name = %s, module_grade = %s WHERE id = %s''',
                        (id, module_name, module_grade, id))
        conn.commit()
        conn.close()

        return redirect(url_for('student_details', student_id=student_id))

# Delete grade
@app.route('/grades/delete/<int:id>', methods=['GET','POST'])
def delete_grade(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM grades WHERE id = %s', (id,))
    grade = cursor.fetchone()
    student_id = grade['student_id']
    cursor.execute('DELETE FROM grades WHERE id = %s', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('student_details', student_id=student_id))

@app.route('/analysis_report', methods=['GET'])
def analysis_report():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Get filter parameters from the form
    name_filter = request.args.get('name', '')
    student_id_filter = request.args.get('student_id', '')
    email_filter = request.args.get('email', '')
    classification_filter = request.args.get('classification', '')
    grade_range_filter = request.args.get('grade_range', '')
    sort_by = request.args.get('sort_by', 'student_id')  # Default sort by student_id
    order_by = request.args.get('order_by', 'ASC')  # Default order is ascending

    # Define the base query
    query = '''
        SELECT student_id, first_name, last_name, email
        FROM students
        WHERE first_name LIKE %s
        AND student_id LIKE %s
        AND email LIKE %s
    '''
    # Add classification filtering if necessary
    if classification_filter:
        if classification_filter == 'Distinction':
            query += ' AND student_id IN (SELECT student_id FROM grades GROUP BY student_id HAVING AVG(module_grade) >= 70)'
        elif classification_filter == 'Merit':
            query += ' AND student_id IN (SELECT student_id FROM grades GROUP BY student_id HAVING AVG(module_grade) >= 60 AND AVG(module_grade) < 70)'
        elif classification_filter == 'Pass':
            query += ' AND student_id IN (SELECT student_id FROM grades GROUP BY student_id HAVING AVG(module_grade) >= 40 AND AVG(module_grade) < 60)'
        elif classification_filter == 'Fail':
            query += ' AND student_id IN (SELECT student_id FROM grades GROUP BY student_id HAVING AVG(module_grade) < 40)'

    # Handle sorting based on the user selection
    if sort_by == 'name':
        query += ' ORDER BY first_name, last_name ' + order_by
    elif sort_by == 'average_grade':
        query += ' ORDER BY (SELECT AVG(module_grade) FROM grades WHERE student_id = students.student_id) ' + order_by
    elif sort_by == 'classification':
        query += ' ORDER BY (CASE WHEN (SELECT AVG(module_grade) FROM grades WHERE student_id = students.student_id) >= 70 THEN "Distinction" '
        query += 'WHEN (SELECT AVG(module_grade) FROM grades WHERE student_id = students.student_id) >= 60 THEN "Merit" '
        query += 'WHEN (SELECT AVG(module_grade) FROM grades WHERE student_id = students.student_id) >= 40 THEN "Pass" ELSE "Fail" END) ' + order_by
    else:
        query += ' ORDER BY student_id ' + order_by

    cursor.execute(query, ('%' + name_filter + '%', '%' + student_id_filter + '%', '%' + email_filter + '%'))
    students = cursor.fetchall()

    student_analysis = []
    for student in students:
        student_id = student['student_id']
        first_name = student['first_name']
        last_name = student['last_name']
        full_name = first_name + ' ' + last_name

        # Fetch all grades for a particular student
        cursor.execute('SELECT module_grade FROM grades WHERE student_id = %s', (student_id,))
        grades = cursor.fetchall()

        if grades:
            grades_list = [grade['module_grade'] for grade in grades if grade['module_grade'] is not None]
            if grades_list:
                avg_grade = sum(grades_list) / len(grades_list)

                # Determine classification
                if avg_grade >= 70:
                    classification = 'Distinction'
                elif avg_grade >= 60:
                    classification = 'Merit'
                elif avg_grade >= 40:
                    classification = 'Pass'
                else:
                    classification = 'Fail'
            else:
                avg_grade = None
                classification = 'No Grades'
        else:
            avg_grade = None
            classification = 'No Grades'

        student_analysis.append({
            'student_id': student_id,
            'first_name': first_name,
            'last_name': last_name,
            'average_grade': round(avg_grade, 2) if avg_grade is not None else 'N/A',
            'classification': classification
        })

    conn.close()
    return render_template('analysis_report.html', students=student_analysis)

if __name__ == '__main__':
    app.run(debug=True)
