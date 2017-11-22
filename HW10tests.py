"""
Class:      SSW-810
Project:    Homework #10
Professor:  James Rowland
Author:     Nick Cohron
Date:       12 November 2017
Brief:      Tests for Homework #10
"""


import unittest
from Homework10Cohron import School


class HomeworkTestSuite(unittest.TestCase):
    """Unit test suite for homework functions"""
    # First instantiate an instance of class School to test on
    USNA = School('USNA')

    def test_read_students(self):
        """Unit tests for function 'read_students'."""
        self.assertEqual(self.USNA.read_students("/Users/nickcohron/Stevens/Software Engineering Tools & Techniques/Code/Software-Engineering-Tools/Tests/Test9.txt"), None)  # file with empty lines
        self.assertRaises(SystemExit, self.USNA.read_students, "not_there.txt")   # file does not exist

    def test_read_instructors(self):
        """Unit tests for function 'read_instructors'."""
        self.assertEqual(self.USNA.read_instructors("/Users/nickcohron/Stevens/Software Engineering Tools & Techniques/Code/Software-Engineering-Tools/Tests/Test9.txt"), None)   # file with empty lines
        self.assertRaises(SystemExit, self.USNA.read_students, "not_there.txt")   # file does not exist

    def test_read_grades(self):
        """Unit tests for function 'read_grades'."""
        self.assertEqual(self.USNA.read_grades('/Users/nickcohron/Stevens/Software Engineering Tools & Techniques/Code/Software-Engineering-Tools/Tests/Testgrades.txt'), None)   # file with lines with no grades and bad format
        self.assertEqual(self.USNA.read_grades("/Users/nickcohron/Stevens/Software Engineering Tools & Techniques/Code/Software-Engineering-Tools/Tests/Test9.txt"), None)  # file with empty lines
        self.assertRaises(SystemExit, self.USNA.read_students, "not_there.txt")  # file does not exist


if __name__ == "__main__":
    # call the unit tests
    unittest.main(exit=False, verbosity=2)


# End of file