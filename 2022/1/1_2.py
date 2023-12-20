#!/usr/bin/env python

"""
By the time you calculate the answer to the Elves' question, they've already realized that the Elf carrying the most Calories of food might eventually run out of snacks.

To avoid this unacceptable situation, the Elves would instead like to know the total Calories carried by the top three Elves carrying the most Calories. That way, even if one of those Elves runs out of snacks, they still have two backups.

In the example above, the top three Elves are the fourth Elf (with 24000 Calories), then the third Elf (with 11000 Calories), then the fifth Elf (with 10000 Calories). The sum of the Calories carried by these three elves is 45000.

Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
"""

with open('input','r') as f:
	lines = f.read().splitlines()

lines += ['']

top3 = [0,0,0]

curr = 0
for line in lines:
	if line == '':
		top3_min = min(top3)
		i = top3.index(top3_min)
		top3[i] = max(curr, top3_min)
		curr = 0
	else:
		curr += int(line)

print(sum(top3))