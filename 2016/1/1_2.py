#!/usr/bin/env python
"""
Then, you notice the instructions continue on the back of the Recruiting Document. Easter Bunny HQ is actually at the first location you visit twice.

For example, if your instructions are R8, R4, R4, R8, the first location you visit twice is 4 blocks away, due East.

How many blocks away is the first location you visit twice?

"""

DIRECTIONS = [(-1,0),(0,1),(1,0),(0,-1)]

with open("input",'r') as f:
    instructions = f.read().split(", ")

x,y = 0, 0
visited = set((0,0))
direction_idx = 0
for instruction in instructions:
    step = int(instruction[1:])
    match instruction[0]:
        case "R":
            direction_idx = (direction_idx + 1) % 4
        case "L":
            direction_idx = (direction_idx - 1) % 4
    for i in range(step):
        x += DIRECTIONS[direction_idx][0]
        y += DIRECTIONS[direction_idx][1]
        if (x,y) in visited:
            print(abs(x) + abs(y))
            exit(0)
        else:
            visited.add((x,y))