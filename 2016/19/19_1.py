#!/usr/bin/env python


# This a non bloody version of Josephus problem, which is sovled
# Gvien N people, N = 2**m + l, with 0 < l < 2** m, then the last one is 2*l + 1

import math

with open('input','r') as f:
    n = int(f.read())

m = math.floor(math.log2(n))
l = n - 2 ** m
print(2 * l + 1)