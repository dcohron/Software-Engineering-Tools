"""
Class:      SSW-810
Project:    Homework #10
Professor:  James Rowland
Author:     Nick Cohron
Date:       12 November 2017
Brief:      Stevens student records week #2
"""


# import os
import unittest
from prettytable import PrettyTable as PT
from collections import defaultdict


class HomeworkTestSuite(unittest.TestCase):
    """Unit test suite for homework functions"""
    # This test suite is not as strong as usual.

    def test_read_students(self):
        """Unit tests for function 'read_students'."""
        self.assertEqual(read_students("Test9.txt"), [])  # file with empty lines
        self.assertRaises(SystemExit, read_students, "not_there.txt")   # file does not exist

    def test_read_instructors(self):
        """Unit tests for function 'read_instructors'."""
        self.assertEqual(read_instructors("Test9.txt"), [])   # file with empty lines
        self.assertRaises(SystemExit, read_students, "not_there.txt")   # file does not exist

    def test_read_grades(self):
        """Unit tests for function 'read_grades'."""
        self.assertEqual(read_grades('Testgrades.txt', [], []), None)   # file with lines with no grades and bad format
        self.assertEqual(read_grades("Test9.txt", [], []), None)  # file with empty lines
        self.assertRaises(SystemExit, read_students, "not_there.txt")  # file does not exist


class School():
    """Class that is a repository for an academic institution.  Will hold student, professor
      and major data including classes taken, classes required and grades achieved."""

    def __init__(self, school):
        """Instantiate an instance of the class School."""
        self.school = school
        self.students = list()
        self.instructors = list()

    def read_students(self, file_name):
        """Read the student input file."""
        # test that can read file
        try:
            fhand = open(file_name, 'r')
        except IOError:
            print("ERROR: cannot read file '%s'." % file_name)
            exit(99)

        with fhand:
            for line in fhand:
                try:
                    words = line.strip().split("\t")
                    new_instance = Student(words[0], words[1], words[2])
                except IndexError:
                    print("ERROR: line formatted incorrectly in '%s'. Continuing to next line." % file_name)
                    continue
                self.students.append(new_instance)
        return None

    def read_instructors(self, file_name):
        """Read the instructor input file."""
        # test that can read file
        try:
            fhand = open(file_name, 'r')
        except IOError:
            print("ERROR: cannot read file '%s'." % file_name)
            exit(99)

        with fhand:
            for line in fhand:
                try:
                    words = line.strip().split("\t")
                    instance_name = Instructor(words[0], words[1], words[2])
                except IndexError:
                    print("ERROR: line formatted incorrectly in '%s'. Continuing to next line." % file_name)
                    continue
                self.instructors.append(instance_name)
        return

    def read_grades(self, file_name):
        """Read the grades input file."""
        # test that can read file
        try:
            fhand = open(file_name, 'r')
        except IOError:
            print("ERROR: cannot read file '%s'." % file_name)
            exit(99)

        with fhand:
            for line in fhand:
                words = line.strip().split("\t")
                # must allow for registered classes without grades yet assigned
                try:
                    if len(words) == 3:
                        stud = words[0]
                        cour = words[1]
                        grade = 'NA'
                        prof = words[2]
                    else:
                        stud = words[0]
                        cour = words[1]
                        grade = words[2]
                        prof = words[3]
                except IndexError:
                    print("ERROR: line formatted incorrectly in '%s'. Continuing to next line." % file_name)
                    continue

                # I think that there is a better way to do the following than using loops
                for item in self.students:
                    if item.CWID == stud:
                        item.courses[cour] = grade
                for item in self.instructors:
                    if item.CWID == prof:
                        item.courses[cour] += 1
        return None

    def student_table(self):
        """Get pretty table as output for students"""
        # 'Registered' instead of 'Completed' as may not have grades for all classes yet
        print()
        print("Student Summary:")
        header = ["CWID", "Name", "Major", "Registered Courses"]
        x = PT(header)
        for item in self.students:
            x.add_row([str(item.CWID), str(item.name), str(item.major), sorted(list(item.courses.keys()))])
        print(x)
        return None

    def instructor_table(self):
        """Get pretty table as output for instructors"""
        print()
        print("Instructor Summary:")
        # decided to display 'Dept' as well, though not required by assignment
        header = ["CWID", "Name", "Dept", "Course", "Students"]
        x = PT(header)
        for item in self.instructors:
            class_list = list(item.courses.keys())
            for subject in class_list:
                x.add_row([str(item.CWID), str(item.name), str(item.dept), subject, item.courses[subject]])
        print(x)
        return None


class Student():
    """Class to store the student data."""
    def __init__(self, CWID, name, major):
        """Instantiate an instance of the class Student."""
        self.CWID = CWID
        self.name = name
        self.major = major
        self.courses = dict()  # key = course number, value = grade received

    def __str__(self):
        """Returns a string for the student."""
        return (str(self.CWID) + " " + str(self.name) + " " +  str(self.major))

    def add_course(self, course, grade='NA'):
        self.courses[course] = grade
        return

class Instructor():
    """Class to store the professor data."""
    def __init__(self, CWID, name, dept):
        """Instantiate an instance of the class Instructor."""
        self.CWID = CWID
        self.name = name
        self.dept = dept
        self.courses = defaultdict(int) # key = course number, value = count of students

    def __str__(self):
        """Returns a string for the professor."""
        return (str(self.CWID) + " " + str(self.name) + " " + str(self.dept))

    def add_student(self):
        self.courses[course] += 1
        return


def main():
    """Main program logic."""

    Stevens = School('Stevens')

    # input file paths
    input_student = "/Users/nickcohron/Stevens/Software Engineering Tools & Techniques/Code/Data/students.txt"
    input_instructors = "/Users/nickcohron/Stevens/Software Engineering Tools & Techniques/Code/Data/instructors.txt"
    input_grades = "/Users/nickcohron/Stevens/Software Engineering Tools & Techniques/Code/Data/grades.txt"

    # read in data
    Stevens.read_students(input_student)
    Stevens.read_instructors(input_instructors)
    Stevens.read_grades(input_grades)

    # print student table
    Stevens.student_table()

    # print instructor table
    Stevens.instructor_table()



if __name__ == "__main__":
    # call main program
    main()

    # now call the unit tests
    # unittest.main(exit=False, verbosity=2)


# End of file