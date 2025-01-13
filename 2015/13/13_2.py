#!/usr/bin/env python
"""
In all the commotion, you realize that you forgot to seat yourself. At this point, you're pretty apathetic toward the whole thing, and your happiness wouldn't really go up or down regardless of who you sit next to. You assume everyone else would be just as ambivalent about sitting next to you, too.

So, add yourself to the list, and give all happiness relationships that involve you a score of 0.

What is the total change in happiness for the optimal seating arrangement that actually includes yourself?
"""


import itertools

with open('input','r') as f:
    data = f.read().splitlines()

happiness_change = {}
people = set()

for line in data:
    line_split = line.split(" ")
    p1 = line_split[0]
    p2 = line_split[-1][:-1]
    d = int(line_split[3])
    if line_split[2] == 'lose':
        d *= -1
    people.add(p1)
    happiness_change[(p1,p2)] = d

for p in people:
    happiness_change[("you",p)] = 0
    happiness_change[(p,"you")] = 0
people.add("you")

max_change = 0
for seating in itertools.permutations(people, len(people)):
    happiness = 0
    for i in range(len(seating)):
        happiness += happiness_change[(seating[i], seating[(i + 1) % len(seating)])]
        happiness += happiness_change[(seating[i], seating[(i - 1) % len(seating)])]
    max_change = max(max_change, happiness)

print(max_change)