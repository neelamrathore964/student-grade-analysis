# Student Grade Analysis

This web-based application allows you to manage and analyse student grade data. You can add, edit, and delete student records, as well as analyse student performance based on average grades and classifications. The app also offers filtering and sorting options for better data analysis.

## Features

- **Student Management**: Add, edit, and delete student records.
- **Grade Management**: Manage grades, calculate average grades, and classify student performance (Pass, Merit, Distinction).
- **Performance Analysis**: View and filter student performance data, including sorting by name, ID, and grade.

## Tech Stack

- **Backend**: Python (Flask)
- **Database**: MySQL
- **Frontend**: HTML, CSS, Bootstrap
- **Others**: Git (version control)

## Installation & Setup

### Prerequisites

1. **Python 3.x**: Ensure Python is installed.
2. **MySQL**: Ensure MySQL is installed and configured for this project.

### Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/neelamrathore964/student-grade-analysis.git
   cd student-grade-analysis
   ```

2. **Set up the MySQL Database**:

   - Create the database and tables:
     ```sql
     CREATE DATABASE IF NOT EXISTS student_management_db;
     USE student_management_db;

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

3. **Set Environment Variables**:

   Before running the app, configure your MySQL credentials via environment variables. In your terminal, run:

   ```bash
   export DB_HOST="localhost"
   export DB_USER="your_username"
   export DB_PASSWORD="your_password"
   export DB_NAME="student_management_db"
   ```

   Replace `your_username` and `your_password` with your MySQL credentials.

4. **Install Dependencies**:

   Install the required Python packages by running:

   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Flask Application**:

   Once the environment variables are set and dependencies are installed, start the app with:

   ```bash
   python app.py
   ```

6. **Access the Application**:

   Open your web browser and visit `http://localhost:5000` to use the app.

## Directory Structure

```
student-grade-analysis/
│
├── app.py                  # Main application file with route definitions and logic
├── templates/              # Contains HTML templates
│   ├── base.html           # Base layout template
│   ├── index.html          # Homepage template
│   ├── add_student.html    # Add a new student form
│   ├── edit_student.html   # Edit student form
│   ├── add_grade.html      # Add a new grade form
│   ├── edit_grades.html    # Edit grade form
│   ├── student_list.html   # List of students
│   ├── student_detail.html # Student details (grades & classification)
│   └── analysis_report.html # Student performance analysis
│
├── static/                 # Static files (CSS, JS, Images)
│   ├── style.css           # Custom styles
│   ├── bootstrap.min.css   # Bootstrap CSS
│   └── bootstrap.bundle.min.js # Bootstrap JS
│
├── database/               # Database-related files
│   ├── db_connection.py    # Database connection code
│   ├── sql.init            # SQL setup file
│   └── student_management_db.sql # Database schema
│
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

## Usage

- **Home Page**: Displays an overview of student performance (total students, classification breakdown).
- **Add Student**: Form to add a new student.
- **Edit Student**: Modify existing student records.
- **Add Grade**: Form to add grades for a student.
- **Edit Grade**: Modify a student's grade for a specific module.
- **Delete Grade**: Remove a grade for a student.
- **Analysis Report**: View a report on student performance, with options to filter and sort by various criteria.

### Available Routes:
- `/students`: List of all students.
- `/students/add`: Add a new student.
- `/students/edit/<student_id>`: Edit a student's details.
- `/students/delete/<student_id>`: Delete a student.
- `/grades/add`: Add grades for a student.
- `/grades/edit/<id>`: Edit a grade.
- `/grades/delete/<id>`: Delete a grade.
- `/analysis_report`: View student performance analysis.