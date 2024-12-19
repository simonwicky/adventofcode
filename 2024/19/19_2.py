#!/usr/bin/env python

"""
The staff don't really like some of the towel arrangements you came up with. To avoid an endless cycle of towel rearrangement, maybe you should just give them every possible option.

Here are all of the different ways the above example's designs can be made:

brwrr can be made in two different ways: b, r, wr, r or br, wr, r.

bggr can only be made with b, g, g, and r.

gbbr can be made 4 different ways:

g, b, b, r
g, b, br
gb, b, r
gb, br
rrbgbr can be made 6 different ways:

r, r, b, g, b, r
r, r, b, g, br
r, r, b, gb, r
r, rb, g, b, r
r, rb, g, br
r, rb, gb, r
bwurrg can only be made with bwu, r, r, and g.

brgr can be made in two different ways: b, r, g, r or br, g, r.

ubwu and bbrgwb are still impossible.

Adding up all of the ways the towels in this example could be arranged into the desired designs yields 16 (2 + 1 + 4 + 6 + 1 + 2).

They'll let you into the onsen as soon as you have the list. What do you get if you add up the number of different ways you could make each design?
"""




def n_ways_design(design, patterns):
    #ways[i] is the number of way to make design[:i]
    ways = [0] * (len(design) + 1)
    ways[0] = 1

    for i in range(1,len(design) + 1):
        for pattern in patterns:
            if i >= len(pattern) and design[i - len(pattern):i] == pattern:
                ways[i] += ways[i-len(pattern)]

    return ways[len(design)]


with open('input','r') as f:
    lines = f.read().splitlines()

patterns = lines[0].split(", ")

designs = lines[2:]


total = 0
for design in designs:  
    total += n_ways_design(design, patterns)
print(total)