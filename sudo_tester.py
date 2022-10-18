from unicodedata import name
from helper_functions import *
from sudo_solver_method1 import sudo_solver


# make a sudo table using the sodo solver:) by using an empty table for starter
empty_table = sudo_table()

# a non empy sudo board
full_sudo = sudo_solver(empty_table)
sudo_board = sudo_maker(full_sudo)

# slove a non-empty sudo board
def sudoku(sudo_board):
    print(f"the sudo bord is {sudo_board}")
    solved_sudo = sudo_solver(sudo_board)
    print(f"The solved sudo is {solved_sudo}")


# if name == __name__:
#     sudoku(sudo_board=sudo_board)

sudoku(sudo_board=sudo_board)
