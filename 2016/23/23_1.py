#!/usr/bin/env python

with open('input','r') as f:
    data = [line.split() for line in f.read().splitlines()]


registers: dict[str, int] = {}
registers["a"] = 7
registers["b"] = 0
registers["c"] = 0
registers["d"] = 0


def inc(argument: str):
    if argument.isalpha():
        registers[argument] += 1

def dec(argument: str):
    if argument.isalpha():
        registers[argument] -= 1

def cpy(src: str, dst: str):
    if not dst.isalpha(): #invalid instruction
        return 
    if src.isalpha(): # a b
        registers[dst] = registers[src]
    else: # 0 a
        registers[dst] = int(src)

def jnz(argument: str, offset: str):
    argument_int = registers[argument] if argument.isalpha() else int(argument)
    offset_int = registers[offset] if offset.isalpha() else int(offset)
    if argument_int != 0:
        return offset_int - 1 # -1 for the increment that happens regardless
    
    return 0

def tgl(argument: str, current_idx: int):
    offset = registers[argument] if argument.isalpha() else int(argument)
    target = current_idx + offset
    if target >= 0 and target < len(data):
        if len(data[target]) == 3:
            # 2 arguments 
            data[target][0] = 'cpy' if data[target][0] == 'jnz' else 'jnz'
        else:
            data[target][0] = 'dec' if data[target][0] == 'inc' else 'inc'


idx = 0
while idx >= 0 and idx < len(data):
    instruction = data[idx]

    if instruction[0] == "inc":
        inc(instruction[1])
    elif instruction[0] == "dec":
        dec(instruction[1])
    elif instruction[0] == "cpy":
        cpy(instruction[1], instruction[2])
    elif instruction[0] == "jnz":
        idx += jnz(instruction[1], instruction[2])
    elif instruction[0] == 'tgl':
        tgl(instruction[1], idx)

    idx += 1

print(registers["a"])