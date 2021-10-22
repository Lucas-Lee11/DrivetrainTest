'''
Forgotten Charger: Lewis Cass, Aryaman Goenka, Oscar Wang
Softdev
K16: Database and SQL Introduction
2021-10-25
time spent: ~90 min
'''

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================

# < < < INSERT YOUR TEAM'S POPULATE-THE-DB CODE HERE > > >


# Clear the table first
# Re-creating tables when they already exist causes errors
command = "DROP TABLE IF EXISTS students"
c.execute(command)

# Create new table
command = "CREATE TABLE students (name TEXT, age INTEGER, id INTEGER)"
c.execute(command)

# Populate student table
filename = "students.csv"
with open(filename) as f:
    csvreader = csv.DictReader(f)

    for row in csvreader:
        name = row['name']
        age = int(row['age'])
        id = int(row['id'])

        # Quotes around `name` since it is a text field
        command = f"""INSERT INTO students VALUES("{name}", {age}, {id})"""
        c.execute(command)

# Clear the table first to prevent errors
command = "DROP TABLE IF EXISTS courses"
c.execute(command)

# Create new table
command = "CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER)"
c.execute(command)

filename = "courses.csv"
with open(filename) as f:
    csvreader = csv.DictReader(f)

    for row in csvreader:
        code = row['code']
        mark = int(row['mark'])
        id = int(row['id'])

        # Quotes around code since it is a text field
        command = f"""INSERT INTO courses VALUES("{code}", {mark}, {id})"""
        c.execute(command)


#==========================================================

db.commit() #save changes
db.close()  #close database
