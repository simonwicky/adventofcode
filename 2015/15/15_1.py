#!/usr/bin/env python

"""
Today, you set out on the task of perfecting your milk-dunking cookie recipe. All you have to do is find the right balance of ingredients.

Your recipe leaves room for exactly 100 teaspoons of ingredients. You make a list of the remaining ingredients you could use to finish the recipe (your puzzle input) and their properties per teaspoon:

capacity (how well it helps the cookie absorb milk)
durability (how well it keeps the cookie intact when full of milk)
flavor (how tasty it makes the cookie)
texture (how it improves the feel of the cookie)
calories (how many calories it adds to the cookie)
You can only measure ingredients in whole-teaspoon amounts accurately, and you have to be accurate so you can reproduce your results in the future. The total score of a cookie can be found by adding up each of the properties (negative totals become 0) and then multiplying together everything except calories.

For instance, suppose you have these two ingredients:

Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
Then, choosing to use 44 teaspoons of butterscotch and 56 teaspoons of cinnamon (because the amounts of each ingredient must add up to 100) would result in a cookie with the following properties:

A capacity of 44*-1 + 56*2 = 68
A durability of 44*-2 + 56*3 = 80
A flavor of 44*6 + 56*-2 = 152
A texture of 44*3 + 56*-1 = 76
Multiplying these together (68 * 80 * 152 * 76, ignoring calories for now) results in a total score of 62842880, which happens to be the best score possible given these ingredients. If any properties had produced a negative total, it would have instead become zero, causing the whole score to multiply to zero.

Given the ingredients in your kitchen and their properties, what is the total score of the highest-scoring cookie you can make?
"""

#result is quite verbose and ugly but who cares

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
            if capacity < 0 or durability < 0 or flavor < 0 or texture < 0 :
                continue
            highest_score = max(highest_score, capacity * durability * flavor * texture)

print(highest_score)