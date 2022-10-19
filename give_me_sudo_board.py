from helper_functions import *
from sudo_solver import sudo_solver
from sys import argv


# make a sudo table using the sodo solver:) by using an empty table for starter
empty_table = sudo_table()

# a non empy sudo board
full_sudo = sudo_solver(empty_table)


def show_me_board():
    difficulty_level = input("Inser your desired difficulty level from 0 to 100: ")
    print(sudo_maker(full_sudo, int(difficulty_level)))


# give me a sudo table with your desired difficutly level from o to 100
show_me_board()
