#!/usr/bin/env python

"""
"Looks like the Chief's not here. Next!" One of The Historians pulls out a device and pushes the only button on it. After a brief flash, you recognize the interior of the Ceres monitoring station!

As the search for the Chief continues, a small Elf who lives on the station tugs on your shirt; she'd like to know if you could help her with her word search (your puzzle input). She only has to find one word: XMAS.

This word search allows words to be horizontal, vertical, diagonal, written backwards, or even overlapping other words. It's a little unusual, though, as you don't merely need to find one instance of XMAS - you need to find all of them. Here are a few ways XMAS might appear, where irrelevant characters have been replaced with .:

..X...
.SAMX.
.A..A.
XMAS.S
.X....
The actual word search will be full of letters instead. For example:

MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
In this word search, XMAS occurs a total of 18 times; here's the same word search again, but where letters not involved in any XMAS have been replaced with .:

....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX
Take a look at the little Elf's word search. How many times does XMAS appear?
"""

def grid_get(grid, i,j):
	if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]):
		return ''
	return grid[i][j]

def find_xmas(grid, i,j, direction):
    xmas = 'XMAS'
    for idx in range(len(xmas)):
        new_i = i + idx * direction[0]
        new_j = j + idx * direction[1]
        if grid_get(grid,new_i,new_j) != xmas[idx]:
            return False
    return True

directions = [(i,j) for i in [-1,0,1] for j in [-1,0,1] if i != 0 or j != 0]

with open('input','r') as f:
    grid = f.read().splitlines()

dimensions = (len(grid),len(grid[0]))

total = 0

for i in range(dimensions[0]):
    for j in range(dimensions[1]):
        for direction in directions:
            if find_xmas(grid,i,j,direction):
                total += 1
print(total)

    
	