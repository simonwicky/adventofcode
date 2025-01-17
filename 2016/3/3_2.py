#!/usr/bin/env python
"""
Now that you've helpfully marked up their design documents, it occurs to you that triangles are specified in groups of three vertically. Each set of three numbers in a column specifies a triangle. Rows are unrelated.

For example, given the following specification, numbers with the same hundreds digit would be part of the same triangle:

101 301 501
102 302 502
103 303 503
201 401 601
202 402 602
203 403 603
In your puzzle input, and instead reading by columns, how many of the listed triangles are possible?
"""


with open('input','r') as f:
    data = f.read().splitlines()

possible = 0
for i in range(0,len(data),3):
    for k in range(3):
        sides = [int(data[i+j].split()[k]) for j in range(3)]
        if sum(sides) > 2 * max(sides):
            possible += 1
print(possible)