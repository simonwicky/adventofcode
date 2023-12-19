#!/usr/bin/env python

"""
Even with your help, the sorting process still isn't fast enough.

One of the Elves comes up with a new plan: rather than sort parts individually through all of these workflows, maybe you can figure out in advance which combinations of ratings will be accepted or rejected.

Each of the four ratings (x, m, a, s) can have an integer value ranging from a minimum of 1 to a maximum of 4000. Of all possible distinct combinations of ratings, your job is to figure out which ones will be accepted.

In the above example, there are 167409079868000 distinct combinations of ratings that will be accepted.

Consider only your list of workflows; the list of part ratings that the Elves wanted you to sort is no longer relevant. How many distinct combinations of ratings will be accepted by the Elves' workflows?
"""
from functools import reduce

class Node():
	def __init__(self, cond, t,f):
		self.cond = cond
		self.t = t
		self.f = f

class Leaf():
	def __init__(self, accepted):
		self.accepted = accepted



def rules(lines):
	rules_dic = {}
	for line in lines:
		rule_name = line[:line.index("{")]
		rules_dic[rule_name] = line[line.index("{")+1:-1]

	return rules_dic

def build_tree(line):
	if ':' not in line:
		if len(line) == 1:
			return Leaf(line)
		else:
		 	return build_tree(rules[name])
	end = line.index(":")
	sep = line.index(",")

	cond = line[:end]
	t = line[end+1:sep]
	f = line[sep+1:]

	if len(t) > 1 and '<' not in t and '>' not in t:
		t = rules[t]

	if len(f) > 1 and '<' not in f and '>' not in f:
		f = rules[f]

	return Node(cond,build_tree(t), build_tree(f))



def count_accepted(node, parts):
	mapping = {'x' : 0, 'm': 1, 'a': 2, 's': 3}
	match node:
		case Leaf():
			if node.accepted == 'A':
				return reduce(lambda x, y : x * y, [rating[1] - rating[0] for rating in parts])
			return 0
		case Node():
			parts_t = [rating for rating in parts]
			parts_f = [rating for rating in parts]
			i = mapping[node.cond[0]]
			bound = int(node.cond[2:])
			if parts[i][0] <= bound < parts[i][1]:
				if node.cond[1] == '>':
					parts_t[i] = (bound + 1, parts[i][1])
					parts_f[i] = (parts[i][0], bound + 1)
				else :
					parts_t[i] = (parts[i][0], bound)
					parts_f[i] = (bound, parts[i][1])


			return count_accepted(node.t, parts_t) + count_accepted(node.f, parts_f)



with open('input','r') as f:
	lines = f.read().splitlines()

split = lines.index('')
rules = rules(lines[:split])
root = build_tree(rules['in'])

parts = [(1,4001),(1,4001),(1,4001),(1,4001)]


print(count_accepted(root, parts))
