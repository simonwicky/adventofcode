#!/usr/bin/env python

"""
The researcher has collected a bunch of data and compiled the data into a single giant image (your puzzle input). The image includes empty space (.) and galaxies (#). For example:

...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
The researcher is trying to figure out the sum of the lengths of the shortest path between every pair of galaxies. However, there's a catch: the universe expanded in the time it took the light from those galaxies to reach the observatory.

Due to something involving gravitational effects, only some space expands. In fact, the result is that any rows or columns that contain no galaxies should all actually be twice as big.

In the above example, three columns and two rows contain no galaxies:

   v  v  v
 ...#......
 .......#..
 #.........
>..........<
 ......#...
 .#........
 .........#
>..........<
 .......#..
 #...#.....
   ^  ^  ^
These rows and columns need to be twice as big; the result of cosmic expansion therefore looks like this:

....#........
.........#...
#............
.............
.............
........#....
.#...........
............#
.............
.............
.........#...
#....#.......
Equipped with this expanded universe, the shortest path between every pair of galaxies can be found. It can help to assign every galaxy a unique number:

....1........
.........2...
3............
.............
.............
........4....
.5...........
............6
.............
.............
.........7...
8....9.......
In these 9 galaxies, there are 36 pairs. Only count each pair once; order within the pair doesn't matter. For each pair, find any shortest path between the two galaxies using only steps that move up, down, left, or right exactly one . or # at a time. (The shortest path between two galaxies is allowed to pass through another galaxy.)

For example, here is one of the shortest paths between galaxies 5 and 9:

....1........
.........2...
3............
.............
.............
........4....
.5...........
.##.........6
..##.........
...##........
....##...7...
8....9.......
This path has length 9 because it takes a minimum of nine steps to get from galaxy 5 to galaxy 9 (the eight locations marked # plus the step onto galaxy 9 itself). Here are some other example shortest path lengths:

Between galaxy 1 and galaxy 7: 15
Between galaxy 3 and galaxy 6: 17
Between galaxy 8 and galaxy 9: 5
In this example, after expanding the universe, the sum of the shortest path between all 36 pairs of galaxies is 374.

Expand the universe, then find the length of the shortest path between every pair of galaxies. What is the sum of these lengths?
"""

def expand_universe(universe, galaxies):
	lines = [i for i in range(len(universe)) if '#' not in universe[i]]
	rows = [j for j in range(len(universe[0])) if '#' not in [universe[i][j] for i in range(len(universe))]]

	line_offset = [len([l for l in lines if l < i]) for i in range(len(universe))]
	row_offset = [len([r for r in rows if r < j]) for j in range(len(universe[0]))]

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