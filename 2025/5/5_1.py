#!/usr/bin/env python

with open('input','r') as f:
    data = f.read().splitlines()


def is_fresh(fresh_ids, ingredient_id):
    for id_range in fresh_ids:
        if ingredient_id >= id_range[0] and ingredient_id <= id_range[1]:
            return True

    return False

fresh_ids = []

i = 0
while data[i] != '':
    lower_bound = data[i].split("-")[0]
    upper_bound = data[i].split("-")[1]
    fresh_ids += [(int(lower_bound), int(upper_bound))]
    i += 1

available_ids = []
for line in data[i+1:]:
    available_ids += [int(line)]


nb_fresh = 0
for ingredient_id in available_ids:
    if is_fresh(fresh_ids, ingredient_id):
        nb_fresh += 1

print(nb_fresh)