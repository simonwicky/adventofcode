#!/usr/bin/env python

def grid_get(grid : list[str], i : int,j : int) -> str:
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]):
        return ''
    return grid[i][j]

with open('input','r') as f:
    grid = f.read().splitlines()



tachyon_beams = [0] * len(grid[0])
tachyon_beams[grid[0].index('S')] = 1
new_tachyon_beams= [0] * len(grid[0])

for i in range(1,len(grid)):
    for j in range(len(grid[i])):
        if tachyon_beams[j] != 0:

            # If splitter underneath, add timeline to left and right
            if grid_get(grid, i+1, j) == '^':
                new_tachyon_beams[j-1] +=  tachyon_beams[j] # particular input doesn't require bound check
                new_tachyon_beams[j+1] +=  tachyon_beams[j]
            # If not, directly below
            else:
                new_tachyon_beams[j] +=  tachyon_beams[j]


    tachyon_beams = new_tachyon_beams
    new_tachyon_beams = [0] * len(grid[0])

print(sum(tachyon_beams))