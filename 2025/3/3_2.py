#!/usr/bin/env python


# Find the max digit with enough space left at the end, isolate it, decrement the size and start again in the second part of the list
def find_max(data, size):
    def inner(data, size, acc):
        if size == 0:
            return acc

        # optional early return, we need to take everything left
        if len(data) == size: 
            return acc + ''.join([str(n) for n in data])

        # find the max, leaving at least size-1 number after it
        max_index = data.index(max(data[:len(data) - size + 1]))

        return inner(data[max_index + 1:], size - 1, acc +str(data[max_index]))
    return inner(data, size, "")





with open('input','r') as f:
    data = f.read().splitlines()

total = 0

for line in data:
    batteries = [int(i) for i in line]
    joltage = int(''.join([str(n) for n in find_max(batteries,12)]))
    total += joltage

print(total)