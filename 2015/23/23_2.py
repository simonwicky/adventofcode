#!/usr/bin/env python
"""
The unknown benefactor is very thankful for releasi-- er, helping little Jane Marie with her computer. Definitely not to distract you, what is the value in register b after the program is finished executing if register a starts as 1 instead?
"""
def execute(instruction, reg, ip):
    op = instruction.split(" ")[0]
    match op:
        case "hlf":
            r_res = instruction.split(" ")[1]
            reg[r_res] //= 2 
            ip += 1
        case "tpl":
            r_res = instruction.split(" ")[1]
            reg[r_res] *= 3 
            ip += 1
        case "inc":
            r_res = instruction.split(" ")[1]
            reg[r_res] += 1 
            ip += 1
        case "jmp":
            offset = int(instruction.split(" ")[1])
            ip += offset
        case "jie":
            r_res = instruction.split(" ")[1][:-1]
            offset = int(instruction.split(" ")[2])
            if reg[r_res] % 2 == 0:
                ip += offset
            else:
                ip += 1
        case "jio":
            r_res = instruction.split(" ")[1][:-1]
            offset = int(instruction.split(" ")[2])
            if reg[r_res] == 1: #TRY TO READ CORRECTLY NEXT TIME
                ip += offset
            else:
                ip += 1
    return reg, ip

with open('input', 'r') as f:
    instructions = f.read().splitlines()

ip = 0
reg = {"a" : 1, "b" : 0 }
while ip < len(instructions):
    reg, ip = execute(instructions[ip], reg, ip)

print(reg["b"])
