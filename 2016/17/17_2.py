#!/usr/bin/env python

import hashlib

def valid_position(position: tuple[int, int, str], direction: tuple[int, int, str]) -> bool:
    new_x = position[0] + direction[0]
    new_y = position[1] + direction[1]

    return new_x >= 0 and new_x < 4 and new_y >= 0 and new_y < 4

def next_positions(position: tuple[int, int, str], password: str):
    DIRECTION: list[tuple[int, int, str]] = [(-1,0,'U'), (1,0,'D'), (0, -1, 'L'), (0, 1, 'R')]

    doors = hashlib.md5((password + position[2]).encode()).hexdigest()[:4]

    new_positions: list[tuple[int, int, str]] = []
    for i in range(4):
        if doors[i] in 'bcdef' and valid_position(position, DIRECTION[i]):
            new_positions += [(position[0] + DIRECTION[i][0], position[1] + DIRECTION[i][1], position[2] + DIRECTION[i][2])]

    return new_positions
            

with open('input','r') as f:
    password = f.read()


positions = [(0,0,'')]

target = (3,3)
longest_path = 0

while len(positions) > 0:
    # Take a step
    new_positions: list[tuple[int, int, str]] = []
    for p in positions:
        new_positions += next_positions(p, password)
    positions = new_positions

    # Prune path that are on the target
    new_positions: list[tuple[int, int, str]] = []
    for p in positions:
        if p[:2] == target:
            longest_path = max(longest_path, len(p[2]))
        else:
            new_positions += [p]
    positions = new_positions

print(longest_path)