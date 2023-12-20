#!/usr/bin/env python

"""
You resume walking through the valley of mirrors and - SMACK! - run directly into one. Hopefully nobody was watching, because that must have been pretty embarrassing.

Upon closer inspection, you discover that every mirror has exactly one smudge: exactly one . or # should be the opposite type.

In each pattern, you'll need to locate and fix the smudge that causes a different reflection line to be valid. (The old reflection line won't necessarily continue being valid after the smudge is fixed.)

Here's the above example again:

#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
The first pattern's smudge is in the top-left corner. If the top-left # were instead ., it would have a different, horizontal line of reflection:

1 ..##..##. 1
2 ..#.##.#. 2
3v##......#v3
4^##......#^4
5 ..#.##.#. 5
6 ..##..##. 6
7 #.#.##.#. 7
With the smudge in the top-left corner repaired, a new horizontal line of reflection between rows 3 and 4 now exists. Row 7 has no corresponding reflected row and can be ignored, but every other row matches exactly: row 1 matches row 6, row 2 matches row 5, and row 3 matches row 4.

In the second pattern, the smudge can be fixed by changing the fifth symbol on row 2 from . to #:

1v#...##..#v1
2^#...##..#^2
3 ..##..### 3
4 #####.##. 4
5 #####.##. 5
6 ..##..### 6
7 #....#..# 7
Now, the pattern has a different horizontal line of reflection between rows 1 and 2.

Summarize your notes as before, but instead use the new different reflection lines. In this example, the first pattern's new horizontal line has 3 rows above it and the second pattern's new horizontal line has 1 row above it, summarizing to the value 400.

In each pattern, fix the smudge and find the different line of reflection. What number do you get after summarizing the new reflection line in each pattern in your notes?

"""

def equal_with_smudge(line1, line2):
	smudge = False
	if len(line1) != len(line2):
		return False, False
	for i in range(len(line1)):
		if line1[i] != line2[i] and smudge:
			return False, True
		if line1[i] != line2[i]:
			smudge = True

	return True, smudge

def horizontal_sym(pattern):
	prev_line = ""
	for index,line in enumerate(pattern):
		symmetry, smudge = equal_with_smudge(line, prev_line)
		if symmetry:
			if check_sym(pattern, index):
				return index
		prev_line = line


	return 0



def check_sym(pattern, index):
	smudge = False


	if index >= len(pattern) / 2:
		indices = range(len(pattern) - index)
	else:
		indices = range(index)

	for i in indices:
		equal, new_smudge = equal_with_smudge(pattern[index + i], pattern[index -1 - i])
		if not equal or (smudge and new_smudge):
			return False
		smudge = smudge or new_smudge
	return smudge



def transpose(pattern):
	cols = []
	for index in range(len(pattern[0])):
		cols += [''.join([pattern[j][index] for j in range(len(pattern))])]

	return cols


with open("input",'r') as f:
	lines = f.read().splitlines()

lines += [''] #eays delimiter for last one

patterns = []
pattern = []
for line in lines:
	if len(line) == 0:
		patterns += [pattern]
		pattern = []
	else:
		pattern += [line]


tot = 0
for pattern in patterns:
	tot += 100 * horizontal_sym(pattern)
	tot += horizontal_sym(transpose(pattern))
print(tot)

