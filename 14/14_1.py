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

def load_column(col):
	standings = []
	current_stop = -1
	current_count = 0
	for i,rock in enumerate(col):
		if rock == '#':
			if current_count > 0:
				standings += [(current_stop, current_count)]
			current_stop = i
			current_count = 0
		if rock == 'O':
			current_count += 1
	if current_count > 0:
		standings += [(current_stop, current_count)]
	
	load = 0
	for state in standings:
		start_rock = len(col) - (state[0] + 1)
		end_rock = start_rock - state[1]
		load += sum(range(start_rock, end_rock,-1))

	return load
	





with open('input','r') as f:
	lines = f.read().splitlines()


total = 0

for j in range(len(lines[0])):
	total += load_column(''.join([lines[i][j] for i in range(len(lines))]))
print(total)
