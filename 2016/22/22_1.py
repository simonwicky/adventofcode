#!/usr/bin/env python

with open('input','r') as f:
    data = f.read().splitlines()

disks: list[tuple[int, int]] = []
for line in data[2:]:
    split_line = line.split()
    disks += [(int(split_line[2][:-1]), int(split_line[3][:-1]))]

total = 0
for i in range(len(disks)):
    for j in range(len(disks)):
        if i == j:
            continue
        if disks[i][0] != 0 and disks[i][0] < disks[j][1]:
            total += 1

print(total)