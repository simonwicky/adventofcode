#!/usr/bin/env python
"""
Scanning the area, you discover that the entire field you're standing on is densely packed with pipes; it was hard to tell at first because they're the same metallic silver color as the "ground". You make a quick sketch of all of the surface pipes you can see (your puzzle input).

The pipes are arranged in a two-dimensional grid of tiles:

| is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east.
J is a 90-degree bend connecting north and west.
7 is a 90-degree bend connecting south and west.
F is a 90-degree bend connecting south and east.
. is ground; there is no pipe in this tile.
S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
Based on the acoustics of the animal's scurrying, you're confident the pipe that contains the animal is one large, continuous loop.

For example, here is a square loop of pipe:

.....
.F-7.
.|.|.
.L-J.
.....
If the animal had entered this loop in the northwest corner, the sketch would instead look like this:

.....
.S-7.
.|.|.
.L-J.
.....
In the above diagram, the S tile is still a 90-degree F bend: you can tell because of how the adjacent pipes connect to it.

Unfortunately, there are also many pipes that aren't connected to the loop! This sketch shows the same loop as above:

-L|F7
7S-7|
L|7||
-L-J|
L|-JF
In the above diagram, you can still figure out which pipes form the main loop: they're the ones connected to S, pipes those pipes connect to, pipes those pipes connect to, and so on. Every pipe in the main loop connects to its two neighbors (including S, which will have exactly two pipes connecting to it, and which is assumed to connect back to those two pipes).

Here is a sketch that contains a slightly more complex main loop:

..F7.
.FJ|.
SJ.L7
|F--J
LJ...
Here's the same example sketch with the extra, non-main-loop pipe tiles also shown:

7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ
If you want to get out ahead of the animal, you should find the tile in the loop that is farthest from the starting position. Because the animal is in the pipe, it doesn't make sense to measure this by direct distance. Instead, you need to find the tile that would take the longest number of steps along the loop to reach from the starting point - regardless of which way around the loop the animal went.

In the first example with the square loop:

.....
.S-7.
.|.|.
.L-J.
.....
You can count the distance each tile in the loop is from the starting point like this:

.....
.012.
.1.3.
.234.
.....
In this example, the farthest point from the start is 4 steps away.

Here's the more complex loop again:

..F7.
.FJ|.
SJ.L7
|F--J
LJ...
Here are the distances for each tile on that loop:

..45.
.236.
01.78
14567
23...
Find the single giant loop starting at S. How many steps along the loop does it take to get from the starting position to the point farthest from the starting position?
"""


def next_pipe(pipes, i, j, prev_i, prev_j):
	if pipes[i][j] == 'S':
		if pipes[i-1][j] in 'F|7':
			return (i-1,j)
		if pipes[i][j+1] in 'J-7':
			return (i,j+1)
		if pipes[i+1][j] in 'L|J':
			return (i+1,j)
		if pipes[i][j-1] in 'L-F':
			return (i,j-1)

	if ((pipes[i][j] == 'F' and prev_i == i + 1) or
		(pipes[i][j] == '-' and prev_j == j - 1) or
		(pipes[i][j] == 'L' and prev_i == i - 1)):
		return (i, j + 1)

	if ((pipes[i][j] == '7' and prev_i == i + 1) or
		(pipes[i][j] == '-' and prev_j == j + 1) or
		(pipes[i][j] == 'J' and prev_i == i - 1)):
		return (i, j - 1)

	if ((pipes[i][j] == '7' and prev_j == j - 1) or
		(pipes[i][j] == '|' and prev_i == i - 1) or
		(pipes[i][j] == 'F' and prev_j == j + 1)):
		return (i + 1, j)

	if ((pipes[i][j] == 'L' and prev_j == j + 1) or
		(pipes[i][j] == '|' and prev_i == i + 1) or
		(pipes[i][j] == 'J' and prev_j == j - 1)):
		return (i - 1, j)

	#this should never happen	
	return (-1,-1)


with open('input','r') as f:
	ground_map = f.read().splitlines()

#adding dots around the map so we can disregard bound problems
ground_map = ['.' * len(ground_map[0])] + ground_map + ['.' * len(ground_map[0])]
ground_map = ['.' + line + '.' for line in ground_map]


for i in range(len(ground_map)):
	if 'S' in ground_map[i]:
		start_point = (i, ground_map[i].index('S'))


previous_position = start_point
current_position = next_pipe(ground_map, *start_point, -1, -1)

step = 1
while current_position != start_point:
	new_position = next_pipe(ground_map, *current_position, *previous_position)

	previous_position = current_position
	current_position = new_position
	step += 1


print(step // 2)



