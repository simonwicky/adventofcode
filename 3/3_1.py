#!/usr/bin/env python


"""
The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. If you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.

The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)

Here is an example engine schematic:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?

"""

non_symbols = '0123456789.'

def adjacent(engine, line_index, start, end):

	lower_bound = start - 1
	upper_bound = end + 1

	if engine[line_index][lower_bound] not in non_symbols:
		return True
	if engine[line_index][upper_bound] not in non_symbols:
		return True

	for j in range(lower_bound, upper_bound + 1):
		if engine[line_index - 1][j] not in non_symbols:
			return True
		if engine[line_index + 1][j] not in non_symbols:
			return True


	return False



with open('input','r') as f:
	engine = f.read().splitlines()

#adding dots around the engine so we can disregard bound problems
engine = ['.' * len(engine[0])] + engine + ['.' * len(engine[0])]
engine = ['.' + line + '.' for line in engine]


total = 0

for i in range(len(engine)):
	start = -1
	for j in range(len(engine[i])):
		if start != -1 and not engine[i][j].isdigit() : #number finished at j-1

			if adjacent(engine, i, start, j-1):
				total += int(engine[i][start:j])

			start = -1

		if start == -1 and engine[i][j].isdigit():
			start = j

		
print(total)
