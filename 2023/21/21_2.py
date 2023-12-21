#!/usr/bin/env python

"""
The Elf seems confused by your answer until he realizes his mistake: he was reading from a list of his favorite numbers that are both perfect squares and perfect cubes, not his step counter.

The actual number of steps he needs to get today is exactly 26501365.

He also points out that the garden plots and rocks are set up so that the map repeats infinitely in every direction.

So, if you were to look one additional map-width or map-height out from the edge of the example map above, you would find that it keeps repeating:

.................................
.....###.#......###.#......###.#.
.###.##..#..###.##..#..###.##..#.
..#.#...#....#.#...#....#.#...#..
....#.#........#.#........#.#....
.##...####..##...####..##...####.
.##..#...#..##..#...#..##..#...#.
.......##.........##.........##..
.##.#.####..##.#.####..##.#.####.
.##..##.##..##..##.##..##..##.##.
.................................
.................................
.....###.#......###.#......###.#.
.###.##..#..###.##..#..###.##..#.
..#.#...#....#.#...#....#.#...#..
....#.#........#.#........#.#....
.##...####..##..S####..##...####.
.##..#...#..##..#...#..##..#...#.
.......##.........##.........##..
.##.#.####..##.#.####..##.#.####.
.##..##.##..##..##.##..##..##.##.
.................................
.................................
.....###.#......###.#......###.#.
.###.##..#..###.##..#..###.##..#.
..#.#...#....#.#...#....#.#...#..
....#.#........#.#........#.#....
.##...####..##...####..##...####.
.##..#...#..##..#...#..##..#...#.
.......##.........##.........##..
.##.#.####..##.#.####..##.#.####.
.##..##.##..##..##.##..##..##.##.
.................................
This is just a tiny three-map-by-three-map slice of the inexplicably-infinite farm layout; garden plots and rocks repeat as far as you can see. The Elf still starts on the one middle tile marked S, though - every other repeated S is replaced with a normal garden plot (.).

Here are the number of reachable garden plots in this new infinite version of the example map for different numbers of steps:

In exactly 6 steps, he can still reach 16 garden plots.
In exactly 10 steps, he can reach any of 50 garden plots.
In exactly 50 steps, he can reach 1594 garden plots.
In exactly 100 steps, he can reach 6536 garden plots.
In exactly 500 steps, he can reach 167004 garden plots.
In exactly 1000 steps, he can reach 668697 garden plots.
In exactly 5000 steps, he can reach 16733044 garden plots.
However, the step count the Elf needs is much larger! Starting from the garden plot marked S on your infinite map, how many garden plots could the Elf reach in exactly 26501365 steps?
"""
def step(grid, positions, i_bound, j_bound):
	new_positions = []
	for p in positions:
		for s in [1,-1, 1j, -1j]:
			new_pos = p + s
			if grid_pos(grid, new_pos, i_bound, j_bound) != '#':
				new_positions += [new_pos]

	return set(new_positions)

def grid_pos(grid, position, i_bound, j_bound):
	pos = position.real % i_bound + (position.imag % j_bound * 1j)
	return grid[pos]

# Too many assumptions on the input are made, no general solutions
# => No will to do it, credit to u/4HbQ


G = {i + j*1j: c for i,r in enumerate(open('input'))
                 for j,c in enumerate(r) if c in '.S'}

N = 131

done = []
todo = {x for x in G if G[x]=='S'}

for s in range(int(2.5*N)+1):
    if s%N == N//2: done.append(len(todo))

    todo = {p+d for d in {1,-1,1j,-1j} for p in todo
            if (p+d).real%N + (p+d).imag%N*1j in G}

f = lambda n,a,b,c: a+n*(b-a) +n*(n-1)//2*((c-b)-(b-a))
print(f(26501365//N, *done))