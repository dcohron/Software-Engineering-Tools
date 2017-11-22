"""
Class:      SSW-810
Project:    Homework #12
Professor:  James Rowland
Author:     Nick Cohron
Date:       22 November 2017
Brief:      Putting student database on the web.
"""


# Notes to self:
# Goto 127.0.0.1:5000 (root) to see rendered web page


from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

@app.route('/instructor_courses')
def instructor_courses():
    """Function to query the database and return result to Flask for web presentation."""
    sqlite_file = '/Applications/sqlite-tools-osx-x86-3210000/810_startup.db'
    query = """SELECT CWID, Name, Dept, course, count(Student_CWID) FROM Instructors 
            JOIN Grades on Instructors.CWID = Grades.Instructor_CWID GROUP BY course 
            ORDER BY Name"""

    conn = sqlite3.connect(sqlite_file)

    c = conn.cursor()

    c.execute(query)

    results = c.fetchall()

    # convert the query results into a list of dictionaries to pass to the template
    data = [{'CWID': cwid, 'Name': name, 'Dept': Dept, 'Course': course, 'Students':count}
                for cwid, name, Dept, course, count in results]

    conn.close()

    return render_template('instructor_courses.html',
                               title='Stevens Repository',
                               table_title="Number of Students by Course and Instructor",
                               instructors=data)

app.run(debug=True)  # automatically restart webserver if anything changes


# End of file