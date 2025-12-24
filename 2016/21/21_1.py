#!/usr/bin/env python


def swap_position(input_str: list[str], x: int, y: int):
    input_str[x], input_str[y] = input_str[y], input_str[x]
    return input_str

def swap_letter(input_str: list[str], letter_x: str, letter_y: str):
    # We assume no duplicate letters and that it will be found
    idx_x = input_str.index(letter_x)
    idx_y = input_str.index(letter_y)
        
    return swap_position(input_str, idx_x, idx_y)

def rotate(input_str: list[str], direction: int, step: int):
    # right is -1, left is 1
    step = step % len(input_str) # Rotation of len(input_str) is equivalent to doing nothing
    return input_str[direction * step:] + input_str[:direction * step]

def rotate_pos(input_str: list[str], letter: str):
    idx = input_str.index(letter)
    if idx >= 4:
        return rotate(input_str, -1, idx + 2)
    return rotate(input_str, -1, idx + 1)

def reverse(input_str: list[str], x: int, y: int):
    # from the input, we assume x < y
    to_reverse = input_str[x:y+1]
    return input_str[:x]  + to_reverse[::-1]+ input_str[y+1:]

def move(input_str: list[str], src: int, dst: int):
    letter = input_str[src]
    del input_str[src]
    return input_str[:dst] + [letter] + input_str[dst:]


def scramble(instruction: str, input_str: list[str]):
    split_intstruction = instruction.split()
    if instruction.startswith("swap position"):
        return swap_position(input_str,int(split_intstruction[2]), int(split_intstruction[5]))
    elif instruction.startswith("swap letter"):
        return swap_letter(input_str,split_intstruction[2], split_intstruction[5])
    elif instruction.startswith("rotate left"):
        return rotate(input_str, 1, int(split_intstruction[2]))
    elif instruction.startswith("rotate right"):
        return rotate(input_str, -1, int(split_intstruction[2]))
    elif instruction.startswith("rotate based"):
        return rotate_pos(input_str, split_intstruction[6])
    elif instruction.startswith("reverse"):
        return reverse(input_str, int(split_intstruction[2]), int(split_intstruction[4]))
    elif instruction.startswith("move"):
        return move(input_str, int(split_intstruction[2]), int(split_intstruction[5]))
    
    # Unreachable according to instructions
    return [""]


with open('input','r') as f:
    data = f.read().splitlines()

input_str = 'egcdahbf'
input_str = [c for c in input_str]


for instruction in data:
    input_str = scramble(instruction, input_str)

print(''.join(input_str))

