#!/usr/bin/env python
"""
That's weird... the sleigh still isn't balancing.

"Ho ho ho", Santa muses to himself. "I forgot the trunk".

Balance the sleigh again, but this time, separate the packages into four groups instead of three. The other constraints still apply.

Given the example packages above, this would be some of the new unique first groups, their quantum entanglements, and one way to divide the remaining packages:


11 4    (QE=44); 10 5;   9 3 2 1; 8 7
10 5    (QE=50); 11 4;   9 3 2 1; 8 7
9 5 1   (QE=45); 11 4;   10 3 2;  8 7
9 4 2   (QE=72); 11 3 1; 10 5;    8 7
9 3 2 1 (QE=54); 11 4;   10 5;    8 7
8 7     (QE=56); 11 4;   10 5;    9 3 2 1
Of these, there are three arrangements that put the minimum (two) number of packages in the first group: 11 4, 10 5, and 8 7. Of these, 11 4 has the lowest quantum entanglement, and so it is selected.

Now, what is the quantum entanglement of the first group of packages in the ideal configuration?
"""
import itertools

with open('input','r') as f:
    pkts = [int(line) for line in f.read().splitlines()]

target = sum(pkts) // 4

smallest_group = 5 #looking at an all odd input and an odd target, we can easily derive that we need 5 ptks minimum

min_qe = 1e20
for group_1 in itertools.combinations(pkts,smallest_group):
    if sum(group_1) == target:
        qe = 1
        for x in group_1:
            qe *= x
        min_qe = min(min_qe, qe)

print(min_qe)