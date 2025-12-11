#!/usr/bin/env python

with open('input','r') as f:
    data = f.read().splitlines()

total = 0
for line in data:
    line = [int(n) for n in line.split()]
    total += max(line) - min(line)

print(total)