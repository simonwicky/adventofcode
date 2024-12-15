#!/usr/bin/env python
"""
The lanternfish use your information to find a safe moment to swim in and turn off the malfunctioning robot! Just as they start preparing a festival in your honor, reports start coming in that a second warehouse's robot is also malfunctioning.

This warehouse's layout is surprisingly similar to the one you just helped. There is one key difference: everything except the robot is twice as wide! The robot's list of movements doesn't change.

To get the wider warehouse's map, start with your original map and, for each tile, make the following changes:

If the tile is #, the new map contains ## instead.
If the tile is O, the new map contains [] instead.
If the tile is ., the new map contains .. instead.
If the tile is @, the new map contains @. instead.
This will produce a new warehouse map which is twice as wide and with wide boxes that are represented by []. (The robot does not change size.)

The larger example from before would now look like this:

####################
##....[]....[]..[]##
##............[]..##
##..[][]....[]..[]##
##....[]@.....[]..##
##[]##....[]......##
##[]....[]....[]..##
##..[][]..[]..[][]##
##........[]......##
####################
Because boxes are now twice as wide but the robot is still the same size and speed, boxes can be aligned such that they directly push two other boxes at once. For example, consider this situation:

#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######

<vv<<^^<<^^
After appropriately resizing this map, the robot would push around these boxes as follows:

Initial state:
##############
##......##..##
##..........##
##....[][]@.##
##....[]....##
##..........##
##############

Move <:
##############
##......##..##
##..........##
##...[][]@..##
##....[]....##
##..........##
##############

Move v:
##############
##......##..##
##..........##
##...[][]...##
##....[].@..##
##..........##
##############

Move v:
##############
##......##..##
##..........##
##...[][]...##
##....[]....##
##.......@..##
##############

Move <:
##############
##......##..##
##..........##
##...[][]...##
##....[]....##
##......@...##
##############

Move <:
##############
##......##..##
##..........##
##...[][]...##
##....[]....##
##.....@....##
##############

Move ^:
##############
##......##..##
##...[][]...##
##....[]....##
##.....@....##
##..........##
##############

Move ^:
##############
##......##..##
##...[][]...##
##....[]....##
##.....@....##
##..........##
##############

Move <:
##############
##......##..##
##...[][]...##
##....[]....##
##....@.....##
##..........##
##############

Move <:
##############
##......##..##
##...[][]...##
##....[]....##
##...@......##
##..........##
##############

Move ^:
##############
##......##..##
##...[][]...##
##...@[]....##
##..........##
##..........##
##############

Move ^:
##############
##...[].##..##
##...@.[]...##
##....[]....##
##..........##
##..........##
##############
This warehouse also uses GPS to locate the boxes. For these larger boxes, distances are measured from the edge of the map to the closest edge of the box in question. So, the box shown below has a distance of 1 from the top edge of the map and 5 from the left edge of the map, resulting in a GPS coordinate of 100 * 1 + 5 = 105.

##########
##...[]...
##........
In the scaled-up version of the larger example from above, after the robot has finished all of its moves, the warehouse would look like this:

####################
##[].......[].[][]##
##[]...........[].##
##[]........[][][]##
##[]......[]....[]##
##..##......[]....##
##..[]............##
##..@......[].[][]##
##......[][]..[]..##
####################
The sum of these boxes' GPS coordinates is 9021.

Predict the motion of the robot and boxes in this new, scaled-up warehouse. What is the sum of all boxes' final GPS coordinates?
"""


def grid_get(grid, position):
    i = position[0]
    j = position[1]
    return grid[i][j]

def grid_set(grid, position, value):
    i = position[0]
    j = position[1]
    grid[i][j] = value
    return grid

def direction(instruction):
    if instruction == '^':
        return (-1, 0)
    if instruction == 'v':
        return (1, 0)
    if instruction == '<':
        return (0, -1)
    if instruction == '>':
        return (0, 1)
    
def step(warehouse, position, direction):
    new_position = (position[0] + direction[0], position[1] + direction[1])
    #If new spot is empty, just move there
    if grid_get(warehouse, new_position) == '.':
        return warehouse, new_position
    #if new spot is a wall, nothing happens
    if grid_get(warehouse, new_position) == '#':
        return warehouse, position
    
    #i f****ing hate shallow copies
    warehouse_copy = [[i for i in row] for row in warehouse]
    moved_box, new_warehouse = movable_box(warehouse_copy, new_position, direction)
    if moved_box:
        return new_warehouse, new_position
    return warehouse, position

def movable_box(warehouse, position, direction):
    if grid_get(warehouse, position) == '.':#nothing to push
        return True, warehouse
    if grid_get(warehouse, position) == '[':
        box_l = position 
        box_r = (position[0], position[1] + 1)
    else:
        box_l = (position[0], position[1] - 1)
        box_r = position 

    new_box_l = (box_l[0] + direction[0], box_l[1] + direction[1])
    new_box_r = (box_r[0] + direction[0], box_r[1] + direction[1])

    #nothing to move
    if grid_get(warehouse,new_box_l) == '#' or grid_get(warehouse,new_box_r) == '#':
        return False, warehouse
    
    #we can move, moving the box and returning
    if ((grid_get(warehouse,new_box_l) == '.' or new_box_l == box_r ) and 
        (grid_get(warehouse,new_box_r) == '.' or new_box_r == box_l )):
        new_warehouse = grid_set(warehouse, box_l,'.')
        new_warehouse = grid_set(new_warehouse, box_r,'.')
        new_warehouse = grid_set(new_warehouse, new_box_l,'[')
        new_warehouse = grid_set(new_warehouse, new_box_r,']')
        return True, new_warehouse
    


    #moving to the right
    if new_box_l == box_r:
        movable, new_warehouse =  movable_box(warehouse, new_box_r, direction)
    #moving to the left
    elif new_box_r == box_l:
        movable, new_warehouse =  movable_box(warehouse, new_box_l, direction)
    else:
    #moving up or down
        left_movable, new_warehouse = movable_box(warehouse, new_box_l, direction)
        right_movable, new_warehouse = movable_box(new_warehouse, new_box_r, direction)
        movable = left_movable and right_movable
            

    if movable:
        new_warehouse = grid_set(new_warehouse, box_l,'.')
        new_warehouse = grid_set(new_warehouse, box_r,'.')
        new_warehouse = grid_set(new_warehouse, new_box_l,'[')
        new_warehouse = grid_set(new_warehouse, new_box_r,']')
        return True, new_warehouse
    return False, warehouse




with open('input','r') as f:
    lines = f.read().splitlines()

warehouse = []
i = 0
while lines[i] != '':
    current = []
    for j in range(len(lines[i])):
        if lines[i][j] == '#':
            current += ['#','#']
        if lines[i][j] == '.':
            current += ['.','.']
        if lines[i][j] == 'O':
            current += ['[',']']
        if lines[i][j] == '@':
            current += ['.','.']
            position = (i,2 * j)
    warehouse += [current]
    i += 1

instructions = ''.join(lines[i+1:])

for instruction in instructions:
    warehouse, position = step(warehouse, position, direction(instruction))

total  = 0
for i in range(len(warehouse)):
    for j in range(len(warehouse[i])):
        #if position == (i,j):
        #    print('@',end='')
        #else:
        #    print(warehouse[i][j], end='')
        if warehouse[i][j] == '[':
            total += 100 * i + j
    #print()

print(total)
