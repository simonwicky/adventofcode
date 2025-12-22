#!/usr/bin/env python

def is_wall(favorite_number: int, x: int,y: int, ) -> bool:
    s = (x * x) + (3*x) + (2*x*y) + y + (y*y) + favorite_number
    binary = '{:b}'.format(s)

    return binary.count('1') % 2 == 1



with open('input','r') as f:
    favorite_number = int(f.read())



current: set[tuple[int, int]] = set([(1,1)])
visited: set[tuple[int, int]]  = set([(1,1)])



for step in range(50):
    new_current: set[tuple[int, int]] = set()
    for c in current:
        for d in [(-1, 0),(1, 0),(0, -1),(0, 1)]:
            new_c = (c[0] + d[0], c[1] + d[1])
            if new_c not in visited and new_c[0] >= 0 and new_c[1] >= 0 and not is_wall(favorite_number, new_c[0],new_c[1]):
                new_current.add(new_c)
    current = new_current
    visited.update(current)

print(len(visited))
