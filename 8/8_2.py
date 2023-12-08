#!/usr/bin/env python

"""
The sandstorm is upon you and you aren't any closer to escaping the wasteland. You had the camel follow the instructions, but you've barely left your starting position. It's going to take significantly more steps to escape!

What if the map isn't for people - what if the map is for ghosts? Are ghosts even bound by the laws of spacetime? Only one way to find out.

After examining the maps a bit longer, your attention is drawn to a curious fact: the number of nodes with names ending in A is equal to the number ending in Z! If you were a ghost, you'd probably just start at every node that ends with A and follow all of the paths at the same time until they all simultaneously end up at nodes that end with Z.

For example:

LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
Here, there are two starting nodes, 11A and 22A (because they both end with A). As you follow each left/right instruction, use that instruction to simultaneously navigate away from both nodes you're currently on. Repeat this process until all of the nodes you're currently on end with Z. (If only some of the nodes you're on end with Z, they act like any other node and you continue as normal.) In this example, you would proceed as follows:

Step 0: You are at 11A and 22A.
Step 1: You choose all of the left paths, leading you to 11B and 22B.
Step 2: You choose all of the right paths, leading you to 11Z and 22C.
Step 3: You choose all of the left paths, leading you to 11B and 22Z.
Step 4: You choose all of the right paths, leading you to 11Z and 22B.
Step 5: You choose all of the left paths, leading you to 11B and 22C.
Step 6: You choose all of the right paths, leading you to 11Z and 22Z.
So, in this example, you end up entirely on nodes that end in Z after 6 steps.

Simultaneously start on every node that ends with A. How many steps does it take before you're only on nodes that end with Z?

"""

def build_map(lines):
	desert_map = {}
	for line in lines:
		key = line[:3]
		value0 = line[7:10]
		value1 = line[12:15]
		desert_map[key] = (value0,value1)
	return desert_map


def build_instructions(line):
	return [int(c) for c in line.replace("L","0").replace("R","1")]



with open("input",'r') as f:
	lines = f.read().splitlines()

directions = build_instructions(lines[0])
desert_map = build_map(lines[2:])

start_points = [key for key in desert_map.keys() if key[2] == "A"]
s_to_e_steps = [0] * len(start_points)
end_points_ordered = [""] * len(start_points)

end_points = [key for key in desert_map.keys() if key[2] == "Z"]
e_to_e_steps = [0] * len(end_points)


for i in range(len(start_points)):
	step = 0
	position = start_points[i]
	while position not in end_points:
		position = desert_map[position][directions[step % len(directions)]]
		step += 1

	s_to_e_steps[i] = step
	end_points_ordered[i] = position

for i in range(len(end_points)):
	step = 1
	position = desert_map[end_points_ordered[i]][directions[step % len(directions)]]
	while position not in end_points:
		position = desert_map[position][directions[step % len(directions)]]
		step += 1

	e_to_e_steps[i] = step


#This works because s_to_e_steps == e_to_e_steps and GCD(e_to_e_steps) == len(directions)
#I take this wasn't random. Otherwise, a bit more work should be done to get those cycles
import numpy as np
print(np.lcm.reduce(e_to_e_steps))
