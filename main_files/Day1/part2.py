# --- Part Two ---
# The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation. They offer you a second one if you can find three numbers in your expense report that meet the same criteria.
#
# Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.
#
# In your expense report, what is the product of the three entries that sum to 2020?

from Challange1 import make_list_from_file
from itertools import combinations
from functools import reduce
from operator import mul

# A litte easier approach using libaries


def calculate_three():
    inputs = make_list_from_file('Challange_input.txt')
    for elements in combinations(inputs, 3):
        if sum(elements) == 2020:
            return reduce(mul, elements)

def main():
    value = calculate_three()
    print(value)

if __name__ == '__main__':
    main()