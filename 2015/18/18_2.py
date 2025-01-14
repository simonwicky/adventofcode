#!/usr/bin/env python
"""
You flip the instructions over; Santa goes on to point out that this is all just an implementation of Conway's Game of Life. At least, it was, until you notice that something's wrong with the grid of lights you bought: four lights, one in each corner, are stuck on and can't be turned off. The example above will actually run like this:

Initial state:
##.#.#
...##.
#....#
..#...
#.#..#
####.#

After 1 step:
#.##.#
####.#
...##.
......
#...#.
#.####

After 2 steps:
#..#.#
#....#
.#.##.
...##.
.#..##
##.###

After 3 steps:
#...##
####.#
..##.#
......
##....
####.#

After 4 steps:
#.####
#....#
...#..
.##...
#.....
#.#..#

After 5 steps:
##.###
.##..#
.##...
.##...
#.#...
##...#
After 5 steps, this example now has 17 lights on.

In your grid of 100x100 lights, given your initial configuration, but with the four corners always in the on state, how many lights are on after 100 steps?
"""

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

    new_grid[0][0] = 1
    new_grid[0][99] = 1
    new_grid[0][0] = 1
    new_grid[99][99] = 1
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

start_grid[0][0] = 1
start_grid[0][99] = 1
start_grid[0][0] = 1
start_grid[99][99] = 1


for i in range(100):
    #print_grid(start_grid)
    #print()
    start_grid = step(start_grid)

total = 0
for i in start_grid:
    total += sum(i)
print(total)