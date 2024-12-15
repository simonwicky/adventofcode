#!/usr/bin/env python

"""
It seems like there is still quite a bit of duplicate work planned. Instead, the Elves would like to know the number of pairs that overlap at all.

In the above example, the first two pairs (2-4,6-8 and 2-3,4-5) don't overlap, while the remaining four pairs (5-7,7-9, 2-8,3-7, 6-6,4-6, and 2-6,4-8) do overlap:

5-7,7-9 overlaps in a single section, 7.
2-8,3-7 overlaps all of the sections 3 through 7.
6-6,4-6 overlaps in a single section, 6.
2-6,4-8 overlaps in sections 4, 5, and 6.
So, in this example, the number of overlapping assignment pairs is 4.


"""

with open('input','r') as f:
	lines = f.read().splitlines()
total = 0
for line in lines:
	start_1 = int(line.split(",")[0].split("-")[0])
	end_1 = int(line.split(",")[0].split("-")[1])
	start_2 = int(line.split(",")[1].split("-")[0])
	end_2 = int(line.split(",")[1].split("-")[1])


	if start_1 <= end_2 and start_2 <= end_1:
		total += 1

print(total)