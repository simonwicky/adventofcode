#!/usr/bin/env python

"""
Seeing how reindeer move in bursts, Santa decides he's not pleased with the old scoring system.

Instead, at the end of each second, he awards one point to the reindeer currently in the lead. (If there are multiple reindeer tied for the lead, they each get one point.) He keeps the traditional 2503 second time limit, of course, as doing otherwise would be entirely ridiculous.

Given the example reindeer from above, after the first second, Dancer is in the lead and gets one point. He stays in the lead until several seconds into Comet's second burst: after the 140th second, Comet pulls into the lead and gets his first point. Of course, since Dancer had been in the lead for the 139 seconds before that, he has accumulated 139 points by the 140th second.

After the 1000th second, Dancer has accumulated 689 points, while poor Comet, our old champion, only has 312. So, with the new scoring system, Dancer would win (if the race ended at 1000 seconds).

Again given the descriptions of each reindeer (in your puzzle input), after exactly 2503 seconds, how many points does the winning reindeer have?
"""

def distance_after(time, reindeer):
    speed    = reindeer[0]
    duration = reindeer[1]
    rest     = reindeer[2]

    rounds = time // (duration + rest)
    remainder = time % (duration + rest)
    distance = rounds * speed * duration
    if remainder > duration:
        distance += speed * duration
    else:
        distance += speed * remainder
    return distance

with open('input','r') as f:
    data = f.read().splitlines()

reindeers = {}
points = {}

for line in data:
    line_split = line.split(" ")
    reindeer = line_split[0]
    speed = int(line_split[3])
    duration = int(line_split[6])
    rest = int(line_split[13])
    reindeers[reindeer] = (speed, duration, rest)
    points[reindeer] = 0



for race_time in range(1,2504):
    distances = {}
    for reindeer in reindeers:
        distances[reindeer] = distance_after(race_time, reindeers[reindeer])
    for reindeer in reindeers:
        if distances[reindeer] == max(distances.values()):
            points[reindeer] += 1

print(max(points.values()))