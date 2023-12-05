#!/usr/bin/env python

"""
Everyone will starve if you only plant such a small number of seeds. Re-reading the almanac, it looks like the seeds: line actually describes ranges of seed numbers.

The values on the initial seeds: line come in pairs. Within each pair, the first value is the start of the range and the second value is the length of the range. So, in the first line of the example above:

seeds: 79 14 55 13
This line describes two ranges of seed numbers to be planted in the garden. The first range starts with seed number 79 and contains 14 values: 79, 80, ..., 91, 92. The second range starts with seed number 55 and contains 13 values: 55, 56, ..., 66, 67.

Now, rather than considering four seed numbers, you need to consider a total of 27 seed numbers.

In the above example, the lowest location number can be obtained from seed number 82, which corresponds to soil 84, fertilizer 84, water 84, light 77, temperature 45, humidity 46, and location 46. So, the lowest location number is 46.

Consider all of the initial seed numbers listed in the ranges on the first line of the almanac. What is the lowest location number that corresponds to any of the initial seed numbers?
"""


def read_mappings(lines):
	in_a_map = False
	mappings = {}
	lines += [''] #allow to disregard end cornercase
	for line in lines:
		if in_a_map and len(line) > 0:
			numbers = [int(i) for i in line.split(" ")]
			mapping += [numbers]
		if in_a_map and len(line) == 0:
			mappings[mapping_name] = mapping_range_fn(mapping)
			in_a_map = False
		if "map" in line:
			mapping_name = line.split(" ")[0]
			mapping = []
			in_a_map = True

	return mappings
			


def mapping_range_fn(numbers_list):
	def inner(lower_b, upper_b):
		for r in numbers_list:
			dst_start = r[0]
			src_start = r[1]
			range_len = r[2]
			if lower_b >= src_start and lower_b < src_start + range_len:
				l_b_mapping =  dst_start + lower_b - src_start

				if upper_b < src_start + range_len:
					u_b_mapping =  dst_start + upper_b - src_start
					return [(l_b_mapping, u_b_mapping)]
				else:
					return [(l_b_mapping, dst_start + range_len - 1)] + inner(src_start + range_len, upper_b)

		#corner case where lower bound is not mapped, but upper bound is
		for r in numbers_list:
			dst_start = r[0]
			src_start = r[1]
			range_len = r[2]
			if upper_b >= src_start and upper_b < src_start + range_len:
				u_b_mapping =  dst_start + upper_b - src_start
				return [(dst_start, u_b_mapping)] + inner(lower_b, src_start - 1)
		

		return [(lower_b, upper_b)]

	return inner




def read_seeds(nb_list):
	seeds = []
	for i in range(len(nb_list) // 2):
		seeds += [(nb_list[2 * i], nb_list[2 * i] + nb_list[2 * i + 1] - 1)]

	return seeds




with open("input",'r') as f:
	lines = f.read().splitlines()


mapping_order = ["seed-to-soil",
				"soil-to-fertilizer",
				"fertilizer-to-water",
				"water-to-light",
				"light-to-temperature",
				"temperature-to-humidity",
				"humidity-to-location"]
mappings = read_mappings(lines[2:])

seeds = [int(i) for i in lines[0].split(" ")[1:]]
seeds = read_seeds(seeds)


input_ranges = seeds


for mapping in mapping_order:
	output_ranges = []
	for seed_range in input_ranges:
		output_ranges += mappings[mapping](*seed_range)
	input_ranges = output_ranges


print(min(output_ranges)[0])
