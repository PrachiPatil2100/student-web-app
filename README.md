# Student Web App

A simple Flask web application for managing student records using SQLite.

## Features
- Add a new student with name, age, and roll number
- Search students by roll number
- Edit existing student details
- Delete student records
- Display student data in a clean web interface

## Project Root
The project root directory is:

- c:\Projects\student_web_app

## Project Structure
- app.py - Main Flask application
- setup_db.py - Creates the SQLite database and students table
- templates/ - HTML templates for the app
- static/ - CSS files
- students.db - SQLite database file

## Requirements
Install the required packages:

```bash
pip install -r requirements.txt
```

## Setup Instructions
1. Open the project folder:
   ```bash
   cd c:\Projects\student_web_app
   ```
2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create the database and table:
   ```bash
   python setup_db.py
   ```
5. Run the application:
   ```bash
   python app.py
   ```

## Run the App
Open your browser and visit:

```text
http://127.0.0.1:5000/
```

## Notes
- The app uses SQLite, so no extra database server is required.
- The database file will be created automatically when you run setup_db.py.
