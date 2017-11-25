"""
Class:      SSW-810
Project:    Optional Practice Assignment
Professor:  James Rowland
Author:     Nick Cohron
Date:       24 November 2017
Brief:      Tic Tac Toe rendered to the web.
"""


# Notes to self:
# Goto 127.0.0.1:5000 (root) to see rendered web page


from flask import Flask, request, render_template
import random
import itertools
from prettytable import PrettyTable as PT

# app = Flask(__name__)

class TTTGame():
    """Class to contain data structures and methods for Tic Tac Toe game."""
    states = ('X', 'O', '_')

    def __init__(self, size):
        """Generates initial board state."""
        self.size = size
        self.board = [[0] * self.size for i in range(self.size)]
        for x, y in itertools.product(range(self.size), range(self.size)):
            self.board[x][y] = random.choice(self.states)
        return None

    def __str__(self):
        board_rep = ""
        for x, y in itertools.product(range(self.size), range(self.size)):
            board_rep = board_rep + '[' + str(x) +',' + str(y) +']=' + self.board[x][y] + " "
        return board_rep

    # @app.route('/')
    def display_board(self):
        """Function to present the board to Flask for web presentation."""
        return render_template('game_board.html',
                                   title='Tic Tac Toe',
                                   table_title="The Game Board",
                                   size=self.size,
                                   board=self.board)

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
            print(z_list, type(z_list))
            z.add_row = (z_list)
        # print(z.get_string())
        print()
        print("Pretty Table:")
        print(z)
        return None

    def check_win(self):
        """Function to determine if there is a win on the board."""
        # check row win

        # check column win

        # check left to right diagonal win

        # check right to left diagonal win

        return False

    # def check(self, x, y):
    #     """Function iterates over cells looking for win."""
    #     previous_cell_state = None
    #     for a in range(x):
    #         for b in range(y):
    #             cell_state = self.board[a, b]
    #             if previous_cell_state == None:
    #                 previous_cell_state = cell_state
    #             elif cell_state != previous_cell_state:
    #                 break
    #             elif b == self.size-1:
    #                 return True
    #     return False
    #
    # def check_diag(self, flag):
    #     """Function to check diagonal wins. Flag tells whether to start
    #     at position 0,0 (top left) or N, 0 (bottom left)."""
    #     pass
    #     return


def get_size_input():
    """Function takes no input parameters, gets user input as a string and returns that string.
    Does not need to use 'try' and 'except' as it casts string to integer, if fail on cast
    recurse with message until get good input from user input.  Will not return until it
    has good input.
    """
    print()
    input_size = input("Please enter a single integer for size of board ('3' will yield 3x3 board): ")

    # now check that file exists, else recursive call
    if not type(int(input_size)) == int:
        print("ERROR: Not an integer, please try again.")
        input_size = get_size()

    return int(input_size)


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

    # output results to web
    # board.display_board()

    # check for win on board
    if board.check_win():
        print("We have a winner!")
    else:
        print("No winner this time.")

    return


if __name__ == "__main__":
    # do the main program loop
    # app.run(debug=True)  # automatically restart webserver if anything changes
    main()

    # do unit tests
    # unittest.main(exit=False, verbosity=2)


# End of File