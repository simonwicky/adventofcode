#!/usr/bin/env python

with open('input','r') as f:
    data = f.read().splitlines()

total = 0

for line in data:
    batteries = [int(i) for i in line]

    max_index = batteries.index(max(batteries))
    
    if max_index == len(batteries) - 1:
    # If the maximum is only the last one, it's the unit and the tens is the max in the start of the list
        total += 10 * max(batteries[:-1]) + batteries[-1]
    else:
        # If in the middle, it's the tens and units is the maximum in the rest of the list
        total += 10 * batteries[max_index] + max(batteries[max_index+1:])

print(total)