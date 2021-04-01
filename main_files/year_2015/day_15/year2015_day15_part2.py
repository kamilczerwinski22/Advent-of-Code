# --- Part Two --- Your cookie recipe becomes wildly popular! Someone asks if you can make another recipe that has
# exactly 500 calories per cookie (so they can use it as a meal replacement). Keep the rest of your award-winning
# process the same (100 teaspoons, same ingredients, same scoring system).
#
# For example, given the ingredients above, if you had instead selected 40 teaspoons of butterscotch and 60 teaspoons
# of cinnamon (which still adds to 100), the total calorie count would be 40*8 + 60*3 = 500. The total score would go
# down, though: only 57600000, the best you can do in such trying circumstances.
#
# Given the ingredients in your kitchen and their properties, what is the total score of the highest-scoring cookie
# you can make with a calorie total of 500?


import re
from operator import mul
from functools import reduce


def calculate_perfect_proportions(total: int, max_calories: int) -> int:
    # read file
    ingredients = dict()
    with open('year2015_day15_challenge_input.txt', 'r', encoding='UTF-8') as f:
        for line in f.read().splitlines():
            ingredient_name, cookie_properties = line.split(':')
            ingredients[ingredient_name] = list(map(int, re.findall(r'-?\d+', cookie_properties)))  # last value is cal

    # main logic - generic solution
    recipe_scores = []
    for recipe in create_recipes(len(ingredients), total):
        current_recipe_values = [0] * (len(list(ingredients.values())[0]) - 1)  # num of each ingredient properties (4)
        current_calories = 0
        for spoons, ing_values in zip(recipe, ingredients.values()):
            current_calories += ing_values[-1] * spoons  # calories
            current_properties = [x * spoons for x in ing_values[:-1]]  # other properties
            # add current ingredient properties to current recipe properties
            current_recipe_values = [org + cur for org, cur in zip(current_recipe_values, current_properties)]

        # check if calories == max_calories
        if current_calories == max_calories:
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
    result = calculate_perfect_proportions(100, 500)
    print(result)
