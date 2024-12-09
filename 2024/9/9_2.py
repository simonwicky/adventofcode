#!/usr/bin/env python
"""
Upon completion, two things immediately become clear. First, the disk definitely has a lot more contiguous free space, just like the amphipod hoped. Second, the computer is running much more slowly! Maybe introducing all of that file system fragmentation was a bad idea?

The eager amphipod already has a new plan: rather than move individual blocks, he'd like to try compacting the files on his disk by moving whole files instead.

This time, attempt to move whole files to the leftmost span of free space blocks that could fit the file. Attempt to move each file exactly once in order of decreasing file ID number starting with the file with the highest file ID number. If there is no span of free space to the left of a file that is large enough to fit the file, the file does not move.

The first example from above now proceeds differently:

00...111...2...333.44.5555.6666.777.888899
0099.111...2...333.44.5555.6666.777.8888..
0099.1117772...333.44.5555.6666.....8888..
0099.111777244.333....5555.6666.....8888..
00992111777.44.333....5555.6666.....8888..
The process of updating the filesystem checksum is the same; now, this example's checksum would be 2858.

Start over, now compacting the amphipod's hard drive using this new method instead. What is the resulting filesystem checksum?
"""


def find_free_space(ls, file):
    for i in range(len(ls)):
        if ls[i: i + file[1]] == [file[0]] * file[1]:
            return -1
        if ls[i: i + file[1]] == [-1] * file[1]:
            return i
    return -1


with open('input','r') as f:
    disk = f.read().splitlines()[0]

            

only_data = [(i // 2 ,int(size)) for i,size in enumerate(disk) if i % 2 == 0]
expanded_disk = []

id = 0
data = True
for size in disk:
    if data:
        expanded_disk += [id] * int(size)
        id += 1
    else:
        expanded_disk += [-1] * int(size)
    data = not data

for file in reversed(only_data):
    print(file)
    index = find_free_space(expanded_disk, file)
    if index != -1:
        for i in range(len(expanded_disk)):
            if expanded_disk[i] == file[0]:
                expanded_disk[i] = -1
        expanded_disk = expanded_disk[:index] + [file[0]] * file[1] + expanded_disk[index + file[1]:]
        

for i in range(len(expanded_disk)):
    if expanded_disk[i] == -1:
        expanded_disk[i] = 0



print(sum([i * el for i, el in enumerate(expanded_disk)]))
            
#this is slow as fuck
#6250605700557
#should do better, probably numpy array for the searching and replacing


