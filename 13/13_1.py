#!/usr/bin/env python

"""
As you move through the valley of mirrors, you find that several of them have fallen from the large metal frames keeping them in place. The mirrors are extremely flat and shiny, and many of the fallen mirrors have lodged into the ash at strange angles. Because the terrain is all one color, it's hard to tell where it's safe to walk or where you're about to run into a mirror.

You note down the patterns of ash (.) and rocks (#) that you see as you walk (your puzzle input); perhaps by carefully analyzing these patterns, you can figure out where the mirrors are!

For example:

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
To find the reflection in each pattern, you need to find a perfect reflection across either a horizontal line between two rows or across a vertical line between two columns.

In the first pattern, the reflection is across a vertical line between two columns; arrows on each of the two columns point at the line between the columns:

123456789
    ><   
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.
    ><   
123456789
In this pattern, the line of reflection is the vertical line between columns 5 and 6. Because the vertical line is not perfectly in the middle of the pattern, part of the pattern (column 1) has nowhere to reflect onto and can be ignored; every other column has a reflected column within the pattern and must match exactly: column 2 matches column 9, column 3 matches 8, 4 matches 7, and 5 matches 6.

The second pattern reflects across a horizontal line instead:

1 #...##..# 1
2 #....#..# 2
3 ..##..### 3
4v#####.##.v4
5^#####.##.^5
6 ..##..### 6
7 #....#..# 7
This pattern reflects across the horizontal line between rows 4 and 5. Row 1 would reflect with a hypothetical row 8, but since that's not in the pattern, row 1 doesn't need to match anything. The remaining rows match: row 2 matches row 7, row 3 matches row 6, and row 4 matches row 5.

To summarize your pattern notes, add up the number of columns to the left of each vertical line of reflection; to that, also add 100 multiplied by the number of rows above each horizontal line of reflection. In the above example, the first pattern's vertical line has 5 columns to its left and the second pattern's horizontal line has 4 rows above it, a total of 405.

Find the line of reflection in each of the patterns in your notes. What number do you get after summarizing all of your notes?
"""

def horizontal_sym(pattern):
	prev_line = ""
	for index,line in enumerate(pattern):
		if line == prev_line:
			if check_sym(pattern, index):
				return index
		prev_line = line


	return 0



def check_sym(pattern, index):
	if index >= len(pattern) / 2:
		start = index - (len(pattern) - index)
		return pattern[index:] == pattern[index-1:start-1:-1]

	end = index * 2
	return pattern[index -1::-1] == pattern[index:end]

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
