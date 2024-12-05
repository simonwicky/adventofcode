#!/usr/bin/env python

"""
While the Elves get to work printing the correctly-ordered updates, you have a little time to fix the rest of them.

For each of the incorrectly-ordered updates, use the page ordering rules to put the page numbers in the right order. For the above example, here are the three incorrectly-ordered updates and their correct orderings:

75,97,47,61,53 becomes 97,75,47,61,53.
61,13,29 becomes 61,29,13.
97,13,75,29,47 becomes 97,75,47,29,13.
After taking only the incorrectly-ordered updates and ordering them correctly, their middle page numbers are 47, 29, and 47. Adding these together produces 123.

Find the updates which are not in the correct order. What do you get if you add up the middle page numbers after correctly ordering just those updates?
"""

def correct(ordering, rules):

    def inner(ordering):
        for i in range(1,len(ordering)):
            # if the set of element before x and rules[x] intersect, ordering is wrong
            intersection = set(ordering[:i]) & set(rules.get(ordering[i], set()))
            if len(intersection) != 0:
                current = ordering[i]
                to_move = [el for el in ordering if el in intersection]
                new_ordering = [el for el in ordering if el not in intersection]
                index = new_ordering.index(current)
                new_ordering = new_ordering[:index + 1] + to_move + new_ordering[index+1:]
                return inner(new_ordering)
            
            
                
        return ordering
    
    corrected_ordering = inner(ordering)
    #if it was correct already, skip it
    if corrected_ordering == ordering:
        return [0]
    return corrected_ordering

with open('input','r') as f:
    lines = f.read().splitlines()


split = lines.index("")
rules = [line.split("|") for line in lines[:split]]
orderings = [line.split(",") for line in lines[split+1:]]

#dictionnary of forbidden orderings
#forbidden[x] gives a set of element that can't appear before it
forbidden = {}
for rule in rules:
    if rule[0] not in forbidden:
         forbidden[rule[0]] = set()
    forbidden[rule[0]].add(rule[1])

total = 0
for ordering in orderings:
    correct_ordering = correct(ordering, forbidden)
    total += int(correct_ordering[len(correct_ordering) // 2])
    

print(total)

