#!/usr/bin/env python

type Tile = tuple[int, int]

def rec_size(tile_1 : Tile, tile_2: Tile) -> int:
    return (abs(tile_1[0] - tile_2[0]) + 1) * (abs(tile_1[1] - tile_2[1]) + 1)


def is_green(tile : Tile, red_tiles: list[Tile]) -> bool:
    # ray_casting : look at all horizontal edges on below of the tile
    
    nb_top = 0
    nb_bottom = 0
    for i in range(len(red_tiles)):
        corner1, corner2 = red_tiles[i], red_tiles[i-1]
        if corner1[0] == corner2[0]: # vertical edges
            if corner1[1] > corner2[1]:
               corner1, corner2 = corner2, corner1 # ensure corner 1 is first
            if tile[0] == corner1[0] and tile[1] >= corner1[1] and tile[1] <= corner2[1]:
                return True # on a vertical edge
            
        if corner1[1] == corner2[1]:
            if corner1[0] > corner2[0]:
               corner1, corner2 = corner2, corner1 # ensure corner 1 is higher

            if tile[0] >= corner1[0] and tile[0] <= corner2[0]:

                if tile[1] == corner1[1]:
                    return True # on a horizontal edge
                if tile[1] > corner2[1]:
                    nb_top += 1 # below the edge
                if tile[1] < corner1[1]: 
                    nb_bottom += 1 # on top of the edge           

    if nb_bottom == 0 or nb_top == 0:
        return False
    
    return nb_bottom % 2 == 1 or nb_top % 2 == 1


# I know this fails on some edge cases
def crossing(line_start : Tile, line_end : Tile, red_tiles: list[Tile]) -> bool:
    for i in range(len(red_tiles)):
        corner1, corner2 = red_tiles[i], red_tiles[i-1]
        if line_start[0] == line_end[0] and corner1[1] == corner2[1]:
            if line_start[1] > line_end[1]:
                line_start, line_end = line_end, line_start # ensure corner 1 comes first
            if corner1[0] > corner2[0]:
                corner1, corner2 = corner2, corner1 # ensure corner 1 comes first
            if (line_start[0] >= corner1[0] and line_start[0] <= corner2[0]) and line_start[1] < corner1[1] and line_end[1] > corner1[1]:
                return True

        if line_start[1] == line_end[1] and corner1[0] == corner2[0]:
            if line_start[0] > line_end[0]:
                line_start, line_end = line_end, line_start # ensure corner 1 comes first
            if corner1[1] > corner2[1]:
                corner1, corner2 = corner2, corner1 # ensure corner 1 comes first
            if line_start[1] >= corner1[1] and line_start[1] <= corner2[1] and line_start[0] < corner1[0] and line_end[0] > corner1[0]:
                return True


    
    return False
             

## check that corners are in the shape and that edges are in the shape
def green_perimeter(tile1: Tile, tile2: Tile, red_tiles: list[Tile]) -> bool:
    top_left = (min(tile1[0], tile2[0]),min(tile1[1], tile2[1])) 
    bot_right = (max(tile1[0], tile2[0]),max(tile1[1], tile2[1]))
    top_right = (top_left[0], bot_right[1])
    bot_left = (bot_right[0], top_left[1]) 

    # if a corner isn't in the shape, reject it
    if not is_green(top_left,red_tiles) or not is_green(top_right, red_tiles) or not is_green(bot_left, red_tiles) or not is_green(bot_right,red_tiles):
        return False

    if (crossing(top_right, top_left, red_tiles)
        or crossing(top_right, bot_right, red_tiles)
        or crossing(top_left, bot_left, red_tiles)
        or crossing(bot_right, bot_left, red_tiles)):
        return False

    return True

with open('input','r') as f:
    data = f.read().splitlines()

red_tiles: list[Tile] = [(int(line.split(",")[0]),int(line.split(",")[1])) for line in data]

max_size = 0

for i in range(len(red_tiles)):
    for j in range(i+1,len(red_tiles)):
        if green_perimeter(red_tiles[i], red_tiles[j], red_tiles):
            size = rec_size(red_tiles[i], red_tiles[j])
            if size > max_size:
                max_size = size

print(max_size)
