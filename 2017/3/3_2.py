#!/usr/bin/env python

with open('input','r') as f:
    target = int(f.read())


def neighbors_sum(square : tuple[int, int], grid: dict[tuple[int,int], int]):
    total = 0
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            if i == 0 and j == 0:
                continue
            total += grid.get((square[0] + i,square[1] + j),0)
    return total






grid: dict[tuple[int,int], int] = {}


square = (0,0)
grid[square] = 1

square_side = 3
directions = [(-1,0),(0,-1),(1,0),(0,1)] # up, left, down right

answer = 0

# we're gonna finish the square before returning but that saves us an exit()
while grid[square] < target:
    for j in range(4):
        for i in range(square_side - 1):
            if i == 0 and j == 0:
                square = (square[0],square[1] + 1) # we start on the right of the previous value
            else:
                square = (square[0] + directions[j][0], square[1] + directions[j][1])
            grid[square] = neighbors_sum(square, grid)
            if grid[square] > target and answer == 0:
                answer = grid[square]
    square_side += 2



print(answer)
