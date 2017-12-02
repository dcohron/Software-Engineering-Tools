"""
Class:      SSW-810
Project:    Homework #12
Professor:  James Rowland
Author:     Nick Cohron
Date:       22 November 2017
Brief:      Putting student database on the web.
"""


import os
from collections import defaultdict


class SearchWords():
    """Class to act as container for search of text files."""
    def __init__(self, input_dir):
        self.input_dir = input_dir
        self.word_dict = defaultdict(list) # key=word, value=list of (file name, list of unique lines word appears in)
        self.words_read = 0

    def index(self):
        """Method to search files and generate word index."""
        files = self.get_files()
        for file in files:
            self.process_file(file)
        return None

    def lookup(self, word):
        """Method to lookup a specific word and identify all distinct files
        and distinct line numbers it appears in."""
        self.index()
        return self.word_dict[word]

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
        lines_appearing = set()  # use set for uniqueness (do list line number if word appears in line more than once
        file_dict = defaultdict(set)

        file_handle = open(file_name, 'r')
        with file_handle:
            for line in file_handle:
                words = line.strip().lower().split()
                for word in words:
                    self.words_read += 1
                    file_dict[word].add(line_index)
                line_index += 1
        print(file_dict)
        for key, value in file_dict.items():
            self.word_dict[key].append((file_name, list(value)))
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

    # # save current working directory for restoration at end
    # cwd = os.getcwd()
    #
    # # change working directory to the path given by user
    # os.chdir(input_path)
    # print(os.getcwd())

    # # get all '.txt' files from that path
    # file_list = get_files(input_path)
    # print(file_list)

    # instantiate class
    instance = SearchWords(input_path)
    print(instance.get_files())
    print(instance.summarize())

    # search for a user input word for lookup
    search_input = get_input('word')
    print("Search result for '", search_input, "' is:", instance.lookup(search_input.lower()))

    # summarize the path search
    file_num, distinct_words, total_words = instance.summarize()
    print("Summary- ")
    print("   Number of .txt files read =", file_num)
    print("   Number of distinct words read =", distinct_words)
    print("   Total number of words read =", total_words)


    # # restore working directory
    # os.chdir(cwd)

if __name__ == "__main__":
    # call main program
    main()


# End of file