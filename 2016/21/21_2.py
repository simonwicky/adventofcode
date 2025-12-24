#!/usr/bin/env python


# identical as part 1
def un_swap_position(input_str: list[str], x: int, y: int):
    input_str[x], input_str[y] = input_str[y], input_str[x]
    return input_str

# identical as part 1
def un_swap_letter(input_str: list[str], letter_x: str, letter_y: str):
    # We assume no duplicate letters and that it will be found
    idx_x = input_str.index(letter_x)
    idx_y = input_str.index(letter_y)
        
    return un_swap_position(input_str, idx_x, idx_y)

# Inverting direction
def un_rotate(input_str: list[str], direction: int, step: int):
    # right is -1, left is 1, to reverse the operation, rotate the other way
    step = step % len(input_str) # Rotation of len(input_str) is equivalent to doing nothing
    return input_str[direction * step:] + input_str[:direction * step]

# a.......  => .a...... 1
# .a......  => ...a.... 2
# ..a.....  => .....a.. 3
# ...a....  => .......a 4
# ....a...  => ..a..... 6
# .....a..  => ....a... 7
# ......a.  => ......a. 8
# .......a  => a....... 9
# How the rotate_pos based on a looks, reverse that
def un_rotate_pos(input_str: list[str], letter: str):
    idx = input_str.index(letter)
    mapping = [9,1,6,2,7,3,8,4]
    return un_rotate(input_str, 1, mapping[idx])

# identical in reverse
def un_reverse(input_str: list[str], x: int, y: int):
    # from the input, we assume x < y
    to_reverse = input_str[x:y+1]
    return input_str[:x]  + to_reverse[::-1]+ input_str[y+1:]

# invert src and dst
def un_move(input_str: list[str], src: int, dst: int):
    letter = input_str[dst]
    del input_str[dst]
    return input_str[:src] + [letter] + input_str[src:]


def un_scramble(instruction: str, input_str: list[str]):
    split_intstruction = instruction.split()
    if instruction.startswith("swap position"):
        return un_swap_position(input_str,int(split_intstruction[2]), int(split_intstruction[5]))
    elif instruction.startswith("swap letter"):
        return un_swap_letter(input_str,split_intstruction[2], split_intstruction[5])
    elif instruction.startswith("rotate left"):
        return un_rotate(input_str, -1, int(split_intstruction[2]))
    elif instruction.startswith("rotate right"):
        return un_rotate(input_str, 1, int(split_intstruction[2]))
    elif instruction.startswith("rotate based"):
        return un_rotate_pos(input_str, split_intstruction[6])
    elif instruction.startswith("reverse"):
        return un_reverse(input_str, int(split_intstruction[2]), int(split_intstruction[4]))
    elif instruction.startswith("move"):
        return un_move(input_str, int(split_intstruction[2]), int(split_intstruction[5]))
    
    # Unreachable according to instructions
    return [""]


with open('input','r') as f:
    data = f.read().splitlines()

input_str = 'fbgdceah'
input_str = [c for c in input_str]


for instruction in data[::-1]:
    print(instruction)
    print(input_str)
    input_str = un_scramble(instruction, input_str)
    print(input_str)
    print()

print(''.join(input_str))
