import random

# emtpy sudo table
def sudo_table():
    sudo_tb = []
    for i in range(9):
        sudo_tb.append([])
        for j in range(9):
            sudo_tb[i].append(0)

    return sudo_tb


# Sudo table tranpose maker
def sudo_transpose(table):
    emp_table = sudo_table()
    for i in range(9):
        for j in range(9):
            emp_table[i][j] = table[j][i]

    return emp_table


# range maker
def table_3x3(i):
    if i / 3 < 1:
        i_range = [0, 3]
    elif i / 3 >= 1 and i / 3 < 2:
        i_range = [3, 6]
    else:
        i_range = [6, 9]

    return i_range


# 3x3 square to list
def sudo_3x3(table, i, j):
    i_range = table_3x3(i)
    j_range = table_3x3(j)
    square_list = []
    for i in range(i_range[0], i_range[1]):
        for j in range(j_range[0], j_range[1]):
            square_list.append(table[i][j])

    return square_list


# next cell
def next_cell(i, j):
    if j == 8:
        i += 1
        j = 0
    else:
        j += 1

    return (i, j)


# make a sudo board
def sudo_maker(table, n):
    try:
        for i in range(n):
            x = random.randint(0, 8)
            y = random.randint(0, 8)
            table[x][y] = 0

        return table

    except:
        print("Use valid inputs")
