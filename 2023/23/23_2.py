#!/usr/bin/env python

"""
As you reach the trailhead, you realize that the ground isn't as slippery as you expected; you'll have no problem climbing up the steep slopes.

Now, treat all slopes as if they were normal paths (.). You still want to make sure you have the most scenic hike possible, so continue to ensure that you never step onto the same tile twice. What is the longest hike you can take?

In the example above, this increases the longest hike to 154 steps:

#S#####################
#OOOOOOO#########OOO###
#######O#########O#O###
###OOOOO#.>OOO###O#O###
###O#####.#O#O###O#O###
###O>...#.#O#OOOOO#OOO#
###O###.#.#O#########O#
###OOO#.#.#OOOOOOO#OOO#
#####O#.#.#######O#O###
#OOOOO#.#.#OOOOOOO#OOO#
#O#####.#.#O#########O#
#O#OOO#...#OOO###...>O#
#O#O#O#######O###.###O#
#OOO#O>.#...>O>.#.###O#
#####O#.#.###O#.#.###O#
#OOOOO#...#OOO#.#.#OOO#
#O#########O###.#.#O###
#OOO###OOO#OOO#...#O###
###O###O#O###O#####O###
#OOO#OOO#O#OOO>.#.>O###
#O###O###O#O###.#.#O###
#OOOOO###OOO###...#OOO#
#####################O#
Find the longest hike you can take through the surprisingly dry hiking trails listed on your map. How many steps long is the longest hike?
"""

class Path():
	def __init__(self,pos, end_point, length = 0,visited = []):
		self.pos = pos
		self.len = length
		self.visited = visited
		self.end_point = end_point

	def step(self,grid):
		if self.pos == end_point:
			return [self]
		new_paths = []
		for s in [1,-1,1j,-1j]:
			new_pos = self.pos + s
			if new_pos not in self.visited:
				if grid[new_pos] != '#':
					new_paths += [Path(new_pos, self.end_point, self.len + 1, self.visited + [new_pos])]
		if len(new_paths) == 1:
			return new_paths[0].step(grid)
		return new_paths


def step_paths(paths, grid):
	new_paths = []
	for path in paths:
		for new_path in path.step(grid):
			new_paths += [new_path]
			#if new_path.pos in new_paths:
			#	new_paths[new_path.pos] = new_path if new_path.len > new_paths[new_path.pos].len else new_paths[new_path.pos]
			#else:
			#	new_paths[new_path.pos] = new_path



	return new_paths



with open('input','r') as f:
	lines = f.read().splitlines()


grid = {i + j * 1j : lines[i][j] for i in range(len(lines)) for j in range(len(lines[i]))}

start_point = [pos for pos in grid if grid[pos] == '.' and pos.real == 0.0][0]
end_point = [pos for pos in grid if grid[pos] == '.' and pos.real == len(lines) -1][0]


paths = [Path(start_point + 1, end_point, length = 1, visited = [start_point, start_point + 1], )]

res = 0
while len(paths) > 0:
	new_paths = step_paths(paths, grid)
	for new_path in new_paths:
		if new_path.pos == end_point:
			res = max(new_path.len,res)
	print(new_paths[0].len)
	

	paths = [path for path in new_paths if path.pos != end_point]

print(res)


#5274 is too low