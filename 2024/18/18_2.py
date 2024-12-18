#!/usr/bin/env python

"""
The Historians aren't as used to moving around in this pixelated universe as you are. You're afraid they're not going to be fast enough to make it to the exit before the path is completely blocked.

To determine how fast everyone needs to go, you need to determine the first byte that will cut off the path to the exit.

In the above example, after the byte at 1,1 falls, there is still a path to the exit:

O..#OOO
O##OO#O
O#OO#OO
OOO#OO#
###OO##
.##O###
#.#OOOO
However, after adding the very next byte (at 6,1), there is no longer a path to the exit:

...#...
.##..##
.#..#..
...#..#
###..##
.##.###
#.#....
So, in this example, the coordinates of the first byte that prevents the exit from being reachable are 6,1.

Simulate more of the bytes that are about to corrupt your memory space. What are the coordinates of the first byte that will prevent the exit from being reachable from your starting position? (Provide the answer as two integers separated by a comma with no other characters.)
"""

x_max = 71
y_max = 71

DIRECTIONS = [(1,0),(0,1),(-1,0),(0,-1)]

def is_corrupted(position, corrupted):
    x = position[0]
    y = position[1]
    if x < 0 or x >= x_max or y < 0 or y >= y_max or [x,y] in corrupted:
        return True
    return False

def exit_reachable(corrupted):
    start = (0,0)
    end = (x_max - 1, y_max - 1)

    current = start
    to_visit = [start]
    visited = set()
    distance = 0
    while end not in to_visit and len(to_visit) != 0:
        new_to_visit = set()
        for current in to_visit:
            for d in DIRECTIONS:
                pos = (current[0] + d[0], current[1] + d[1])
                if not is_corrupted(pos, corrupted) and pos not in visited:
                    new_to_visit.add(pos)
            visited.add(current)
        distance += 1
        to_visit = new_to_visit

    if len(to_visit) == 0:
        return False

    return True
    

with open('input','r') as f:
    lines = f.read().splitlines()

corrupted = []
for i in range(len(lines)):
    corrupted += [[int(x) for x in lines[i].split(",")]]


index = len(corrupted)
while not exit_reachable(corrupted[:index]):
    index -= 1

print(f"{corrupted[index][0]},{corrupted[index][1]}")