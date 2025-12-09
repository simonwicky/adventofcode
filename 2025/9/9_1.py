#!/usr/bin/env python

with open('input','r') as f:
    data = f.read().splitlines()

red_tiles = [(int(line.split(",")[0]),int(line.split(",")[1])) for line in data]

max_size = 0

for i in range(len(red_tiles)):
    for j in range(i+1,len(red_tiles)):
        rec_size = (abs(red_tiles[i][0] - red_tiles[j][0]) + 1) * (abs(red_tiles[i][1] - red_tiles[j][1]) + 1)
        if rec_size > max_size:
            max_size = rec_size

print(max_size)