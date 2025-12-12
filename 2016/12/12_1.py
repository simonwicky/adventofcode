#!/usr/bin/env python

with open('input','r') as f:
    data = f.read().splitlines()


registers = {}
registers["a"] = 0
registers["b"] = 0
registers["c"] = 0
registers["d"] = 0


idx = 0
while idx >= 0 and idx < len(data):
    instruction = data[idx].split()

    if instruction[0] == "inc":
        registers[instruction[1]] += 1
    elif instruction[0] == "dec":
         registers[instruction[1]] -= 1
    elif instruction[0] == "cpy":
        if instruction[1].isalpha():
            registers[instruction[2]] = registers[instruction[1]]
        else:
            registers[instruction[2]] = int(instruction[1])
    elif instruction[0] == "jnz":
        if instruction[1].isalpha():
            if registers[instruction[1]] != 0:
                idx += int(instruction[2]) - 1 # -1 for the increment that happens regardless
        else:
            if int(instruction[1]) != 0:
                idx += int(instruction[2]) - 1 # -1 for the increment that happens regardless

    idx += 1

print(registers["a"])