#!/usr/bin/env python
"""
The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?

"""

numbers = '0123456789'
total = 0
with open("input",'r') as f:
	for line in f:
		for c in line:
			if c in numbers:
				total += 10 * int(c)
				break
		for c in line[::-1]:
			if c in numbers:
				total += int(c)
				break

print(total)		
