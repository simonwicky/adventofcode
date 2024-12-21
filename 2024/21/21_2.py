#!/usr/bin/env python
"""
Just as the missing Historian is released, The Historians realize that a second member of their search party has also been missing this entire time!

A quick life-form scan reveals the Historian is also trapped in a locked area of the ship. Due to a variety of hazards, robots are once again dispatched, forming another chain of remote control keypads managing robotic-arm-wielding robots.

This time, many more robots are involved. In summary, there are the following keypads:

One directional keypad that you are using.
25 directional keypads that robots are using.
One numeric keypad (on a door) that a robot is using.
The keypads form a chain, just like before: your directional keypad controls a robot which is typing on a directional keypad which controls a robot which is typing on a directional keypad... and so on, ending with the robot which is typing on the numeric keypad.

The door codes are the same this time around; only the number of robots and directional keypads has changed.

Find the fewest number of button presses you'll need to perform in order to cause the robot in front of the door to type each code. What is the sum of the complexities of the five codes on your list?
"""
from functools import cache

def shortest_path(key1, key2, keypad):
    key_sequence = ''
    x_move, y_move = keypad[key2][0] - keypad[key1][0], keypad[key2][1] - keypad[key1][1]

    x_symbol = 'v' if x_move > 0 else '^'
    key_sequence += x_symbol * abs(x_move)
    y_symbol = '>' if y_move > 0 else '<'
    key_sequence += y_symbol * abs(y_move)
    
    result = []
    if (keypad[key1][0] + x_move, keypad[key1][1]) != keypad['void']:
        result += [key_sequence]
    if (keypad[key1][0], keypad[key1][1] + y_move) != keypad['void']:
        if key_sequence[::-1] != key_sequence:
            result += [key_sequence[::-1]]

    return result

def shortest_path_code(code, keypad):
    code = 'A' + code
    res = []
    for i in range(1,len(code)):
        res += [[sp + 'A' for sp in shortest_path(code[i-1], code[i], keypad)]]
    return res

        
with open('input','r') as f:
    codes = f.read().splitlines()

num_keypad = {'7' : (0,0),
              '8' : (0,1),
              '9' : (0,2),
              '4' : (1,0),
              '5' : (1,1),
              '6' : (1,2),
              '1' : (2,0),
              '2' : (2,1),
              '3' : (2,2),
              '0' : (3,1),
              'A' : (3,2),
              'void' : (3,0)}

dir_keypad = {'^' : (0,1),
              'A' : (0,2),
              '<' : (1,0),
              'v' : (1,1),
              '>' : (1,2),
              'void' : (0,0)}


@cache
def solve(code, nb_times):
    if nb_times == 0:
        return len(code)
    
    if any(c in code for c in "012345679"):
        keypad = num_keypad
    else:
        keypad = dir_keypad

    res = 0
    for shortest_paths in shortest_path_code(code, keypad):
        res += min(solve(sp, nb_times - 1) for sp in shortest_paths)
    return res
        
complexity = 0
for code in codes:
    lmin = solve(code, 1 + 25)
    complexity += lmin * int(code[:-1])

print(complexity)
