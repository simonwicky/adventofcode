#!/usr/bin/env python

"""
Every year, Santa manages to deliver all of his presents in a single night.

This year, however, he has some new locations to visit; his elves have provided him the distances between every pair of locations. He can start and end at any two (different) locations he wants, but he must visit each location exactly once. What is the shortest distance he can travel to achieve this?

For example, given the following distances:

London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141
The possible routes are therefore:

Dublin -> London -> Belfast = 982
London -> Dublin -> Belfast = 605
London -> Belfast -> Dublin = 659
Dublin -> Belfast -> London = 659
Belfast -> Dublin -> London = 605
Belfast -> London -> Dublin = 982
The shortest of these is London -> Dublin -> Belfast = 605, and so the answer is 605 in this example.

What is the distance of the shortest route?
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

min_distance = 1e6
for route in itertools.permutations(locations, len(locations)):
    route_distance = 0
    for i in range(len(route) - 1):
        route_distance += distances[(route[i], route[i+1])]
    min_distance = min(min_distance, route_distance)

print(min_distance)