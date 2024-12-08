#!/usr/bin/env python
"""
Watching over your shoulder as you work, one of The Historians asks if you took the effects of resonant harmonics into your calculations.

Whoops!

After updating your model, it turns out that an antinode occurs at any grid position exactly in line with at least two antennas of the same frequency, regardless of distance. This means that some of the new antinodes will occur at the position of each antenna (unless that antenna is the only one of its frequency).

So, these three T-frequency antennas now create many antinodes:

T....#....
...T......
.T....#...
.........#
..#.......
..........
...#......
..........
....#.....
..........
In fact, the three T-frequency antennas are all exactly in line with two antennas, so they are all also antinodes! This brings the total number of antinodes in the above example to 9.

The original example now has 34 antinodes, including the antinodes that appear on every antenna:

##....#....#
.#.#....0...
..#.#0....#.
..##...0....
....0....#..
.#...#A....#
...#..#.....
#....#.#....
..#.....A...
....#....A..
.#........#.
...#......##
Calculate the impact of the signal using this updated model. How many unique locations within the bounds of the map contain an antinode?
"""

def grid_get(grid, position):
    i,j = position[0], position[1]
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]):
        return ''
    return grid[i][j]

def get_antennas(grid):
    antennas = {}
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            frequency =  grid[i][j]
            if frequency != '.':
                antennas[frequency] = antennas.get(frequency,[]) + [(i,j)]
    return antennas


def get_anti_nodes(grid, antenna):
    anti_nodes = set()
    for a1 in antenna:
        for a2 in antenna:
            if a1 == a2:
                continue
            distance = ( a2[0] - a1[0], a2[1] - a1[1])

            #check every point until off-grid
            maybe_anti_node = a2
            while grid_get(grid, maybe_anti_node):
               anti_nodes.add(maybe_anti_node)
               maybe_anti_node = (maybe_anti_node[0] + distance[0], maybe_anti_node[1] + distance[1])

    return anti_nodes

            
    

with open('input','r') as f:
    grid = f.read().splitlines()



antennas = get_antennas(grid)
anti_nodes = set()
for antenna in antennas.values():
    anti_nodes.update(get_anti_nodes(grid, antenna))

print(len(anti_nodes))


# distance in L#62 might be reductible, i.e there might be an anti-nodes between two antennas, e.g. antenna at (1,3) and (3,5), antinode at (2,4)
# if it is, it needs to be divided by the GCD of the two components and code should check between the antennas