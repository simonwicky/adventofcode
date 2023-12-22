#!/usr/bin/env python

"""
Disintegrating bricks one at a time isn't going to be fast enough. While it might sound dangerous, what you really need is a chain reaction.

You'll need to figure out the best brick to disintegrate. For each brick, determine how many other bricks would fall if that brick were disintegrated.

Using the same example as above:

Disintegrating brick A would cause all 6 other bricks to fall.
Disintegrating brick F would cause only 1 other brick, G, to fall.
Disintegrating any other brick would cause no other bricks to fall. So, in this example, the sum of the number of other bricks that would fall as a result of disintegrating each brick is 7.

For each brick, determine how many other bricks would fall if that brick were disintegrated. What is the sum of the number of other bricks that would fall?
"""


def get_bricks(lines):
	bricks_pos = {}
	bricks = {}
	for i,line in enumerate(lines):
		start = [int(c) for c in line.split('~')[0].split(',')]
		end = [int(c) for c in line.split('~')[1].split(',')]
		if start[0] != end[0]:
			for j in range(start[0], end[0] + 1):
				bricks_pos[j + start[1] * 1j] = bricks_pos.get(j + start[1] * 1j,[]) + [(i,start[2])]
				bricks[i] = bricks.get(i,[]) + [(j + start[1] * 1j,start[2])] 
		elif start[1] != end[1]:
			for j in range(start[1], end[1] + 1):
				bricks_pos[start[0] + j * 1j] = bricks_pos.get(start[0] + j * 1j, []) + [(i,start[2])]
				bricks[i] = bricks.get(i,[]) + [(start[0] + j * 1j,start[2])] 
		else:
			for j in range(start[2], end[2] + 1):
				bricks_pos[start[0] + start[1] * 1j] = bricks_pos.get(start[0] + start[1] * 1j, []) + [(i,j)]
				bricks[i] = bricks.get(i,[]) + [(start[0] + start[1] * 1j,j)] 

	return bricks_pos, bricks

#get support candidates for each brick, i.e. the list of bricks directly underneath it
def support(bricks, bricks_pos):
	support_cand = {}
	for brick in bricks:
		support_cand[brick] = set()
		for pos in bricks[brick]:
			highest = (-1,0)
			for other in bricks_pos[pos[0]]:
				if other[1] > highest[1] and other[1] < pos[1] and other[0] != brick:
					highest = other
			if highest[0] != -1:
				support_cand[brick].add(highest[0])

	return support_cand

#get brick height once it's settled, equivalent to the brick size + the highest of the support candidates
def brick_height(bricks,support):
	brick_height = {}
	def height(brick):
		if brick not in brick_height:
			brick_size = bricks[brick][-1][1] - bricks[brick][0][1] + 1
			if len(support[brick]) == 0:
				brick_height[brick] = brick_size
			else:
				brick_height[brick] = max([height(b) for b in support[brick]]) + brick_size

		return brick_height[brick]

	for brick in support:
		height(brick)

	return brick_height

#get the list of which brick support which one
def actual_support(brick_height, support):
	actual_supports = {}
	for brick in support:
		support_bricks = support[brick]
		if len(support_bricks) != 0:
			#count how many candidates are actually supporting. If it's one, we count that brick as not touchable
			support_height = max([brick_height[b] for b in support_bricks])
			actual_supports[brick] = [support_brick for support_brick in support_bricks if brick_height[support_brick] == support_height]

	return actual_supports


def disintegrate(actual_supports, brick):
	to_remove = [brick]
	removed = 0
	while len(to_remove) != 0:
		new_actual_supports = {}
		removing = to_remove.pop(0)
		for b in actual_supports:
			new_actual_supports[b] = [i for i in actual_supports[b]]
			if removing in new_actual_supports[b]:
				new_actual_supports[b].remove(removing)
				if len(new_actual_supports[b]) == 0:
					to_remove += [b]
					removed += 1
		actual_supports = new_actual_supports

	return removed





with open('input','r') as f:
	lines = f.read().splitlines()


bricks_pos, bricks = get_bricks(lines)
support = support(bricks, bricks_pos)
brick_height = brick_height(bricks, support)

actual_supports = actual_support(brick_height, support)



total = 0
for i in range(len(bricks)):
	total += disintegrate(actual_supports,i)
print(total)