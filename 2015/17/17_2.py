#!/usr/bin/env python

"""
While playing with all the containers in the kitchen, another load of eggnog arrives! The shipping and receiving department is requesting as many containers as you can spare.

Find the minimum number of containers that can exactly fit all 150 liters of eggnog. How many different ways can you fill that number of containers and still hold exactly 150 litres?

In the example above, the minimum number of containers was two. There were three ways to use that many containers, and so the answer there would be 3.
"""

from itertools import *

#from itertools doc
def powerset(iterable):
    "Subsequences of the iterable from shortest to longest."
    # powerset([1,2,3]) → () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


with open('input','r') as f:
	containers = [int(line) for line in f.read().splitlines()]

nb_ways = [0] * len(containers)
for s in powerset(containers):
	if sum(s) == 150:
		nb_ways[len(s)] += 1

print([x for x in nb_ways if x != 0][0])
