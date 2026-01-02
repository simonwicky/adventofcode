#!/usr/bin/env python

with open('input','r') as f:
    data = f.read()

# If it is at the bottom, is will only appear once
for line in data.splitlines():
    if data.count(line.split()[0]) == 1:
        print(line.split()[0])
