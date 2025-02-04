#!/usr/bin/env python
"""
What do you get if you multiply together the values of one chip in each of outputs 0, 1, and 2?
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
            if instructions[nb][0] == 'output':
                outputs[instructions[nb][1]] = low
            else:
                new_bots[instructions[nb][1]] = new_bots.get(instructions[nb][1],[]) + [low]
            if instructions[nb][2] == 'output':
                outputs[instructions[nb][3]] = high
            else:
                new_bots[instructions[nb][3]] = new_bots.get(instructions[nb][3],[]) + [high]
    bots = new_bots
            
print(outputs[0] * outputs[1] * outputs[2])