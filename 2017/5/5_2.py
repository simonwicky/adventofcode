#!/usr/bin/env python

with open('input','r') as f:
    data = f.read().splitlines()

instructions = [int(d) for d in data]


step = 0
pointer = 0
while pointer >= 0 and pointer < len(instructions):
    jump = instructions[pointer]
    if jump >= 3:
        instructions[pointer] -= 1
    else:
        instructions[pointer] += 1

    pointer = pointer + jump
    step += 1

print(step)