#!/usr/bin/env python


# Modified 2025 day 5 part 2

with open('input','r') as f:
    data = f.read().splitlines()


"""Given range_a and range_b, return range_b' such that range_a U range_b = range_a U range_b', but interestion(range_a, range_b') is null"""
def reduce(range_a: tuple[int,int], range_b: tuple[int,int]):
    # disjoint
    if range_b[0] > range_a[1] or range_b[1] < range_a[0]:
        return [range_b]

    new_ranges: list[tuple[int, int]] = []
    if range_b[0] < range_a[0]:
        new_ranges += [(range_b[0],range_a[0]-1)]

    if range_b[1] > range_a[1]:
        new_ranges += [(range_a[1]+1,range_b[1])]

    return new_ranges

blocked_ips: list[tuple[int, int]] = []

for line in data:
    lower_bound = line.split("-")[0]
    upper_bound = line.split("-")[1]
    blocked_ips += [(int(lower_bound), int(upper_bound))]

disjoint_ips: list[tuple[int, int]] = []

# Take the first range, reduce the rest with it and add it to disjoints_ids
while len(blocked_ips) > 0:
    current_ips: tuple[int, int] = blocked_ips[0]
    pending_ips = blocked_ips[1:]
    new_fresh_ips: list[tuple[int, int]] = []
    for ips in pending_ips:
        new_fresh_ips += reduce(current_ips, ips)

    disjoint_ips += [current_ips]
    blocked_ips = new_fresh_ips

# We now know every range is disjoint so we can just count them
# we want allowd address so it's just an inversion
total = 0
for ips in disjoint_ips:
    total += ips[1]- ips[0] + 1

print(2 ** 32 - total)