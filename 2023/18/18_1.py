#!/usr/bin/env python

"""
However, they aren't sure the lagoon will be big enough; they've asked you to take a look at the dig plan (your puzzle input). For example:

R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)
The digger starts in a 1 meter cube hole in the ground. They then dig the specified number of meters up (U), down (D), left (L), or right (R), clearing full 1 meter cubes as they go. The directions are given as seen from above, so if "up" were north, then "right" would be east, and so on. Each trench is also listed with the color that the edge of the trench should be painted as an RGB hexadecimal color code.

When viewed from above, the above example dig plan would result in the following loop of trench (#) having been dug out from otherwise ground-level terrain (.):

#######
#.....#
###...#
..#...#
..#...#
###.###
#...#..
##..###
.#....#
.######
At this point, the trench could contain 38 cubic meters of lava. However, this is just the edge of the lagoon; the next step is to dig out the interior so that it is one meter deep as well:

#######
#######
#######
..#####
..#####
#######
#####..
#######
.######
.######
Now, the lagoon can contain a much more respectable 62 cubic meters of lava. While the interior is dug out, the edges are also painted according to the color codes in the dig plan.

The Elves are concerned the lagoon won't be large enough; if they follow their dig plan, how many cubic meters of lava could it hold?
"""

def dig(instructions):
	dug = { 0:[] }
	current = (0,0)
	for line in instructions:
		direction = line.split()[0]
		size = int(line.split()[1])
		if direction == 'R':
			dug[current[0]] += [current[1] + size]
			current = (current[0], current[1] + size)
		elif direction == 'L':
			dug[current[0]] += [current[1] - size]
			current = (current[0], current[1] - size)
		elif direction == 'D':
			for i in range(1,size+1):
				dug[current[0] + i] = dug.get(current[0] + i,[]) + [current[1]]
			current = (current[0] +  size, current[1])
		elif direction == 'U':
			for i in range(1,size+1):
				dug[current[0] - i] = dug.get(current[0] - i,[]) + [current[1]]
			current = (current[0] -  size, current[1])

	return dug


def area(lagoon):
	total = 0
	for line in sorted(lagoon.keys()):
		inside = False
		on_side = False
		prev_b = 0
		prev_b_dir = 0
		for b in sorted(lagoon[line]):
			if not inside and not on_side: #correct the off by ones
				total += 1
			curr_b_dir = 1 if b in lagoon.get(line + 1,[]) else -1
			if b in lagoon.get(line + 1,[]) and b in lagoon.get(line - 1,[]):
				if inside:
					total += b - prev_b
				inside = not inside
				prev_b = b

			elif not on_side:
				if inside:
					total += b - prev_b
				on_side = True
				prev_b = b
				prev_b_dir = 1 if b in lagoon.get(line + 1,[]) else -1

			elif on_side and (prev_b_dir == curr_b_dir): # leaving side, not crossing it
				on_side = False
				total += b - prev_b
				prev_b = b
			elif on_side and (prev_b_dir != curr_b_dir): # leaving side, crossing it
				on_side = False
				total += b - prev_b
				prev_b = b
				inside = not inside

	return total





with open('input','r') as f:
	lines = f.read().splitlines()


lagoon = dig(lines)
print(area(lagoon))
