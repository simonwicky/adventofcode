#!/usr/bin/env python


## as it turns out, the problem is easy, because either the matrix can't contain all shapes because it has less spaces than required
## or it waaaaay enough space that how you pack them doesn't even matter
## thus it's just about checking that the given grid can accommodate everything

with open('input','r') as f:
    data = f.read().splitlines()


# Shape size parsing
shape_size: list[int] = []
i = 0
shape_index = 0
while data[i] == str(shape_index) + ":":
    shape_size += [(data[i+1] + data[i+2] + data[i+3]).count("#")]
    i += 5
    shape_index += 1



problems = data[i:]

total = 0
for line in problems:
    line = line.split()

    # Parsing height and width
    height = int(line[0][:-1].split("x")[0])
    width = int(line[0][:-1].split("x")[1])
    shapes = [int(c) for c in line[1:]]


    total_size_shapes = sum([shape_size[i] * shapes[i] for i in range(len(shapes))])

    # if the grid is bigger than all the presents
    if height * width > total_size_shapes:
        total += 1



print(total)