#!/usr/bin/env python


def dst_sq(box_a: list[int], box_b : list[int]):
    return sum([(box_b[i]- box_a[i]) ** 2 for i in range(3)])

with open('input','r') as f:
    data = f.read().splitlines()

boxes: list[list[int]] = []
for line in data:
    boxes += [[int(c) for c in line.split(',')]]

# distances sorted
dst: list[list[int]] = []
for a in range(len(boxes)):
    for b in range(a+1, len(boxes)):
        dst += [[a,b,dst_sq(boxes[a], boxes[b])]]
dst.sort(key= lambda x : x[2])



circuits: list[list[int]] = []

last_connection = []
i = 0

# while we have no circuits or the first circuits doesn't contain everything
while len(circuits) == 0 or len(circuits[0]) != len(boxes):

    connection = dst[i][:2]
    index_a, index_b = -1, -1
    for j in range(len(circuits)):
        if connection[0] in circuits[j]:
            index_a = j
        if connection[1] in circuits[j]:
            index_b = j
    

    if index_a >= 0 and index_b >= 0 and index_a != index_b:
        #need to merge two circuits
        circuits[index_a] += circuits[index_b]
        del circuits[index_b]
    elif index_a >= 0 and index_b >= 0 and index_a == index_b:
        #in the same circuit, nothing to do
        pass
    elif index_a >= 0 and index_b == -1:
        # a in a circuit, not b
        circuits[index_a] += [connection[1]]
    elif index_b >= 0 and index_a == -1:
        # b in a circuit, not a
        circuits[index_b] += [connection[0]]
    elif index_a == -1 and index_b == -1:
        # not in a circuit at all
        circuits += [[connection[0], connection[1]]]

    
    i += 1
    last_connection = connection

print(boxes[last_connection[0]][0] * boxes[last_connection[1]][0])