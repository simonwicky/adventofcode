#!/usr/bin/env python

"""Return the character at position i,j in grid, nothing if it's out of bounds"""
def grid_get(grid, i,j):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]):
        return ''
    return grid[i][j]

def forklift_accessible(grid, i, j):
    adjacent = 0
    for x in [-1,0,1]:
        for y in [-1,0,1]:
            if x == 0 and y == 0:
                continue
            if grid_get(grid, i + x, j + y) == '@':
                adjacent += 1
    return adjacent < 4
    


with open('input','r') as f:
    grid = f.read().splitlines()


total = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid_get(grid,i,j) == '@' and forklift_accessible(grid,i,j):
            total += 1

print(total)