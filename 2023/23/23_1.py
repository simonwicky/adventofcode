#!/usr/bin/env python

"""
The Elves resume water filtering operations! Clean water starts flowing over the edge of Island Island.

They offer to help you go over the edge of Island Island, too! Just hold on tight to one end of this impossibly long rope and they'll lower you down a safe distance from the massive waterfall you just created.

As you finally reach Snow Island, you see that the water isn't really reaching the ground: it's being absorbed by the air itself. It looks like you'll finally have a little downtime while the moisture builds up to snow-producing levels. Snow Island is pretty scenic, even without any snow; why not take a walk?

There's a map of nearby hiking trails (your puzzle input) that indicates paths (.), forest (#), and steep slopes (^, >, v, and <).

For example:

#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#
You're currently on the single path tile in the top row; your goal is to reach the single path tile in the bottom row. Because of all the mist from the waterfall, the slopes are probably quite icy; if you step onto a slope tile, your next step must be downhill (in the direction the arrow is pointing). To make sure you have the most scenic hike possible, never step onto the same tile twice. What is the longest hike you can take?

In the example above, the longest hike you can take is marked with O, and your starting position is marked S:

#S#####################
#OOOOOOO#########...###
#######O#########.#.###
###OOOOO#OOO>.###.#.###
###O#####O#O#.###.#.###
###OOOOO#O#O#.....#...#
###v###O#O#O#########.#
###...#O#O#OOOOOOO#...#
#####.#O#O#######O#.###
#.....#O#O#OOOOOOO#...#
#.#####O#O#O#########v#
#.#...#OOO#OOO###OOOOO#
#.#.#v#######O###O###O#
#...#.>.#...>OOO#O###O#
#####v#.#.###v#O#O###O#
#.....#...#...#O#O#OOO#
#.#########.###O#O#O###
#...###...#...#OOO#O###
###.###.#.###v#####O###
#...#...#.#.>.>.#.>O###
#.###.###.#.###.#.#O###
#.....###...###...#OOO#
#####################O#
This hike contains 94 steps. (The other possible hikes you could have taken were 90, 86, 82, 82, and 74 steps long.)

Find the longest hike you can take through the hiking trails listed on your map. How many steps long is the longest hike?
"""

class Path():
	def __init__(self,pos, length = 0,visited = []):
		self.pos = pos
		self.len = length
		self.visited = visited

	def step(self,grid):
		new_paths = []
		for s in [1,-1,1j,-1j]:
			new_pos = self.pos + s
			if new_pos not in self.visited:
				if grid[new_pos] == '.':
					new_paths += [Path(new_pos, self.len + 1, self.visited + [new_pos])]

				elif grid[new_pos] == '^' and s != 1 and new_pos -1 not in self.visited:
					new_paths += [Path(new_pos -1, self.len + 2, self.visited + [new_pos, new_pos -1])]

				elif grid[new_pos] == 'v' and s != -1 and new_pos +1 not in self.visited:
					new_paths += [Path(new_pos  +1, self.len + 2, self.visited + [new_pos, new_pos +1])]

				elif grid[new_pos] == '<' and s != 1j and new_pos - 1j not in self.visited:
					new_paths += [Path(new_pos -1j, self.len + 2, self.visited + [new_pos, new_pos -1j])]

				elif grid[new_pos] == '>' and s != -1j and new_pos + 1j not in self.visited:
					new_paths += [Path(new_pos +1j, self.len + 2, self.visited + [new_pos, new_pos +1j])]


		return new_paths


def step_paths(paths, grid):
	new_paths = []
	for path in paths:
		new_paths += path.step(grid)

	return new_paths



with open('input','r') as f:
	lines = f.read().splitlines()


grid = {i + j * 1j : lines[i][j] for i in range(len(lines)) for j in range(len(lines[i]))}

start_point = [pos for pos in grid if grid[pos] == '.' and pos.real == 0.0][0]
end_point = [pos for pos in grid if grid[pos] == '.' and pos.real == len(lines) -1][0]


paths = [Path(start_point + 1, length = 1, visited = [start_point])]

res = 0
while len(paths) > 0:
	new_paths = step_paths(paths, grid)
	for new_path in new_paths:
		if new_path.pos == end_point:
			res = new_path.len

	paths = [path for path in new_paths if path.pos != end_point]

print(res)


