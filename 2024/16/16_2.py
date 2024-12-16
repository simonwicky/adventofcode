#!/usr/bin/env python
"""
Now that you know what the best paths look like, you can figure out the best spot to sit.

Every non-wall tile (S, ., or E) is equipped with places to sit along the edges of the tile. While determining which of these tiles would be the best spot to sit depends on a whole bunch of factors (how comfortable the seats are, how far away the bathrooms are, whether there's a pillar blocking your view, etc.), the most important factor is whether the tile is on one of the best paths through the maze. If you sit somewhere else, you'd miss all the action!

So, you'll need to determine which tiles are part of any best path through the maze, including the S and E tiles.

In the first example, there are 45 tiles (marked O) that are part of at least one of the various best paths through the maze:

###############
#.......#....O#
#.#.###.#.###O#
#.....#.#...#O#
#.###.#####.#O#
#.#.#.......#O#
#.#.#####.###O#
#..OOOOOOOOO#O#
###O#O#####O#O#
#OOO#O....#O#O#
#O#O#O###.#O#O#
#OOOOO#...#O#O#
#O###.#.#.#O#O#
#O..#.....#OOO#
###############
In the second example, there are 64 tiles that are part of at least one of the best paths:

#################
#...#...#...#..O#
#.#.#.#.#.#.#.#O#
#.#.#.#...#...#O#
#.#.#.#.###.#.#O#
#OOO#.#.#.....#O#
#O#O#.#.#.#####O#
#O#O..#.#.#OOOOO#
#O#O#####.#O###O#
#O#O#..OOOOO#OOO#
#O#O###O#####O###
#O#O#OOO#..OOO#.#
#O#O#O#####O###.#
#O#O#OOOOOOO..#.#
#O#O#O#########.#
#O#OOO..........#
#################
Analyze your map further. How many tiles are part of at least one of the best paths through the maze?
"""
import math
DIRECTIONS = [(1,0),(0,1),(-1,0),(0,-1)]

class Position():
    def __init__(self, i,j):
        self.i = i
        self.j = j
        self.visited = False
        self.distances = {}
        self.previous = {}
        for direction in DIRECTIONS:
            self.distances[direction] = math.inf
            self.previous[direction] = []
    
    def min_distance(self):
        tmp = math.inf
        for direction in DIRECTIONS:
            if self.distances[direction] < tmp:
                tmp = self.distances[direction]
        return tmp
    
    def min_direction(self):
        tmp = math.inf
        tmp_dir = []
        for direction in DIRECTIONS:
            if self.distances[direction] <= tmp:
                tmp = self.distances[direction]
                tmp_dir += [direction]
        return tmp_dir

     
    def min_distance_visited(self):
        if self.visited:
            return math.inf
        return self.min_distance()
    def key(self):
        return (self.i, self.j)

    def __repr__(self):
        return f"""({self.i},{self.j}) : {self.distances} : {self.previous}"""

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
                pos.previous[direction] = [direction]
            elif new_distance == pos.distances[direction]:
                pos.previous[direction] += [direction]
            for other in DIRECTIONS:
                if other != direction and pos.distances[other] > pos.distances[direction] + 1000:
                    pos.distances[other] = pos.distances[direction] + 1000
                    pos.previous[other] = [direction]
                elif other != direction and pos.distances[other] == pos.distances[direction] + 1000:
                    pos.previous[other] += [direction]


    current.visited = True
    current = labyrinth.get(min(labyrinth.values(), key = lambda x : x.min_distance_visited()).key())
    if current.visited:
        current = None



on_shortest_path = set()
to_visit = [(end, end.min_direction()[0])]
while len(to_visit) > 0:
    current, direction = to_visit.pop()
    for d in current.previous[direction]:
        node_key = (current.i - d[0], current.j - d[1])
        if node_key not in on_shortest_path:
            to_visit += [(labyrinth[node_key],d)]
    on_shortest_path.add(current.key())



print(len(on_shortest_path))
