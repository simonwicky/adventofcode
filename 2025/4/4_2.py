#!/usr/bin/env python

"""Return the character at position i,j in grid, nothing if it's out of bounds"""
def grid_get(grid, i,j):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]):
        return ''
    return grid[i][j]

def forklift_accessible(grid, i, j):
    if grid_get(grid,i,j) != '@':
        return False
    adjacent = 0
    for x in [-1,0,1]:
        for y in [-1,0,1]:
            if x == 0 and y == 0:
                continue
            if grid_get(grid, i + x, j + y) == '@':
                adjacent += 1
    return adjacent < 4


def remove_paper(grid, coordinates_list):
    for coordinate in coordinates_list:
        grid[coordinate[0]][coordinate[1]] = '.'
    return grid

def removable_paper(grid):
    coordinates = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if forklift_accessible(grid,i,j):
                coordinates += [(i,j)]

    return coordinates
    



with open('input','r') as f:
    grid = f.read().splitlines()

# prepare the grid for modifications
for i in range(len(grid)):
    grid[i] = [n for n in grid[i]]

total = 0
to_remove = removable_paper(grid)
while len(to_remove) > 0:
    total += len(to_remove)
    grid = remove_paper(grid, to_remove)
    to_remove = removable_paper(grid)


print(total)