# --- Part Two ---
# The Elves decide they don't want to visit an infinite number of houses.
# Instead, each Elf will stop after delivering presents to 50 houses.
# To make up for it, they decide to deliver presents equal to eleven times their number at each house.
#
# With these changes, what is the new lowest house number of the house to get at least as many presents as the number
# in your puzzle input?

from sympy import divisors
from itertools import count


def calculate_house(target: int) -> int:
    for house in count(1):
        if sum(divisor * 11 for divisor in divisors(house) if divisor * 50 >= house) >= target:
            return house


if __name__ == '__main__':
    result = calculate_house(36000000)
    print(f"The result is {result} house")
