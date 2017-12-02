"""
Class:      SSW-810
Project:    Final Exam Tests
Professor:  James Rowland
Author:     Nick Cohron
Date:       2 December 2017
Brief:      Indexed search
"""


import unittest
from FinalExamCohron import SearchWords


class ExamTestSuite(unittest.TestCase):
    """Unit test suite for Final Exam programming assignment"""
    path1 = "/Users/nickcohron/Stevens/TempTestExam"
    path2 = "/Users/nickcohron/Stevens/TempTest"
    test1 = SearchWords(path1)
    test2 = SearchWords(path2)

    def test_get_files(self):
        """Unit tests for '.get_files' method"""
        self.assertEqual(self.test1.get_files(), ['sherlock1.txt', 'sherlock2.txt', 'sherlock3.txt'])
        self.assertEqual(self.test2.get_files(), ['test1.txt', 'test.txt', 'again.txt'])

    def test_lookup(self):
        """Unit tests for '.lookup' method"""
        self.assertEqual(self.test1.lookup('extra'), [('sherlock1.txt', [0]), ('sherlock2.txt', [0])])
        # self.assertEqual(self.test1.lookup('Holmes'), [('sherlock1.txt', [2, 10, 20]), ('sherlock2.txt', [12, 40, 60, 64, 87]), ('sherlock3.txt', [4])])
        # self.assertEqual(self.test1.lookup('Ebook'), [('sherlock1.txt', [4, 7, 14, 20])])
        self.assertEqual(self.test1.lookup('Not_a_word'), [])
        self.assertEqual(self.test2.lookup('watch'), [('again.txt', [1])])
        self.assertEqual(self.test2.lookup('NotAWord'), [])

    def test_summarize(self):
        """Unit tests for '.summarize' method"""
        self.assertEqual(self.test1.summarize(), (3, 592, 1341))
        self.assertEqual(self.test2.summarize(), (3, 12, 22))


if __name__ == "__main__":
    # call the unit tests
    unittest.main(exit=False, verbosity=2)


# End of file
