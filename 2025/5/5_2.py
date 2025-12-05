#!/usr/bin/env python

with open('input','r') as f:
    data = f.read().splitlines()


"""Given range_a and range_b, return range_b' such that range_a U range_b = range_a U range_b', but interestion(range_a, range_b') is null"""
def reduce(range_a, range_b):
    # disjoint
    if range_b[0] > range_a[1] or range_b[1] < range_a[0]:
        return [range_b]

    new_ranges = []
    if range_b[0] < range_a[0]:
        new_ranges += [(range_b[0],range_a[0]-1)]

    if range_b[1] > range_a[1]:
        new_ranges += [(range_a[1]+1,range_b[1])]

    return new_ranges

fresh_ids = []

i = 0
while data[i] != '':
    lower_bound = data[i].split("-")[0]
    upper_bound = data[i].split("-")[1]
    fresh_ids += [(int(lower_bound), int(upper_bound))]
    i += 1

disjoint_ids = []

# Take the first range, reduce the rest with it and add it to disjoints_ids
while len(fresh_ids) > 0:
    current_ids = fresh_ids[0]
    pending_ids = fresh_ids[1:]
    new_fresh_ids = []
    for ids in pending_ids:
        new_fresh_ids += reduce(current_ids, ids)

    disjoint_ids += [current_ids]
    fresh_ids = new_fresh_ids

# We now know every range is disjoint so we can just count them
total = 0
for ids in disjoint_ids:
    total += ids[1]- ids[0] + 1

print(total)