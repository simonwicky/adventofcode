#!/usr/bin/env python


# Josephus problem but with powers of 3
import math

with open('input','r') as f:
    n = int(f.read())


m = math.floor(math.log(n,3))
k = 3 ** m


if n == k:
    print(n)
elif n <= 2*k:
    print(n - k)
else:
    print(2*n - 3*k)

