# --- Day 15: Science for Hungry People --- Today, you set out on the task of perfecting your milk-dunking cookie
# recipe. All you have to do is find the right balance of ingredients.
#
# Your recipe leaves room for exactly 100 teaspoons of ingredients. You make a list of the remaining ingredients you
# could use to finish the recipe (your puzzle input) and their properties per teaspoon:
#
# - capacity (how well it helps the cookie absorb milk)
# - durability (how well it keeps the cookie intact when full of milk)
# - flavor (how tasty it makes the cookie)
# - texture (how it improves the feel of the cookie)
# - calories (how many calories it adds to the cookie)
# You can only measure ingredients in whole-teaspoon amounts accurately, and you have to be accurate so you can
# reproduce your results in the future. The total score of a cookie can be found by adding up each of the properties (
# negative totals become 0) and then multiplying together everything except calories.
#
# For instance, suppose you have these two ingredients:
#
# Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8 Cinnamon: capacity 2, durability 3,
# flavor -2, texture -1, calories 3 Then, choosing to use 44 teaspoons of butterscotch and 56 teaspoons of cinnamon (
# because the amounts of each ingredient must add up to 100) would result in a cookie with the following properties:
#
# - A capacity of 44*-1 + 56*2 = 68
# - A durability of 44*-2 + 56*3 = 80
# - A flavor of 44*6 + 56*-2 = 152
# - A texture of 44*3 + 56*-1 = 76
# Multiplying these together (68 * 80 * 152 * 76, ignoring calories for now) results in a total score of 62842880,
# which happens to be the best score possible given these ingredients. If any properties had produced a negative
# total, it would have instead become zero, causing the whole score to multiply to zero.
#
# Given the ingredients in your kitchen and their properties, what is the total score of the highest-scoring cookie
# you can make?

import re
from operator import mul
from functools import reduce


def calculate_perfect_proportions(total: int) -> int:
    # read file
    ingredients = dict()
    with open('year2015_day15_challenge_input.txt', 'r', encoding='UTF-8') as f:
        for line in f.read().splitlines():
            ingredient_name, cookie_properties = line.split(':')
            ingredients[ingredient_name] = list(map(int, re.findall(r'-?\d+', cookie_properties)))[:-1]  # skip calories

    # main logic - generic solution
    recipe_scores = []
    for recipe in create_recipes(len(ingredients), total):
        current_recipe_values = [0] * len(list(ingredients.values())[0])  # num of each ingredient properties (4)
        for spoons, ing_values in zip(recipe, ingredients.values()):
            current_properties = [x * spoons for x in ing_values]
            # add current ingredient properties to current recipe properties
            current_recipe_values = [org + cur for org, cur in zip(current_recipe_values, current_properties)]

        # check if all values in current_recipe_values are greater than 0, if yes - get product of them, else add 0
        recipe_scores.append(reduce(mul, current_recipe_values) if all(x > 0 for x in current_recipe_values) else 0)
    return max(recipe_scores)


def create_recipes(n: int, total: int):
    start = total if n == 1 else 0  # start with 0 if dim > 1

    for i in range(start, total + 1):
        left_side = total - i  # left side to sum to calculate last element
        if n - 1 != 0:  # if dim > 1
            for y in create_recipes(n - 1, left_side):  # if dim > 1 go deeper
                yield [i] + y
        else:
            yield [i]  # return last digit as list


if __name__ == '__main__':
    result = calculate_perfect_proportions(100)
    print(result)
