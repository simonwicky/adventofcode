#!/usr/bin/env python

"""
Your cookie recipe becomes wildly popular! Someone asks if you can make another recipe that has exactly 500 calories per cookie (so they can use it as a meal replacement). Keep the rest of your award-winning process the same (100 teaspoons, same ingredients, same scoring system).

For example, given the ingredients above, if you had instead selected 40 teaspoons of butterscotch and 60 teaspoons of cinnamon (which still adds to 100), the total calorie count would be 40*8 + 60*3 = 500. The total score would go down, though: only 57600000, the best you can do in such trying circumstances.

Given the ingredients in your kitchen and their properties, what is the total score of the highest-scoring cookie you can make with a calorie total of 500?
"""

with open('input','r') as f:
    data = f.read().splitlines()

ingredients = []
for line in data:
    line_split = line.split(" ")
    ingredients += [[int(line_split[2][:-1]), int(line_split[4][:-1]), int(line_split[6][:-1]), int(line_split[8][:-1]), int(line_split[10])]]


highest_score = 0
for i in range(100):
    for j in range(100):
        for k in range(100):
            l = 100 - i - j - k
            if l < 0:
                continue
            capacity = i * ingredients[0][0] + j * ingredients[1][0] + k * ingredients[2][0] + l * ingredients[3][0]
            durability = i * ingredients[0][1] + j * ingredients[1][1] + k * ingredients[2][1] + l * ingredients[3][1]
            flavor = i * ingredients[0][2] + j * ingredients[1][2] + k * ingredients[2][2] + l * ingredients[3][2]
            texture = i * ingredients[0][3] + j * ingredients[1][3] + k * ingredients[2][3] + l * ingredients[3][3]
            calories = i * ingredients[0][4] + j * ingredients[1][4] + k * ingredients[2][4] + l * ingredients[3][4]
            if capacity < 0 or durability < 0 or flavor < 0 or texture < 0 :
                continue
            if calories != 500:
                continue
            highest_score = max(highest_score, capacity * durability * flavor * texture)

print(highest_score)