"""
Class:      SSW-810
Project:    Final Exam
Professor:  James Rowland
Author:     Nick Cohron
Date:       2 December 2017
Brief:      Indexed search
"""


import os
from collections import defaultdict


class SearchWords():
    """Class to act as container for search of text files."""
    def __init__(self, input_dir):
        self.input_dir = input_dir
        self.word_dict = defaultdict(list) # key=word, value=list of (file name, list of unique lines word appears in)
        self.words_read = 0
        self.index()

    def index(self):
        """Method to search files and generate word index."""
        files = self.get_files()
        for file in files:
            self.process_file(file)
        return None

    def lookup(self, word):
        """Method to lookup a specific word and identify all distinct files
        and distinct line numbers it appears in."""
        if word in self.word_dict:
            return sorted(self.word_dict[word])
        else:
            return []

    def summarize(self):
        """Method to summarize the total number of files, total distinct works,
        and total words read in all files."""
        return (len(self.get_files()), len(self.word_dict), self.words_read)

    def get_files(self):
        """Method takes a path and returns a list of files in the directory that end in
        '.txt' (text files)."""
        return [file_name for file_name in os.listdir(self.input_dir) if file_name.endswith(".txt")]

    def process_file(self, file_name):
        """Method to take a file and add word details and count to instance attributes."""
        # file_dir does not need to be checked as it was read from path validated in get_input
        os.chdir(self.input_dir)

        line_index = 0
        # use set for uniqueness (if word appears in line more than once)
        file_dict = defaultdict(set)

        file_handle = open(file_name, 'r')
        with file_handle:
            for line in file_handle:
                words = line.strip().lower().split()
                for word in words:
                    self.words_read += 1
                    file_dict[word].add(line_index)
                line_index += 1

        for key, value in file_dict.items():
            self.word_dict[key].append((file_name, sorted(list(value))))
        return None


def get_input(type_input):
    """Function takes no input parameters, gets user input as a string and returns that string.
    Does not need to use 'try' and 'except' as it uses 'os.path.exists' to check that path exists,
    otherwise recurse with message until get good path from user input.  Will not return until it
    has good input.
    """
    print()
    type_dict = {'path': ('Please enter path to search for .txt files: '), 'word': ('Please enter word to search: ')}
    message = type_dict[type_input]

    # get user input
    user_input = input(message)

    # perform check on input, if fail -> recurse until pass
    if type_input == 'path' and not os.path.exists(user_input):
        print("ERROR 404: Path not found. Please try again.")
        user_input = get_input(type_input)

    return user_input


def main():
    """Main program logic."""
    # get user input for path
    input_path = get_input('path')

    # instantiate class
    instance = SearchWords(input_path)

    # search for a user input word for lookup
    print()
    search_input = get_input('word')
    print("Search result for '", search_input, "' is:", instance.lookup(search_input.lower()))

    # summarize the path search
    file_num, distinct_words, total_words = instance.summarize()
    print()
    print("Summary- ")
    print("   Number of .txt files read =", file_num)
    print("   Number of distinct words read =", distinct_words)
    print("   Total number of words read =", total_words)


if __name__ == "__main__":
    # call main program
    main()


# End of file