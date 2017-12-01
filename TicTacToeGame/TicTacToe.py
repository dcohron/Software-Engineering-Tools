"""
Class:      SSW-810
Project:    Optional Practice Assignment
Professor:  James Rowland
Author:     Nick Cohron
Date:       24 November 2017
Brief:      Tic Tac Toe rendered to the console (and soon to the web).
"""


# Notes to self:
# Goto 127.0.0.1:5000 (root) to see rendered web page


from flask import Flask, render_template
import random
import itertools
from collections import defaultdict
from prettytable import PrettyTable as PT
import unittest


# app = Flask(__name__)


class HomeworkTest(unittest.TestCase):
    """Unit tests for this script."""

    def test_check_win(self):
        """Verify that function 'check_win' is functioning properly."""
        test_board = TTTGame(3)

        self.assertEqual(test_board.check_win(), (False, 'No winner'))


class TTTGame():
    """Class to contain data structures and methods for Tic Tac Toe game."""
    STATES = ('X', 'O', '_')

    def __init__(self, size):
        """Generates initial board state."""
        self.size = size
        self.board = [[0] * self.size for i in range(self.size)]
        for x, y in itertools.product(range(self.size), range(self.size)):
            self.board[x][y] = random.choice(self.STATES)

    def __str__(self):
        board_rep = ""
        for x, y in itertools.product(range(self.size), range(self.size)):
            board_rep = board_rep + '[' + str(x) +',' + str(y) +']=' + self.board[x][y] + " "
        return board_rep

    def print_board(self):
        """Function to print out a pretty table of the game board."""
        print()
        print("Tic Tac Toe Game Board:")
        header = list()
        count = 0
        for column in range(self.size):
            count +=1
            header.append(str(count))
        header = ["Row/Column"] + header
        z = PT(header)
        for x in range(self.size):
            z_list=list()
            for y in range(self.size):
                z_list.append(self.board[x][y])
            z_list = [str(x+1)] + z_list
            # print(z_list, type(z_list))
            z.add_row(z_list)
        # print(z.get_string())
        print()
        print("Pretty Table:")
        print(z)
        return None

    def check_win(self):
        """Function to determine if there is a win on the board."""
        # check row win
        for a in range(self.size):
            win_dict = defaultdict(int)
            for b in range(self.size):
                if self.board[a][b] == "_":
                    continue
                win_dict[self.board[a][b]] += 1
            try:
                if win_dict[max(win_dict, key=win_dict.get)] == self.size:
                    return (True, 'Row ' + str(a+1))
            except ValueError:
                continue

        # check column win
        for b in range(self.size):
            win_dict = defaultdict(int)
            for a in range(self.size):
                if self.board[a][b] == "_":
                    continue
                win_dict[self.board[a][b]] += 1
            try:
                if win_dict[max(win_dict, key=win_dict.get)] == self.size:
                    return (True, 'Column ' + str(b+1))
            except ValueError:
                continue

        # check left to right diagonal win
        win_dict = defaultdict(int)
        for a in range(self.size):
            if self.board[a][a] == "_":
                break
            win_dict[self.board[a][a]] += 1
        try:
            if win_dict[max(win_dict, key=win_dict.get)] == self.size:
                return (True, 'Diagonal- top left to bottom right')
        except ValueError:
            # do nothing, continue to next test

        # check right to left diagonal win
            win_dict = defaultdict(int)
            for a in range(self.size-1, -1, -1):
                if self.board[a][self.size-(a+1)] == "_":
                    break
                win_dict[self.board[a][self.size-(a+1)]] += 1
            try:
                if win_dict[max(win_dict, key=win_dict.get)] == self.size:
                    return (True, 'Diagonal- bottom left to top right')
            except ValueError:
                pass
                # do nothing, finished test conditions for a win
        # if have not returned already from finding a win condition
        # now must return False for no win condition found
        return (False, 'No winner')


# global variables required by Flask
# board_size = 0
# board = TTTGame(0)


def get_size_input():
    """Function takes no input parameters, gets user input as a string and returns that string.
    Does not need to use 'try' and 'except' as it casts string to integer, if fail on cast
    recurse with message until get good input from user input.  Will not return until it
    has good input.
    """
    print()
    input_size = input("Please enter a single integer for size of board ('3' will yield 3x3 board): ")

    # check that input was correct, else recursive call
    if not type(int(input_size)) == int:
        print("ERROR: Not an integer, please try again.")
        input_size = get_size()

    return int(input_size)


# @app.route('/')
# def display_board():
#     """Function to present the board to Flask for web presentation."""
#     return render_template('game_board.html',
#                                title='Tic Tac Toe',
#                                table_title="The Game Board",
#                                size=board_size,
#                                board=board)


def main():
    """Main program logic."""
    # perform heavy lifting in the functions and methods

    # get input for board size
    board_size = get_size_input()
    print()

    # initialize game board
    board = TTTGame(board_size)
    print(board)
    print()

    # output results to console
    board.print_board()
    print()

    # check for win on board
    win_bool, location = board.check_win()
    if win_bool:
        print("We have a winner at", location)
    else:
        print("No winner this time.")

    # output results to web
    # app.run(debug=True)  # automatically restart web server if anything changes

    # replay or exit
    try:
        again = input('Would you like to play again? y/n ')
        if again[0].lower() == 'y':
            main()
        else:
            print('Thank you for playing.')
    except TypeError:
        print('ERROR: type error.  Closing program.')

    return


if __name__ == "__main__":
    # do the main program loop
    main()

    # do unit tests
    # unittest.main(exit=False, verbosity=2)


# End of File