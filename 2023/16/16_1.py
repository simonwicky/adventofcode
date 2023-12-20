#!/usr/bin/env python	

"""
Upon closer inspection, the contraption appears to be a flat, two-dimensional square grid containing empty space (.), mirrors (/ and \\), and splitters (| and -).

The contraption is aligned so that most of the beam bounces around the grid, but each tile on the grid converts some of the beam's light into heat to melt the rock in the cavern.

You note the layout of the contraption (your puzzle input). For example:

.|...\\....
|.-.\\.....
.....|-...
........|.
..........
.........\
..../.\\\\..
.-.-/..|..
.|....-|.\
..//.|....
The beam enters in the top-left corner from the left and heading to the right. Then, its behavior depends on what it encounters as it moves:

If the beam encounters empty space (.), it continues in the same direction.
If the beam encounters a mirror (/ or \\), the beam is reflected 90 degrees depending on the angle of the mirror. For instance, a rightward-moving beam that encounters a / mirror would continue upward in the mirror's column, while a rightward-moving beam that encounters a \\ mirror would continue downward from the mirror's column.
If the beam encounters the pointy end of a splitter (| or -), the beam passes through the splitter as if the splitter were empty space. For instance, a rightward-moving beam that encounters a - splitter would continue in the same direction.
If the beam encounters the flat side of a splitter (| or -), the beam is split into two beams going in each of the two directions the splitter's pointy ends are pointing. For instance, a rightward-moving beam that encounters a | splitter would split into two beams: one that continues upward from the splitter's column and one that continues downward from the splitter's column.
Beams do not interact with other beams; a tile can have many beams passing through it at the same time. A tile is energized if that tile has at least one beam pass through it, reflect in it, or split in it.

In the above example, here is how the beam of light bounces around the contraption:

>|<<<\\....
|v-.\\^....
.v...|->>>
.v...v^.|.
.v...v^...
.v...v^..\
.v../2\\\\..
<->-/vv|..
.|<<<2-|.\
.v//.|.v..
Beams are only shown on empty tiles; arrows indicate the direction of the beams. If a tile contains beams moving in multiple directions, the number of distinct directions is shown instead. Here is the same diagram but instead only showing whether a tile is energized (#) or not (.):

######....
.#...#....
.#...#####
.#...##...
.#...##...
.#...##...
.#..####..
########..
.#######..
.#...#.#..
Ultimately, in this example, 46 tiles become energized.

The light isn't energizing enough tiles to produce lava; to debug the contraption, you need to start by analyzing the current situation. With the beam starting in the top-left heading right, how many tiles end up being energized?
"""

def beam_step(grid, beams):
	
	new_beams = []
	for beam in beams:
		cur_i = beam[0][0]
		cur_j = beam[0][1]
		if beam[1] == (0,1): #to the right
			if grid[cur_i][cur_j] == '|':
				new_beams += [[(cur_i - 1,cur_j),(-1,0)]]
				new_beams += [[(cur_i + 1,cur_j),(1,0)]]
			elif grid[cur_i][cur_j] == '\\':
				new_beams += [[(cur_i + 1,cur_j),(1,0)]]
			elif grid[cur_i][cur_j] == '/':
				new_beams += [[(cur_i - 1,cur_j),(-1,0)]]
			else:
				new_beams += [[(cur_i,cur_j + 1),(0,1)]]

		elif beam[1] == (0,-1): #to the left
			if grid[cur_i][cur_j] == '|':
				new_beams += [[(cur_i - 1,cur_j),(-1,0)]]
				new_beams += [[(cur_i + 1,cur_j),(1,0)]]
			elif grid[cur_i][cur_j] == '\\':
				new_beams += [[(cur_i - 1,cur_j),(-1,0)]]
			elif grid[cur_i][cur_j] == '/':
				new_beams += [[(cur_i + 1,cur_j),(1,0)]]
			else:
				new_beams += [[(cur_i,cur_j - 1),(0,-1)]]

		elif beam[1] == (1,0): #to the bottom
			if grid[cur_i][cur_j] == '-':
				new_beams += [[(cur_i, cur_j + 1),(0,1)]]
				new_beams += [[(cur_i, cur_j - 1),(0,-1)]]
			elif grid[cur_i][cur_j] == '\\':
				new_beams += [[(cur_i, cur_j + 1),(0,1)]]
			elif grid[cur_i][cur_j] == '/':
				new_beams += [[(cur_i, cur_j - 1),(0,-1)]]
			else:
				new_beams += [[(cur_i + 1,cur_j),(1,0)]]


		elif beam[1] == (-1,0): #to the top
			if grid[cur_i][cur_j] == '-':
				new_beams += [[(cur_i, cur_j + 1),(0,1)]]
				new_beams += [[(cur_i, cur_j - 1),(0,-1)]]
			elif grid[cur_i][cur_j] == '\\':
				new_beams += [[(cur_i, cur_j - 1),(0,-1)]]
			elif grid[cur_i][cur_j] == '/':
				new_beams += [[(cur_i, cur_j + 1),(0,1)]]
			else:
				new_beams += [[(cur_i - 1,cur_j),(-1,0)]]



	i_bound = len(grid)
	j_bound = len(grid[0])
	return [beam for beam in new_beams if (beam[0][0] >= 0 and beam[0][0] < i_bound and beam[0][1] >= 0 and beam[0][1] < j_bound)]






with open('input','r') as f:
	grid = f.read().splitlines()


energized = [[(0,0),(0,1)]]

beams = [[(0,0),(0,1)]]
while len(beams) > 0:
	beams = beam_step(grid, beams)
	beams = [beam for beam in beams if beam not in energized]
	for beam in beams:
		energized += [beam]

print(len(set([beam[0] for beam in energized])))

