# Student Grade Analysis

This web-based application is designed to manage and analyse student grade data. It provides functionality to add, edit, and delete student records, as well as analyse student performance with average grades and classifications. The application also includes filtering and sorting options for better analysis of student data.

## Features

1. **Student Management:**
   - Add new students to the database.
   - Edit existing student records.
   - Delete student records and their related grades.

2. **Grade Management:**
   - Add, edit, and delete grades for students.
   - Automatically calculate the average grade for each student.
   - Classify student performance into Pass(40%+), Merit(60%+), or Distinction(70%+) based on their average grade.

3. **Student Performance Analysis:**
   - Display a list of students along with their average grades and classifications.
   - Filter students by:
     - Student Name
     - Student ID
     - Student Email
     - Classification (Pass, Merit, Distinction)
   - Sort students by:
     - Student ID
     - Name
     - Average Grade
     - Classification
   - Dashboard showing the total number of students, as well as the number of students in each classification.

## Tech Stack

This application is built using the following technologies:

- **Backend:**
  - **Python**: The programming language used to build the application.
  - **Flask**: A lightweight web framework for Python used to manage routes, handle requests, and render HTML templates.
  - **MySQL**: A relational database management system to store student and grade data.
  - **MySQL Connector for Python**: A MySQL database connector for Python that allows us to interact with the database.

- **Frontend:**
  - **HTML**: Markup language for structuring web pages.
  - **CSS**: Styling language for designing the user interface.
  - **Bootstrap**: A CSS framework used for responsive design and easy layout management.

- **Others:**
  - **Git**: Version control system for managing source code.

## Installation & Setup

### Prerequisites

1. **Python 3.x** - Make sure Python is installed on your system.
2. **MySQL** - Ensure that MySQL is installed and set up for this project.
3. **MySQL Connector for Python** - Install the MySQL connector for Python:
   ```bash
   pip install mysql-connector-python
   ```

4. **Flask** - Install Flask using:
   ```bash
   pip install flask
   ```

5. **Bootstrap** - Bootstrap CSS and JS are included via CDN or the link using downloaded files for frontend styling.

### Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone github.com:neelamrathore964/student-grade-analysis.git
   cd student-grade-analysis
   ```

2. **Create and set up the MySQL database:**

   1. Create the `student_management_db` database in MySQL:
   ```sql
   CREATE DATABASE IF NOT EXISTS student_management_db;
   USE student_management_db;
   ```

   2. Create the `students` and `grades` tables:
   ```sql
   CREATE TABLE students (
       id INT PRIMARY KEY AUTO_INCREMENT,
       student_id VARCHAR(10) NOT NULL,
       first_name VARCHAR(50),
       last_name VARCHAR(50),
       dob DATE,
       gender VARCHAR(10),
       email VARCHAR(100),
       phone VARCHAR(15),
       address VARCHAR(255),
       course_enrolled VARCHAR(100),
       year_of_study INT
   );

   CREATE TABLE grades (
       id INT PRIMARY KEY AUTO_INCREMENT,
       student_id VARCHAR(10),
       module_name VARCHAR(100),
       module_grade FLOAT,
       FOREIGN KEY (student_id) REFERENCES students(student_id)
   );
   ```

3. **Configure the database connection:**

   In `app.py`, update the `get_db_connection()` function to use your MySQL credentials:
   ```python
   def get_db_connection():
       return mysql.connector.connect(
           host='localhost',
           user='your_user',
           password='your_password',
           database='student_management_db'
       )
   ```

4. **Run the Flask application:**
   ```bash
   python app.py
   ```

5. **Access the application:**
   Open a web browser and go to `http://localhost:5000` to access the application.

## Directory Structure

The project has the following directory structure:

```
student-grade-analysis/
│
├── app.py                  # Main application file with route definitions and logic
├── templates/              # Contains HTML templates
│   ├── base.html           # Base template used for common layout
│   ├── index.html          # Homepage template
│   ├── add_student.html    # Form to add a new student
│   ├── edit_student.html   # Form to edit an existing student's details
│   ├── add_grade.html      # Form to add grades for a student
│   ├── edit_grades.html    # Form to edit grades for a student
│   ├── student_list.html   # Displays the list of students
│   ├── student_detail.html # Displays the details of a student, including grades and performance classification
│   └── analysis_report.html # Template for displaying student analysis
│
├── static/                 # Static files such as CSS, JavaScript, images
│   ├── style.css           # Custom stylesheets
│   ├── bootstrap.min.css   # Bootstrap CSS
│   └── bootstrap.bundle.min.js # Bootstrap JS
│
├── database/               # Database-related files
│   ├── db_connection.py    # Database connection handling code
│   ├── sql.init            # Initial setup SQL file
│   └── student_management_db.sql # SQL file for creating tables and schema
│
├── requirements.txt        # List of required Python packages
└── README.md               # This file
```

## Requirements

You can install the required Python dependencies by running:

```bash
pip install -r requirements.txt
```

## Usage

- **Home Page**: Displays an overview of student performance, including total students and a breakdown by classification (Pass, Merit, Distinction).
- **Add Student**: A form to add new students with personal details.
- **Edit Student**: A form to modify student records and their grades.
- **Analysis Report**: Displays a summary of all students, their average grades, and classifications (Pass, Merit, Distinction). It includes options to filter and sort students by name, ID, classification, and average grade.

### Available Routes:
- `/students`: Displays the list of all students.
- `/students/add`: Add a new student.
- `/students/edit/<student_id>`: Edit a student's details .
- `/students/delete/<student_id>`: Delete a student and their grades.
- `/grades/edit/<id>`: Edit a grade.
- `/grades/delete/<id>`: Delete a grade.
- `/analysis_report`: View a student performance analysis.
