#!/usr/bin/env python
"""
Digging deeper in the device's manual, you discover the problem: this program is supposed to output another copy of the program! Unfortunately, the value in register A seems to have been corrupted. You'll need to find a new value to which you can initialize register A so that the program's output instructions produce an exact copy of the program itself.

For example:

Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0
This program outputs a copy of itself if register A is instead initialized to 117440. (The original initial value of register A, 2024, is ignored.)

What is the lowest positive initial value for register A that causes the program to output a copy of itself?
"""

def is_copy(r_a, r_b, r_c, ip, instructions, copy_of):
    #print(r_a, copy_of)
    output_index = 0
    while ip < len(instructions):
        op = instructions[ip+1]
        if op <=3:
            combo_op = op
        elif op == 4:
            combo_op = r_a
        elif op == 5:
            combo_op = r_b
        elif op == 6:
            combo_op = r_c
        
        match instructions[ip]:
            case 0: #adv
                r_a = int(r_a / (2 ** combo_op))
                ip += 2
            case 1: #bxl
                r_b = r_b ^ op
                ip += 2
            case 2: #bst
                r_b = combo_op & 7
                ip += 2
            case 3: #jnz
                if r_a != 0:
                    ip = op
                else:
                    ip += 2
            case 4: #bxc
                r_b = r_b ^ r_c
                ip += 2
            case 5: #out
                output = combo_op & 7
                if output_index >= len(copy_of) or copy_of[output_index] != output:
                    return False
                output_index += 1
                ip += 2
            case 6: #bdv
                r_b = int(r_a / (2 ** combo_op))
                ip += 2
            case 7: #cdv
                r_c = int(r_a / (2 ** combo_op))
                ip += 2

    return output_index == len(copy_of)


with open('input', 'r') as f:
    lines = f.read().splitlines()


r_a = int(lines[0].split(":")[1])
r_b = int(lines[1].split(":")[1])
r_c = int(lines[2].split(":")[1])
instructions = [int(i) for i in lines[4].split(":")[1].split(",")]

ip = 0


# Might not work for every program, but probably all valid program for aoc
# instructions 5 (0 3) is the only one altering the register a, which is being // 8 each round. 
# Hence each round's output is only altered by the three last bits.
# Test progressively starting at the end, save candidates that are working for this step with << 3

candidates = [0]
for index in range(len(instructions)):
    new_candidates = [] 
    copy_of = instructions[len(instructions) - index - 1:]
    for candidate in candidates:
        for i in range(8):
            if is_copy((candidate << 3) + i, r_b, r_c,0,instructions, copy_of):
                new_candidates += [(candidate << 3) + i]
    candidates = new_candidates


print(candidates[0])

