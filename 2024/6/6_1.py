#!/usr/bin/env python
"""
The Historians use their fancy device again, this time to whisk you all away to the North Pole prototype suit manufacturing lab... in the year 1518! It turns out that having direct access to history is very convenient for a group of historians.

You still have to be careful of time paradoxes, and so it will be important to avoid anyone from 1518 while The Historians search for the Chief. Unfortunately, a single guard is patrolling this part of the lab.

Maybe you can work out where the guard will go ahead of time so that The Historians can search safely?

You start by making a map (your puzzle input) of the situation. For example:

....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
The map shows the current position of the guard with ^ (to indicate the guard is currently facing up from the perspective of the map). Any obstructions - crates, desks, alchemical reactors, etc. - are shown as #.

Lab guards in 1518 follow a very strict patrol protocol which involves repeatedly following these steps:

If there is something directly in front of you, turn right 90 degrees.
Otherwise, take a step forward.
Following the above protocol, the guard moves up several times until she reaches an obstacle (in this case, a pile of failed suit prototypes):

....#.....
....^....#
..........
..#.......
.......#..
..........
.#........
........#.
#.........
......#...
Because there is now an obstacle in front of the guard, she turns right before continuing straight in her new facing direction:

....#.....
........>#
..........
..#.......
.......#..
..........
.#........
........#.
#.........
......#...
Reaching another obstacle (a spool of several very long polymers), she turns right again and continues downward:

....#.....
.........#
..........
..#.......
.......#..
..........
.#......v.
........#.
#.........
......#...
This process continues for a while, but the guard eventually leaves the mapped area (after walking past a tank of universal solvent):

....#.....
.........#
..........
..#.......
.......#..
..........
.#........
........#.
#.........
......#v..
By predicting the guard's route, you can determine which specific positions in the lab will be in the patrol path. Including the guard's starting position, the positions visited by the guard before leaving the area are marked with an X:

....#.....
....XXXXX#
....X...X.
..#.X...X.
..XXXXX#X.
..X.X.X.X.
.#XXXXXXX.
.XXXXXXX#.
#XXXXXXX..
......#X..
In this example, the guard will visit 41 distinct positions on your map.

Predict the path of the guard. How many distinct positions will the guard visit before leaving the mapped area?

"""

def grid_get(grid, i,j):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]):
        return ''
    return grid[i][j]

def get_start_position(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid_get(grid,i,j) == '^':
                return (i,j)


with open('input','r') as f:
    grid = f.read().splitlines()


position = get_start_position(grid)

direction = (-1,0)
path = set()
path.add(position)
new_path = '^'

while new_path:
    new_position = (position[0] + direction[0], position[1] + direction[1])
    new_path = grid_get(grid, new_position[0], new_position[1])
    if new_path == '.' or new_path == '^': #possible to take a step, take a step, add the path
        path.add(new_position)
        position = new_position
    elif new_path == '#': #obstacle, don't move, turn right
        direction = (direction[1],-direction[0]) #that's a right turn


print(len(path))


# Visualize the path if wanted
# with open('output','w') as f:
#     for i in range(len(grid)):
#         for j in range(len(grid[i])):
#             if grid_get(grid,i,j) == '.' and  (i,j) in path:
#                 f.write('X')
#             else:
#                 f.write(grid_get(grid,i,j))
#         f.write('\n')
