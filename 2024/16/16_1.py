#!/usr/bin/env python
"""
It's time again for the Reindeer Olympics! This year, the big event is the Reindeer Maze, where the Reindeer compete for the lowest score.

You and The Historians arrive to search for the Chief right as the event is about to start. It wouldn't hurt to watch a little, right?

The Reindeer start on the Start Tile (marked S) facing East and need to reach the End Tile (marked E). They can move forward one tile at a time (increasing their score by 1 point), but never into a wall (#). They can also rotate clockwise or counterclockwise 90 degrees at a time (increasing their score by 1000 points).

To figure out the best place to sit, you start by grabbing a map (your puzzle input) from a nearby kiosk. For example:

###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############
There are many paths through this maze, but taking any of the best paths would incur a score of only 7036. This can be achieved by taking a total of 36 steps forward and turning 90 degrees a total of 7 times:


###############
#.......#....E#
#.#.###.#.###^#
#.....#.#...#^#
#.###.#####.#^#
#.#.#.......#^#
#.#.#####.###^#
#..>>>>>>>>v#^#
###^#.#####v#^#
#>>^#.....#v#^#
#^#.#.###.#v#^#
#^....#...#v#^#
#^###.#.#.#v#^#
#S..#.....#>>^#
###############
Here's a second example:

#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################
In this maze, the best paths cost 11048 points; following one such path would look like this:

#################
#...#...#...#..E#
#.#.#.#.#.#.#.#^#
#.#.#.#...#...#^#
#.#.#.#.###.#.#^#
#>>v#.#.#.....#^#
#^#v#.#.#.#####^#
#^#v..#.#.#>>>>^#
#^#v#####.#^###.#
#^#v#..>>>>^#...#
#^#v###^#####.###
#^#v#>>^#.....#.#
#^#v#^#####.###.#
#^#v#^........#.#
#^#v#^#########.#
#S#>>^..........#
#################
Note that the path shown above includes one 90 degree turn as the very first move, rotating the Reindeer from facing East to facing North.

Analyze your map carefully. What is the lowest score a Reindeer could possibly get?
"""
import math
DIRECTIONS = [(1,0),(0,1),(-1,0),(0,-1)]

class Position():
    def __init__(self, i,j):
        self.i = i
        self.j = j
        self.visited = False
        self.distances = {}
        for direction in DIRECTIONS:
            self.distances[direction] = math.inf 
    
    def min_distance(self):
        tmp = math.inf
        for direction in DIRECTIONS:
            if self.distances[direction] < tmp:
                tmp = self.distances[direction]
        return tmp  
   
    def min_distance_visited(self):
        if self.visited:
            return math.inf
        return self.min_distance()
    def key(self):
        return (self.i, self.j)

    def __repr__(self):
        return f"""({self.i},{self.j}) : {self.distances}"""

def grid_get(grid, i,j):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]):
        return ''
    return grid[i][j]


with open('input','r') as f:
    grid = f.read().splitlines()

labyrinth = {}
start = None
end = None
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == '.':
            labyrinth[(i,j)] = Position(i,j)
        if grid[i][j] == 'E':
            end = Position(i,j) 
            labyrinth[(i,j)] = end
        if grid[i][j] == 'S':
            start = Position(i,j)
            start.distances[DIRECTIONS[0]] = 1000
            start.distances[DIRECTIONS[1]] = 0
            start.distances[DIRECTIONS[2]] = 1000
            start.distances[DIRECTIONS[3]] = 1000
            labyrinth[(i,j)] = start


#Dijkstra
current = start
while current:
    for direction in DIRECTIONS:
        pos = labyrinth.get((current.i + direction[0], current.j + direction[1]), None)
        if pos:

            new_distance = current.distances[direction] + 1
            if new_distance < pos.distances[direction] :
                pos.distances[direction] = new_distance
            for other in DIRECTIONS:
                if other != direction and pos.distances[other] > pos.distances[direction] + 1000:
                    pos.distances[other] = pos.distances[direction] + 1000

    current.visited = True
    current = labyrinth.get(min(labyrinth.values(), key = lambda x : x.min_distance_visited()).key())
    if current.visited:
        current = None

print(end.min_distance())
