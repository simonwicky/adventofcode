#!/usr/bin/env python

"""
As you look out at the field of springs, you feel like there are way more springs than the condition records list. When you examine the records, you discover that they were actually folded up this whole time!

To unfold the records, on each row, replace the list of spring conditions with five copies of itself (separated by ?) and replace the list of contiguous groups of damaged springs with five copies of itself (separated by ,).

So, this row:

.# 1
Would become:

.#?.#?.#?.#?.# 1,1,1,1,1
The first line of the above example would become:

???.###????.###????.###????.###????.### 1,1,3,1,1,3,1,1,3,1,1,3,1,1,3
In the above example, after unfolding, the number of possible arrangements for some rows is now much larger:

???.### 1,1,3 - 1 arrangement
.??..??...?##. 1,1,3 - 16384 arrangements
?#?#?#?#?#?#?#? 1,3,1,6 - 1 arrangement
????.#...#... 4,1,1 - 16 arrangements
????.######..#####. 1,6,5 - 2500 arrangements
?###???????? 3,2,1 - 506250 arrangements
After unfolding, adding all of the possible arrangement counts together produces 525152.

Unfold your condition records; what is the new sum of possible arrangement counts?
"""
from functools import cache

@cache
def nb_arrangement(springs, arrangement):
	if len(springs) == 0 and len(arrangement) == 0: 
		return 1
	if len(springs) == 0 and len(arrangement) > 0: 
		return 0

	if springs[0] == '?': #replace ? by . and # and sum up
		return nb_arrangement('.'  + springs[1:], arrangement) + nb_arrangement('#'  + springs[1:], arrangement)
	if springs[0] == '.': #remove any .
		return nb_arrangement(springs.lstrip('.'), arrangement)

	# springs[0] is a '#'
	if len(arrangement) == 0: #no arrangement left
		return 0
	if len(springs) < arrangement[0]: #not enough springs left
		return 0
	if '.' in springs[:arrangement[0]]: #a . in the # streak
		return 0
	if len(springs) > arrangement[0] and springs[arrangement[0]] == '#': #the one following the streak is another #
		return 0
	return nb_arrangement(springs[arrangement[0] + 1:].lstrip('.'), arrangement[1:]) #remove that group and move further


with open('input','r') as f:
	lines = f.read().splitlines()

tot = 0
for line in lines:
	springs = '?'.join([line.split()[0]] * 5)
	arrangement = tuple([int(i) for i in line.split()[1].split(",")] * 5)
	tot += nb_arrangement(springs, arrangement)

print(tot)


