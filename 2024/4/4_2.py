#!/usr/bin/env python

"""
The Elf looks quizzically at you. Did you misunderstand the assignment?

Looking for the instructions, you flip over the word search to find that this isn't actually an XMAS puzzle; it's an X-MAS puzzle in which you're supposed to find two MAS in the shape of an X. One way to achieve that is like this:

M.S
.A.
M.S
Irrelevant characters have again been replaced with . in the above diagram. Within the X, each MAS can be written forwards or backwards.

Here's the same example from before, but this time all of the X-MASes have been kept instead:

.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........
In this example, an X-MAS appears 9 times.

Flip the word search from the instructions back over to the word search side and try again. How many times does an X-MAS appear?

"""


def grid_get(grid, i,j):
	if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]):
		return ''
	return grid[i][j]

def find_xmas(grid, i,j):
    if grid_get(grid, i,j) != 'A': 
        return False
	
    top_l = grid_get(grid,i-1,j-1)
    top_r = grid_get(grid,i-1,j+1)
    bot_l = grid_get(grid,i+1,j-1)
    bot_r = grid_get(grid,i+1,j+1)
	
    #Diagonals must be one M and one S, whatever way 
    if sorted(top_l + bot_r) == ['M','S'] and sorted(top_r + bot_l) == ['M','S']:
        return True
    return False


with open('input','r') as f:
	grid = f.read().splitlines()

dimensions = (len(grid),len(grid[0]))

total = 0

for i in range(dimensions[0]):
	for j in range(dimensions[1]):
		if find_xmas(grid,i,j):
			total += 1


print(total)