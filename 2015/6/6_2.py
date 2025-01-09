#!/usr/bin/env python
"""
You just finish implementing your winning light pattern when you realize you mistranslated Santa's message from Ancient Nordic Elvish.

The light grid you bought actually has individual brightness controls; each light can have a brightness of zero or more. The lights all start at zero.

The phrase turn on actually means that you should increase the brightness of those lights by 1.

The phrase turn off actually means that you should decrease the brightness of those lights by 1, to a minimum of zero.

The phrase toggle actually means that you should increase the brightness of those lights by 2.

What is the total brightness of all lights combined after following Santa's instructions?

For example:

turn on 0,0 through 0,0 would increase the total brightness by 1.
toggle 0,0 through 999,999 would increase the total brightness by 2000000.
"""


with open('input','r') as f:
    data = f.read().splitlines()

lights = [[0] * 1000 for i in range(1000)]

for instruction in data:
    instruction = instruction.split(" ")
    if instruction[0] == 'toggle':
        top_left = [int(i) for i in instruction[1].split(",")]
        bot_right = [int(i) for i in instruction[3].split(",")]
        for i in range(top_left[0], bot_right[0] + 1):
            for j in range(top_left[1], bot_right[1] + 1):
                lights[i][j] += 2
    
    else:
        top_left = [int(i) for i in instruction[2].split(",")]
        bot_right = [int(i) for i in instruction[4].split(",")]
        if instruction[1] == 'on':
            value = 1
        else: 
            value = -1
        for i in range(top_left[0], bot_right[0] + 1):
            for j in range(top_left[1], bot_right[1] + 1):
                lights[i][j] += value
                if lights[i][j] < 0:
                    lights[i][j] = 0

total = 0
for i in range(1000):
    total += sum(lights[i])
print(total)
