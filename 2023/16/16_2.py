#!/usr/bin/env python	

"""
As you try to work out what might be wrong, the reindeer tugs on your shirt and leads you to a nearby control panel. There, a collection of buttons lets you align the contraption so that the beam enters from any edge tile and heading away from that edge. (You can choose either of two directions for the beam if it starts on a corner; for instance, if the beam starts in the bottom-right corner, it can start heading either left or upward.)

So, the beam could start on any tile in the top row (heading downward), any tile in the bottom row (heading upward), any tile in the leftmost column (heading right), or any tile in the rightmost column (heading left). To produce lava, you need to find the configuration that energizes as many tiles as possible.

In the above example, this can be achieved by starting the beam in the fourth tile from the left in the top row:

.|<2<\\....
|v-v\\^....
.v.v.|->>>
.v.v.v^.|.
.v.v.v^...
.v.v.v^..\
.v.v/2\\..
<-2-/vv|..
.|<<<2-|.\
.v//.|.v..
Using this configuration, 51 tiles are energized:

.#####....
.#.#.#....
.#.#.#####
.#.#.##...
.#.#.##...
.#.#.##...
.#.#####..
########..
.#######..
.#...#.#..
Find the initial beam configuration that energizes the largest number of tiles; how many tiles are energized in that configuration?
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


def nb_energized(grid, beam):
	energized = [beam]
	beams = [beam]

	while len(beams) > 0:
		beams = beam_step(grid, beams)
		beams = [beam for beam in beams if beam not in energized]
		for beam in beams:
			energized += [beam]
	return len(set([beam[0] for beam in energized]))




with open('input','r') as f:
	grid = f.read().splitlines()


maximum = 0
for i in range(len(grid)):
	print("i",i)
	#from the left
	start_beam = [(i,0),(0,1)]
	maximum = max (maximum, nb_energized(grid, start_beam))

	#from the right
	start_beam = [(i,len(grid[0]) - 1),(0,-1)]
	maximum = max (maximum, nb_energized(grid, start_beam))

for j in range(len(grid[0])):
	print("j",j)
	#from the top
	start_beam = [(0,j),(-1,0)]
	maximum = max (maximum, nb_energized(grid, start_beam))

	#from the bottom
	start_beam = [(0,len(grid) - 1),(1,0)]
	maximum = max (maximum, nb_energized(grid, start_beam))

print(maximum)

