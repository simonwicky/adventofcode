#!/usr/bin/env python

"""
The next year, just to show off, Santa decides to take the route with the longest distance instead.

He can still start and end at any two (different) locations he wants, and he still must visit each location exactly once.

For example, given the distances above, the longest route would be 982 via (for example) Dublin -> London -> Belfast.

What is the distance of the longest route?
"""


#Traveling salesman problem
import itertools

with open('input','r') as f:
    data = f.read().splitlines()

distances = {}
locations = set()

for line in data:
    line_split = line.split(" ")
    l1 = line_split[0]
    l2 = line_split[2]
    d = int(line_split[4])
    locations.update((l1,l2))
    distances[(l1,l2)] = d
    distances[(l2,l1)] = d

max_distance = 0
for route in itertools.permutations(locations, len(locations)):
    route_distance = 0
    for i in range(len(route) - 1):
        route_distance += distances[(route[i], route[i+1])]
    max_distance = max(max_distance, route_distance)

print(max_distance)