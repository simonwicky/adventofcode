#!/usr/bin/env python

with open('input','r') as f:
    data = f.read().splitlines()

instructions = [int(d) for d in data]


step = 0
pointer = 0
while pointer >= 0 and pointer < len(instructions):
    next_pointer = pointer + instructions[pointer]
    instructions[pointer] += 1

    pointer = next_pointer
    step += 1

print(step)