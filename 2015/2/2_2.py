#!/usr/bin/env python
"""
The elves are also running low on ribbon. Ribbon is all the same width, so they only have to worry about the length they need to order, which they would again like to be exact.

The ribbon required to wrap a present is the shortest distance around its sides, or the smallest perimeter of any one face. Each present also requires a bow made out of ribbon as well; the feet of ribbon required for the perfect bow is equal to the cubic feet of volume of the present. Don't ask how they tie the bow, though; they'll never tell.

For example:

A present with dimensions 2x3x4 requires 2+2+3+3 = 10 feet of ribbon to wrap the present plus 2*3*4 = 24 feet of ribbon for the bow, for a total of 34 feet.
A present with dimensions 1x1x10 requires 1+1+1+1 = 4 feet of ribbon to wrap the present plus 1*1*10 = 10 feet of ribbon for the bow, for a total of 14 feet.
How many total feet of ribbon should they order?
"""

with open('input','r') as f:
    data = f.read().splitlines()

total = 0
for line in data:
    dimensions = [int(i) for i in line.split("x")]
    total += dimensions[0] * dimensions[1] * dimensions[2]
    #instead of adding twice the two smallest sides, add twice everything and remove the bigger one
    total += 2 * sum(dimensions)
    total -= 2 * max(dimensions)

print(total)