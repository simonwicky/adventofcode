#!/usr/bin/env python
"""
During the bathroom break, someone notices that these robots seem awfully similar to ones built and used at the North Pole. If they're the same type of robots, they should have a hard-coded Easter egg: very rarely, most of the robots should arrange themselves into a picture of a Christmas tree.

What is the fewest number of seconds that must elapse for the robots to display the Easter egg?
"""

tile_x = 101
tile_y = 103

def robot_position(robot, time):
    return ((robot[0][0] + time * robot[1][0]) % tile_x, (robot[0][1] + time * robot[1][1]) % tile_y)


robots = []
with open('input','r') as f:
    for line in f.read().splitlines():
        line = line.split(" ")
        position = [int(x) for x in line[0][2:].split(",")]
        velocity = [int(x) for x in line[1][2:].split(",")]
        robots += [(position, velocity)]



second = 0
flag = False
display = False #change to true to see the christmas tree
while not flag:
    second += 1
    positions = [['.'] * tile_x for _ in range(tile_y)]
    for robot in robots:
        pos = robot_position(robot, second)
        positions[pos[1]][pos[0]] = '1'


    for line in positions:
        if '1' * 10 in ''.join(line): #we're gonna say there is a christmas tree if 10 robots are right next to each other
            flag = True


    if flag and display:
        for line in positions:
            print(''.join(line))

print(second)
