#!/usr/bin/env python


"""
The missing part wasn't the only issue - one of the gears in the engine is wrong. A gear is any * symbol that is adjacent to exactly two part numbers. Its gear ratio is the result of multiplying those two numbers together.

This time, you need to find the gear ratio of every gear and add them all up so that the engineer can figure out which gear needs to be replaced.

Consider the same engine schematic again:

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
In this schematic, there are two gears. The first is in the top left; it has part numbers 467 and 35, so its gear ratio is 16345. The second gear is in the lower right; its gear ratio is 451490. (The * adjacent to 617 is not a gear because it is only adjacent to one part number.) Adding up all of the gear ratios produces 467835.

What is the sum of all of the gear ratios in your engine schematic?

"""

def gear_ratio(engine, i, j):
	numbers = []
	starts = [(-1,-1)]

	for k in [i-1 , i, i+1]:
		for l in [j-1, j, j+1]:
			start, number = get_number(engine, k,l)
			if start not in starts:
				starts += [start]
				numbers += [number]
	if len(numbers) == 2:
		return numbers[1] * numbers[0]
	return 0


#return the number that uses (i,j) as digit, along with the start of that number
#if (i,j) is not a digit, return (-1,-1), -1
def get_number(engine, i, j):
	if not engine[i][j].isdigit():
		return (-1,-1), -1

	start = j
	end = j
	while engine[i][start-1].isdigit():
		start -=1

	while engine[i][end+1].isdigit():
		end +=1

	return (i,start), int(engine[i][start:end+1])



with open('input','r') as f:
	engine = f.read().splitlines()

#adding dots around the engine so we can disregard bound problems
engine = ['.' * len(engine[0])] + engine + ['.' * len(engine[0])]
engine = ['.' + line + '.' for line in engine]


total = 0

for i in range(len(engine)):
	for j in range(len(engine[i])):
		if engine[i][j] == '*':
			total += gear_ratio(engine, i, j)

		
print(total)
