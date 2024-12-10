#!/usr/bin/env python
"""
The reindeer spends a few minutes reviewing your hiking trail map before realizing something, disappearing for a few minutes, and finally returning with yet another slightly-charred piece of paper.

The paper describes a second way to measure a trailhead called its rating. A trailhead's rating is the number of distinct hiking trails which begin at that trailhead. For example:

.....0.
..4321.
..5..2.
..6543.
..7..4.
..8765.
..9....
The above map has a single trailhead; its rating is 3 because there are exactly three distinct hiking trails which begin at that position:

.....0.   .....0.   .....0.
..4321.   .....1.   .....1.
..5....   .....2.   .....2.
..6....   ..6543.   .....3.
..7....   ..7....   .....4.
..8....   ..8....   ..8765.
..9....   ..9....   ..9....
Here is a map containing a single trailhead with rating 13:

..90..9
...1.98
...2..7
6543456
765.987
876....
987....
This map contains a single trailhead with rating 227 (because there are 121 distinct hiking trails that lead to the 9 on the right edge and 106 that lead to the 9 on the bottom edge):

012345
123456
234567
345678
4.6789
56789.
Here's the larger example from before:

89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
Considering its trailheads in reading order, they have ratings of 20, 24, 10, 4, 1, 4, 5, 8, and 5. The sum of all trailhead ratings in this larger example topographic map is 81.

You're not sure how, but the reindeer seems to have crafted some tiny flags out of toothpicks and bits of paper and is using them to mark trailheads on your topographic map. What is the sum of the ratings of all trailheads?
"""


def grid_get(grid, position):
    i, j = position[0], position[1]
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]):
        return ''
    return int(grid[i][j])

#don't turn the list into sets, and now we can double count points
def trailhead_rating(grid,start_i,start_j):
    current_positions = [(start_i, start_j)]
    current_elevation = 0
    directions = [(-1, 0), (0, 1), (1, 0), (0 ,-1)]
    while current_elevation < 9:
        new_positions = []
        for position in current_positions:
            for direction in directions:
                new_position = (position[0] + direction[0], position[1] + direction[1])
                if grid_get(grid, new_position) == current_elevation + 1:
                    new_positions += [new_position]
        current_elevation += 1
        current_positions = new_positions
    return len(current_positions)
    





with open('input','r') as f:
    grid = f.read().splitlines()


total = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid_get(grid, (i,j)) == 0:
            total += trailhead_rating(grid, i, j)

print(total)