#!/usr/bin/env python
"""
You come upon a factory in which many robots are zooming around handing small microchips to each other.

Upon closer examination, you notice that each bot only proceeds when it has two microchips, and once it does, it gives each one to a different bot or puts it in a marked "output" bin. Sometimes, bots take microchips from "input" bins, too.

Inspecting one of the microchips, it seems like they each contain a single number; the bots must use some logic to decide what to do with each chip. You access the local control computer and download the bots' instructions (your puzzle input).

Some of the instructions specify that a specific-valued microchip should be given to a specific bot; the rest of the instructions indicate what a given bot should do with its lower-value or higher-value chip.

For example, consider the following instructions:

value 5 goes to bot 2
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 2
Initially, bot 1 starts with a value-3 chip, and bot 2 starts with a value-2 chip and a value-5 chip.
Because bot 2 has two microchips, it gives its lower one (2) to bot 1 and its higher one (5) to bot 0.
Then, bot 1 has two microchips; it puts the value-2 chip in output 1 and gives the value-3 chip to bot 0.
Finally, bot 0 has two microchips; it puts the 3 in output 2 and the 5 in output 0.
In the end, output bin 0 contains a value-5 microchip, output bin 1 contains a value-2 microchip, and output bin 2 contains a value-3 microchip. In this configuration, bot number 2 is responsible for comparing value-5 microchips with value-2 microchips.

Based on your instructions, what is the number of the bot that is responsible for comparing value-61 microchips with value-17 microchips?
"""

with open('input','r') as f:
    data = f.read().splitlines()


bots = {}
instructions = {}
outputs = {}


for line in data:
    line = line.split(" ")
    if line[0] == "value":
        bots[int(line[5])] = bots.get(int(line[5]),[]) + [int(line[1])]
    else:
        instructions[int(line[1])] = [line[5],int(line[6]), line[10],int(line[11])]

done = False
while not done:
    done = True
    new_bots = {}
    for nb in bots:
        if len(bots[nb]) == 1:
            new_bots[nb] = new_bots.get(nb,[]) + bots[nb]
        if len(bots[nb]) == 2:
            done = False
            low = min(bots[nb])
            high = max(bots[nb])
            if low == 17 and high == 61:
                print(nb)
                done = True
                break
            if instructions[nb][0] == 'output':
                outputs[instructions[nb][1]] = low
            else:
                new_bots[instructions[nb][1]] = new_bots.get(instructions[nb][1],[]) + [low]
            if instructions[nb][2] == 'output':
                outputs[instructions[nb][3]] = high
            else:
                new_bots[instructions[nb][3]] = new_bots.get(instructions[nb][3],[]) + [high]
    bots = new_bots
            
