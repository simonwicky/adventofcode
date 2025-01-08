#!/usr/bin/env python

"""
Now, given the same instructions, find the position of the first character that causes him to enter the basement (floor -1). The first character in the instructions has position 1, the second character has position 2, and so on.

For example:

) causes him to enter the basement at character position 1.
()()) causes him to enter the basement at character position 5.
What is the position of the character that causes Santa to first enter the basement?
"""


with open('input','r') as f:
    data = f.read()

floor = 0
i = 0
while floor >= 0:
    if data[i] == '(':
        floor += 1
    elif data[i] == ')':
        floor -= 1
    i += 1

print(i)