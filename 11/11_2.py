#!/usr/bin/env python

"""
The galaxies are much older (and thus much farther apart) than the researcher initially estimated.

Now, instead of the expansion you did before, make each empty row or column one million times larger. That is, each empty row should be replaced with 1000000 empty rows, and each empty column should be replaced with 1000000 empty columns.

(In the example above, if each empty row or column were merely 10 times larger, the sum of the shortest paths between every pair of galaxies would be 1030. If each empty row or column were merely 100 times larger, the sum of the shortest paths between every pair of galaxies would be 8410. However, your universe will need to expand far beyond these values.)

Starting with the same initial image, expand the universe according to these new rules, then find the length of the shortest path between every pair of galaxies. What is the sum of these lengths?
"""

def expand_universe(universe, galaxies):
	lines = [i for i in range(len(universe)) if '#' not in universe[i]]
	rows = [j for j in range(len(universe[0])) if '#' not in [universe[i][j] for i in range(len(universe))]]

	line_offset = [(1_000_000 - 1) * len([l for l in lines if l < i]) for i in range(len(universe))]
	row_offset = [(1_000_000 - 1) * len([r for r in rows if r < j]) for j in range(len(universe[0]))]

	return [(galaxy[0] + line_offset[galaxy[0]], galaxy[1] + row_offset[galaxy[1]]) for galaxy in galaxies]
	

def find_galaxies(universe):
	return [(i,j)  for i in range(len(universe)) for j in range(len(universe[i])) if universe[i][j] == '#']


def shortest_path(galaxy_a, galaxy_b):
	return abs(galaxy_b[0] - galaxy_a[0]) + abs(galaxy_b[1] - galaxy_a[1])





with open('input','r') as f:
	universe = f.read().splitlines()

galaxies = find_galaxies(universe)
new_galaxies = expand_universe(universe, galaxies)
total = 0
for a in range(len(new_galaxies)):
	for b in range(a+1,len(new_galaxies)):
		total += shortest_path(new_galaxies[a], new_galaxies[b])

print(total)