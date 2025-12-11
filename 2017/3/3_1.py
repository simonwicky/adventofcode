#!/usr/bin/env python


with open('input','r') as f:
    target = int(f.read())


# Each "spiral" is a square with numbers up to (2n+1)**2 for the nth spiral

square_side = int(target ** 0.5) + 1 # ceil(sqrt(target))

# index of middle of the side
middle = square_side // 2 + 1

offset = (square_side ** 2 - target) % square_side


print(middle - 1 + abs(middle - offset) + 1)

# It was solved with pen and paper tbh
# 1. Find what spiral the target is on
# 2. Find the offset to the last number of the spiral
# 3. Find the offset to the middle of the side
# 4. Add steps to go to middle of side and then middle of everything