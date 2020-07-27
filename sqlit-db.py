import sqlite3
MySchool=sqlite3.connect('schooltest.db')
curschool=MySchool.cursor()
curschool.execute('''CREATE TABLE students (
StudentID INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT (20) NOT NULL,
house TEXT,
marks REAL);''')
MySchool.close()
