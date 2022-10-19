from sudo_solver import sudo_solver
from helper_functions import sudo_table
import sys

# slove a non-empty sudo board
def sudoku(sudo_board):
    print(f"the sudo bord is {sudo_board}")
    solved_sudo = sudo_solver(sudo_board)
    print(f"The solved sudo is {solved_sudo}")


def process_table(table):
    for item in ["[", "]", ",", " "]:
        table = table.replace(item, "")

    target_table = sudo_table()
    index = 0
    for i in range(9):
        for j in range(9):
            target_table[i][j] = int(table[index])
            index += 1
    return target_table


def solve_my_sudo():
    try:
        sudo_table = input("Insert your desired sudo table: ")
        table = process_table(sudo_table)
        solved_sudo = sudo_solver(table)
        print("Here is the solved sudoku table \n")
        print(solved_sudo)
    except:
        print('Insert the right input which is "python sudo_solver your_desired_table"')


solve_my_sudo()
