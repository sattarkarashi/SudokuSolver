import numpy as np
from helper_functions import *
from sys import argv


def ranger(i):
    if i < 3:
        i_range = [0, 3]
    if i > 2 and i < 6:
        i_range = [3, 6]
    if i > 5:
        i_range = [6, 9]
    return i_range


def empty_cells(sudo):
    emtpy_cell_items = []
    for i in range(9):
        for j in range(9):
            if sudo[i, j] == 0:
                emtpy_cell_items.append((i, j))
    return emtpy_cell_items


def possible_empty_cell_items(sudo, i, j):
    possible_items = []
    empty_cells = empty_cells(sudo)

    for item in range(10):
        if (
            (not np.count_nonzero(sudo[i] == item))
            and (not np.count_nonzero(sudo[:, j] == item))
            and not (
                np.count_nonzero(
                    sudo[ranger(i)[0] : ranger(i)[1], ranger(j)[0] : ranger(j)[1]]
                    == item
                )
            )
        ):
            possible_items.append(i)

    return possible_items


def SuDoSolver(sudo):
    empty_cells = empty_cells(sudo)
    s = {}
    for k in d:
        s[k] = []

    i = 0
    while True:

        p = d[i][0]
        ph = d[i][1]
        lispos = emp(sudo, p, ph)

        for l in lispos:
            if l not in s[(p, ph)]:
                sudo[p, ph] = l
                s[(p, ph)].append(l)

                i += 1
                break
        else:
            s[(p, ph)] = []
            sudo[p, ph] = 0
            i -= 1
        if i == -1:
            break

        if i > len(d) - 1:
            print(sudo)
            break


sudo(argsv.args[0])
