#!/usr/bin/env python

"""
The programs seem perplexed by your list of cheats. Apparently, the two-picosecond cheating rule was deprecated several milliseconds ago! The latest version of the cheating rule permits a single cheat that instead lasts at most 20 picoseconds.

Now, in addition to all the cheats that were possible in just two picoseconds, many more cheats are possible. This six-picosecond cheat saves 76 picoseconds:

###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#1#####.#.#.###
#2#####.#.#...#
#3#####.#.###.#
#456.E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
Because this cheat has the same start and end positions as the one above, it's the same cheat, even though the path taken during the cheat is different:

###############
#...#...#.....#
#.#.#.#.#.###.#
#S12..#.#.#...#
###3###.#.#.###
###4###.#.#...#
###5###.#.###.#
###6.E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
Cheats don't need to use all 20 picoseconds; cheats can last any amount of time up to and including 20 picoseconds (but can still only end when the program is on normal track). Any cheat time not used is lost; it can't be saved for another cheat later.

You'll still need a list of the best cheats, but now there are even more to choose between. Here are the quantities of cheats in this example that save 50 picoseconds or more:

There are 32 cheats that save 50 picoseconds.
There are 31 cheats that save 52 picoseconds.
There are 29 cheats that save 54 picoseconds.
There are 39 cheats that save 56 picoseconds.
There are 25 cheats that save 58 picoseconds.
There are 23 cheats that save 60 picoseconds.
There are 20 cheats that save 62 picoseconds.
There are 19 cheats that save 64 picoseconds.
There are 12 cheats that save 66 picoseconds.
There are 14 cheats that save 68 picoseconds.
There are 12 cheats that save 70 picoseconds.
There are 22 cheats that save 72 picoseconds.
There are 4 cheats that save 74 picoseconds.
There are 3 cheats that save 76 picoseconds.
Find the best cheats using the updated cheating rules. How many cheats would save you at least 100 picoseconds?
"""


import math
DIRECTIONS = [(1,0),(0,1),(-1,0),(0,-1)]

class Position():
    def __init__(self, i,j):
        self.i = i
        self.j = j
        self.visited = False
        self.distance = math.inf
     
    def distance_visited(self):
        if self.visited:
            return math.inf
        return self.distance
    
    def key(self):
        return (self.i, self.j)

    def __repr__(self):
        return f"""({self.i},{self.j}) : {self.distance}"""



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
            start.distance = 0
            labyrinth[(i,j)] = start


#Dijkstra
current = start
while current:
    for direction in DIRECTIONS:
        pos = labyrinth.get((current.i + direction[0], current.j + direction[1]), None)
        if pos:
            new_distance = current.distance + 1
            if new_distance < pos.distance :
                pos.distance = new_distance


    current.visited = True
    current = labyrinth.get(min(labyrinth.values(), key = lambda x : x.distance_visited()).key())
    if current.visited:
        current = None

max_cheat_time = 20
min_gain_time = 100


moves = set()
for d in range(2,max_cheat_time + 1):
    for i in range(d + 1):
        j = d - i
        moves.update([(i,j), (i,-j),(-i,j),(-i,-j)])


total = 0
current = start
while current != end:
    for d1 in DIRECTIONS:
        pos = labyrinth.get((current.i + d1[0], current.j + d1[1]), None)
        if pos and pos.distance == current.distance + 1:
            next_current = pos #might not work if multiple path possible

    for m in moves:
        cheat_to = labyrinth.get((current.i + m[0], current.j + m[1]), None)
        if cheat_to and cheat_to.distance >= current.distance + abs(m[0]) + abs(m[1]) + min_gain_time:
            total += 1
    current = next_current
    


print(total)
