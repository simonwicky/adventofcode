#!/usr/bin/env python

"""
After the million lights incident, the fire code has gotten stricter: now, at most ten thousand lights are allowed. You arrange them in a 100x100 grid.

Never one to let you down, Santa again mails you instructions on the ideal lighting configuration. With so few lights, he says, you'll have to resort to animation.

Start by setting your lights to the included initial configuration (your puzzle input). A # means "on", and a . means "off".

Then, animate your grid in steps, where each step decides the next configuration based on the current one. Each light's next state (either on or off) depends on its current state and the current states of the eight lights adjacent to it (including diagonals). Lights on the edge of the grid might have fewer than eight neighbors; the missing ones always count as "off".

For example, in a simplified 6x6 grid, the light marked A has the neighbors numbered 1 through 8, and the light marked B, which is on an edge, only has the neighbors marked 1 through 5:

1B5...
234...
......
..123.
..8A4.
..765.
The state a light should have next is based on its current state (on or off) plus the number of neighbors that are on:

A light which is on stays on when 2 or 3 neighbors are on, and turns off otherwise.
A light which is off turns on if exactly 3 neighbors are on, and stays off otherwise.
All of the lights update simultaneously; they all consider the same current state before moving to the next.

Here's a few steps from an example configuration of another 6x6 grid:

Initial state:
.#.#.#
...##.
#....#
..#...
#.#..#
####..

After 1 step:
..##..
..##.#
...##.
......
#.....
#.##..

After 2 steps:
..###.
......
..###.
......
.#....
.#....

After 3 steps:
...#..
......
...#..
..##..
......
......

After 4 steps:
......
......
..##..
..##..
......
......
After 4 steps, this example has four lights on.

In your grid of 100x100 lights, given your initial configuration, how many lights are on after 100 steps?
"""
#Basically a game of life

def grid_get(grid, i,j):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]):
        return 0
    return grid[i][j]


def step(grid):
    new_grid = []
    for i in range(len(grid)):
        new_row = []
        for j in range(len(grid[i])):
            neighbors = sum(grid_get(grid, i + dx, j +dy) for dx in [-1,0,1] for dy in [-1,0,1]) - grid_get(grid, i, j)
            if grid_get(grid, i, j) == 1:
                if neighbors == 2 or neighbors == 3:
                    new_row += [1]
                else:
                    new_row += [0]
            else:
                if neighbors == 3:
                    new_row += [1]
                else:
                    new_row += [0]
        new_grid += [new_row]
    return new_grid
                    

def print_grid(grid):
    for i in grid:
        for j in i:
            if j:
                print("#", end='')
            else:
                print(".", end='')
        print()


with open('input','r') as f:
    grid = f.read().splitlines()

start_grid = []
for i in grid:
    row = []
    for j in i:
        if j == '#':
            row += [1]
        else:
            row += [0]
    start_grid += [row]


for i in range(100):
    #print_grid(start_grid)
    #print()
    start_grid = step(start_grid)

total = 0
for i in start_grid:
    total += sum(i)
print(total)