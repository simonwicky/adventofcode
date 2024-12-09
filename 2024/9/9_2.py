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


def find_free_space(disk, file_index):
    file_size = disk[file_index][1]
    for i in range(file_index):
        if disk[i][0] == -1 and disk[i][1] >= file_size:
            return i
    return -1


with open('input','r') as f:
    disk = f.read().splitlines()[0]

            

only_data = [(i // 2 ,int(size)) for i,size in enumerate(disk) if i % 2 == 0]

expanded_disk = []
for i,size in enumerate(disk):
    if size == '0':
        continue
    if i % 2 == 0:
        expanded_disk += [(i // 2 ,int(size))]
    else:
         expanded_disk += [(-1 ,int(size))]


i = len(expanded_disk) -1
while i >= 0:
    if expanded_disk[i][0] != -1:
        index = find_free_space(expanded_disk,i)
        if index != -1:
            if expanded_disk[index][1] == expanded_disk[i][1]:
                expanded_disk[index] = expanded_disk[i] #spot on replacement
            else:
                expanded_disk = expanded_disk[:index] + [expanded_disk[i], (-1, expanded_disk[index][1] - expanded_disk[i][1])] + expanded_disk[index+1:]
                i += 1 #we added something
            expanded_disk[i] = (-1, expanded_disk[i][1])
    i -= 1



checksum = 0
multiplier = 0
for file in expanded_disk:
    for i in range(file[1]):
        if file[0] != -1:
            checksum += multiplier * file[0]
        multiplier += 1
print(checksum)



