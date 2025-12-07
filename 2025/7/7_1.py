#!/usr/bin/env python

def grid_get(grid : list[str], i : int,j : int) -> str:
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]):
        return ''
    return grid[i][j]

with open('input','r') as f:
    grid = f.read().splitlines()


tachyon_beams = set([grid[0].index('S')])
split = 0
new_tachyon_beams: set[int] = set()


for i in range(1,len(grid)):
    for beam in tachyon_beams:
        if grid_get(grid, i, beam) == '^':
            split += 1
            new_tachyon_beams.add(beam - 1) # particular input doesn't require bound check
            new_tachyon_beams.add(beam + 1)
        else:
            new_tachyon_beams.add(beam)

    tachyon_beams = new_tachyon_beams
    new_tachyon_beams = set()

print(split)