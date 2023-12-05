#!/usr/bin/env python
"""
Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

What is the sum of all of the calibration values?
"""

numbers = '0123456789'
numbers_spelled = ['zero','one','two','three','four','five','six','seven','eight','nine']
total = 0
with open("input",'r') as f:
	for line in f:
		found = False
		for i in range(len(line)):
			if not found and line[i] in numbers:
				total += 10 * int(line[i])
				
				found = True
			for v, n in enumerate(numbers_spelled):
				try:
					if not found and line[i:].index(n) == 0:
						total += 10 * v
						found = True
				except:
					pass

		found = False
		for i in range(len(line)-1,-1,-1):
			if not found and line[i] in numbers:
				total += int(line[i])
				found = True
			for v, n in enumerate(numbers_spelled):
				try:
					if not found and line[i:].index(n) == 0:
						total += v
						found = True
				except:
					pass


print(total)	



