############################################################
# CIS 521: Homework 2
############################################################

student_name = "Type your full name here."

############################################################
# Imports
############################################################

# Include your imports here, if any are used.
import sys
import math

############################################################
# Section 1: N-Queens
############################################################


def main():
    a = num_placements_all(8)
    print a
    b = num_placements_one_per_row(8)
    print b


def num_placements_all(n):
    board_size = n*n
    possible_placements = 1
    for i in xrange(0,n):
        possible_placements *= board_size
        board_size -= 1
    return possible_placements


def num_placements_one_per_row(n):
    return math.pow(n,n)

def n_queens_valid(board):
    pass

def n_queens_solutions(n):
    pass

############################################################
# Section 2: Lights Out
############################################################

class LightsOutPuzzle(object):

    def __init__(self, board):
        pass

    def get_board(self):
        pass

    def perform_move(self, row, col):
        pass

    def scramble(self):
        pass

    def is_solved(self):
        pass

    def copy(self):
        pass

    def successors(self):
        pass

    def find_solution(self):
        pass

def create_puzzle(rows, cols):
    pass

############################################################
# Section 3: Linear Disk Movement
############################################################

def solve_identical_disks(length, n):
    pass

def solve_distinct_disks(length, n):
    pass

############################################################
# Section 4: Feedback
############################################################

feedback_question_1 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""

feedback_question_2 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""

feedback_question_3 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""
if __name__ == '__main__':
    main()