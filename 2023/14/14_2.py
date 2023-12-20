#!/usr/bin/env python

"""
Upon closer inspection, the individual mirrors each appear to be connected via an elaborate system of ropes and pulleys to a large metal platform below the dish. The platform is covered in large rocks of various shapes. Depending on their position, the weight of the rocks deforms the platform, and the shape of the platform controls which ropes move and ultimately the focus of the dish.

In short: if you move the rocks, you can focus the dish. The platform even has a control panel on the side that lets you tilt it in one of four directions! The rounded rocks (O) will roll when the platform is tilted, while the cube-shaped rocks (#) will stay in place. You note the positions of all of the empty spaces (.) and rocks (your puzzle input). For example:

O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
Start by tilting the lever so all of the rocks will slide north as far as they will go:

OOOO.#.O..
OO..#....#
OO..O##..O
O..#.OO...
........#.
..#....#.#
..O..#.O.O
..O.......
#....###..
#....#....
You notice that the support beams along the north side of the platform are damaged; to ensure the platform doesn't collapse, you should calculate the total load on the north support beams.

The amount of load caused by a single rounded rock (O) is equal to the number of rows from the rock to the south edge of the platform, including the row the rock is on. (Cube-shaped rocks (#) don't contribute to load.) So, the amount of load caused by each rock in each row is as follows:

OOOO.#.O.. 10
OO..#....#  9
OO..O##..O  8
O..#.OO...  7
........#.  6
..#....#.#  5
..O..#.O.O  4
..O.......  3
#....###..  2
#....#....  1
The total load is the sum of the load caused by all of the rounded rocks. In this example, the total load is 136.

Tilt the platform so that the rounded rocks all roll north. Afterward, what is the total load on the north support beams?
"""

def tilt(col,direction = 1):
	standings = []
	current_stop = -1 if direction == 1 else len(col)
	current_count = 0
	for i,rock in list(enumerate(col))[::direction]:
		if rock == '#':
			standings += [(current_stop, current_count)]
			current_stop = i
			current_count = 0
		if rock == 'O':
			current_count += 1

	standings += [(current_stop, current_count)]
	new_col = ['.'] * len(col)
	for state in standings:
		if 0 <= state[0] < len(col):
			new_col[state[0]] = '#'

		start = state[0] + direction
		end = state[0] + (1 + state[1]) * direction
		if state[1] != 0:
			if end == -1:
				new_col[start::direction] = ['O'] * state[1]
			else:
				new_col[start:end:direction] = ['O'] * state[1]


	return ''.join(new_col)

def load_column(col):
	load = 0
	for i in range(len(col)):
		if col[len(col)-i-1] == 'O':
			load += i + 1

	return load

def transpose(pattern):
	cols = []
	for j in range(len(pattern[0])):

		cols += [''.join([pattern[i][j] for i in range(len(pattern))])]
	return cols


with open('input','r') as f:
	pattern = f.read().splitlines()



#There is probably a cycle somewhere
previous_patterns = []
i = 0
while pattern not in previous_patterns:
	previous_patterns += [pattern]

	#Tilt North
	pattern = transpose(pattern)
	pattern = [tilt(line) for line in pattern]

	#tilt west
	pattern = transpose(pattern)
	pattern = [tilt(line) for line in pattern]

	#tilt south
	pattern = transpose(pattern)
	pattern = [tilt(line, direction = -1) for line in pattern]

	#tilt east
	pattern = transpose(pattern)
	pattern = [tilt(line, direction = -1) for line in pattern]
	i += 1
	



cycle_len = i - previous_patterns.index(pattern)
cycle_start = previous_patterns.index(pattern)


cycle_pos = (1000000000 - cycle_start) % cycle_len
end_pattern = previous_patterns[cycle_start + cycle_pos]


print(sum([load_column(col) for col in transpose(end_pattern)]))

