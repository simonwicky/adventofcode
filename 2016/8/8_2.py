#!/usr/bin/env python
"""
You notice that the screen is only capable of displaying capital letters; in the font it uses, each letter is 5 pixels wide and 6 tall.

After you swipe your card, what code is the screen trying to display?
"""

def print_screen(screen):
    for i in screen:
        for j in i:
            if j:
                print("#",end="")
            else:
                print(" ", end="")
        print()

def rotate_row(screen, row_index, amount):
    new_row = [0] * screen_w
    for i in range(screen_w):
        new_row[(i + amount) % screen_w] = screen[row_index][i]
    screen[row_index] = new_row
    return screen

def rotate_col(screen, col_index, amount):
    col = [screen[i][col_index] for i in range(screen_h)]
    for i in range(screen_h):
        screen[(i + amount) % screen_h][col_index] = col[i]

    return screen

def rect(screen, rect_w, rect_h):
    for i in range(rect_h):
        for j in range(rect_w):
            screen[i][j] = 1
    return screen

with open('input','r') as f:
    data = f.read().splitlines()

screen_w = 50
screen_h = 6

screen = [[0] * screen_w for _ in range(screen_h)]

for instruction in data:
    instruction = instruction.split(" ")
    if instruction[0] == "rect":
        w = int(instruction[1].split("x")[0])
        h = int(instruction[1].split("x")[1])
        screen = rect(screen, w, h)
    else:
        index = int(instruction[2].split("=")[1])
        amount = int(instruction[4])
        if instruction[1] == 'row':
            screen = rotate_row(screen, index, amount)
        elif instruction[1] == 'column':
            screen = rotate_col(screen, index, amount)
    



print_screen(screen)
#EOARGPHYAO in my case