import random
import copy
from helper_functions import *


def sudo_solver(table):
    table_copy = [row[:] for row in table]
    i = 0
    j = 0
    while i < 9 and j < 9:
        tries = []
        if table[i][j] != 0:
            (i, j) = next_cell(i, j)
            continue
        while table[i][j] == 0:
            place_holder = random.randint(1, 9)
            tries.append(place_holder)
            if (
                (place_holder not in table[i])
                and (place_holder not in sudo_transpose(table)[j])
                and (place_holder not in sudo_3x3(table, i, j))
            ):
                if len([item for item in sudo_3x3(table, i, j) if item != 0]) == 9:
                    if sum(sudo_3x3(table, i, j)) == 45:
                        pass
                    else:
                        break

                table[i][j] = place_holder
                if i == 8 and j == 8:
                    return table

                (i, j) = next_cell(i, j)
                break
            if len(set(tries)) == 9:
                # start from scratch
                i = 0
                j = 0
                table = [row[:] for row in table_copy]
                break
