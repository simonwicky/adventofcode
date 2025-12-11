#!/usr/bin/env python

with open('input','r') as f:
    data = f.read()

total = 0
for i in range(len(data)):
    if data[i] == data[(i + len(data) // 2) % len(data)]:
        total += int(data[i])

print(total)