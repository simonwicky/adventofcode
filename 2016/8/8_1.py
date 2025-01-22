#!/usr/bin/env python
"""
You come across a door implementing what you can only assume is an implementation of two-factor authentication after a long game of requirements telephone.

To get past the door, you first swipe a keycard (no problem; there was one on a nearby desk). Then, it displays a code on a little screen, and you type that code on a keypad. Then, presumably, the door unlocks.

Unfortunately, the screen has been smashed. After a few minutes, you've taken everything apart and figured out how it works. Now you just have to work out what the screen would have displayed.

The magnetic strip on the card you swiped encodes a series of instructions for the screen; these instructions are your puzzle input. The screen is 50 pixels wide and 6 pixels tall, all of which start off, and is capable of three somewhat peculiar operations:

rect AxB turns on all of the pixels in a rectangle at the top-left of the screen which is A wide and B tall.
rotate row y=A by B shifts all of the pixels in row A (0 is the top row) right by B pixels. Pixels that would fall off the right end appear at the left end of the row.
rotate column x=A by B shifts all of the pixels in column A (0 is the left column) down by B pixels. Pixels that would fall off the bottom appear at the top of the column.
For example, here is a simple sequence on a smaller screen:

rect 3x2 creates a small rectangle in the top-left corner:

###....
###....
.......
rotate column x=1 by 1 rotates the second column down by one pixel:

#.#....
###....
.#.....
rotate row y=0 by 4 rotates the top row right by four pixels:

....#.#
###....
.#.....
rotate column x=1 by 1 again rotates the second column down by one pixel, causing the bottom pixel to wrap back to the top:

.#..#.#
#.#....
.#.....
As you can see, this display technology is extremely powerful, and will soon dominate the tiny-code-displaying-screen market. That's what the advertisement on the back of the display tries to convince you, anyway.

There seems to be an intermediate check of the voltage used by the display: after you swipe your card, if the screen did work, how many pixels should be lit?
"""

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
    



print(sum([sum(i) for i in screen]))