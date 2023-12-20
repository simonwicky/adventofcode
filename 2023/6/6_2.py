#!/usr/bin/env python
"""
As the race is about to start, you realize the piece of paper with race times and record distances you got earlier actually just has very bad kerning. There's really only one race - ignore the spaces between the numbers on each line.

So, the example from before:

Time:      7  15   30
Distance:  9  40  200
...now instead means this:

Time:      71530
Distance:  940200
Now, you have to figure out how many ways there are to win this single race. In this example, the race lasts for 71530 milliseconds and the record distance you need to beat is 940200 millimeters. You could hold the button anywhere from 14 to 71516 milliseconds and beat the record, a total of 71503 ways!

"""

#Same reflexion as 6.1
#Let T be the time of the race and D the distance to beat. A boat held X ms will reach a distance of X(T-X)mm. We're then looking for integer solutions of X (T - X) > D
#That gives us (T ± SQRT(T^2 -4D)) / 2. Any integer between those bounds will be a solution

import math


def nb_solution(time, distance):
	l_b = (time - math.sqrt(time * time - 4 * distance)) / 2
	u_b = (time + math.sqrt(time * time - 4 * distance)) / 2
	return math.floor(u_b) - math.ceil(l_b) + 1


with open("input",'r') as f:
	lines = f.read().splitlines()

time = ''.join(lines[0].split()[1:])
distance = ''.join(lines[1].split()[1:])

print(nb_solution(int(time), int(distance)))