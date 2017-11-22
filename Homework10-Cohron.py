"""
Class:      SSW-810
Project:    Homework #10
Professor:  James Rowland
Author:     Nick Cohron
Date:       12 November 2017
Brief:      Stevens student records week #2
"""


from prettytable import PrettyTable as PT
from collections import defaultdict


class School():
    """Class that is a repository for an academic institution.  Will hold student, professor
      and major data including classes taken, classes required and grades achieved."""

    def __init__(self, school):
        """Instantiate an instance of the class School."""
        self.school = school
        self.students = list()
        self.instructors = list()
        self.majors = defaultdict(Major)

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

    def read_majors(self, file_name):
        # test that can read file
        try:
            fhand = open(file_name, 'r')
        except IOError:
            print("ERROR: cannot read file '%s'." % file_name)
            exit(99)

        with fhand:
            for line in fhand:
                words = line.strip().split("\t")
                dept, required, course = words[0], words[1], words[2]
                self.majors[dept].add_course(required, course)
        return None


    def courses_remaining(self, student):
        """Method to calculate the courses remaining, both required and elective."""
        required = self.majors[student.major].required_courses
        elective = self.majors[student.major].elective_courses
        passing_grades = ['A', 'A-', 'B+', 'B', 'B-', 'C+', 'C']
        passed_courses = set()

        for course, grade in student.courses.items():
            if grade in passing_grades:
                passed_courses.add(course)
        if len(elective.intersection(passed_courses)) > 0:
            elective_remaining = []
        else:
            elective_remaining = elective
        return(passed_courses, required.difference(passed_courses), elective_remaining)


    def student_table(self):
        """Get pretty table as output for students"""
        print()
        print("Student Summary:")
        header = ["CWID", "Name", "Major", "Courses Completed w/ grade >= C", "Remaining Required", "Remaining Electives"]
        x = PT(header)
        for item in self.students:
            # First get difference between required and completed classes passed satisfactorily (grade >= 'C')
            passed_courses, required_remaining, elective_remaining = self.courses_remaining(item)
            x.add_row([str(item.CWID), str(item.name), str(item.major), sorted(passed_courses), sorted(required_remaining), sorted(elective_remaining)])
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

    def major_table(self):
        """Get pretty table as output of majors"""
        print()
        print("Major Summary:")
        header = ['Dept', 'Required', 'Elective']
        x = PT(header)
        for key in self.majors.keys():
            x.add_row([key, sorted(self.majors[key].required_courses), sorted(self.majors[key].elective_courses)])
        print(x)
        return None


class Student():
    """Class to store the student data."""
    def __init__(self, CWID, name, major):
        """Instantiate an instance of the class Student."""
        self.CWID = CWID
        self.name = name
        self.major = major
        self.courses = dict()  # key = course name, value = grade received

    def __str__(self):
        """Returns a string for the student."""
        return (str(self.CWID) + " " + str(self.name) + " " +  str(self.major))

    def add_course(self, course, grade='NA'):
        """Method to add a course to a dictionary of courses key = course name, value = grade."""
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
        """Method to add a student to a course count."""
        self.courses[course] += 1
        return


class Major():
    """Class to store the required and elective requirements of a major."""
    def __init__(self):
        """Instantiate and instance of the Major class."""
        self.required_courses = set()
        self.elective_courses = set()

    def add_course(self, required, course):
        """Method to add a required or elective course to a major."""
        if required == 'R':
            self.required_courses.add(course)
        elif required == 'E':
            self.elective_courses.add(course)
        else:
            print("ERROR: course type is incorrect for course %s" %course)
        return None


def main():
    """Main program logic."""
    Stevens = School('Stevens')

    # input file paths
    input_student = "/Users/nickcohron/Stevens/Software Engineering Tools & Techniques/Code/Software-Engineering-Tools/Data/students.txt"
    input_instructors = "/Users/nickcohron/Stevens/Software Engineering Tools & Techniques/Code/Software-Engineering-Tools/Data/instructors.txt"
    input_grades = "/Users/nickcohron/Stevens/Software Engineering Tools & Techniques/Code/Software-Engineering-Tools/Data/grades.txt"
    input_grades2 = "/Users/nickcohron/Stevens/Software Engineering Tools & Techniques/Code/Software-Engineering-Tools/Data/grades2.txt"
    input_majors = "/Users/nickcohron/Stevens/Software Engineering Tools & Techniques/Code/Software-Engineering-Tools/Data/majors2.txt"

    # read in data
    Stevens.read_students(input_student)
    Stevens.read_instructors(input_instructors)
    Stevens.read_grades(input_grades2)
    Stevens.read_majors(input_majors)

    # print majors table
    Stevens.major_table()

    # print student table
    Stevens.student_table()

    # print instructor table
    Stevens.instructor_table()


if __name__ == "__main__":
    # call main program
    main()


# End of file