# --- Day 17: No Such Thing as Too Much ---
# The elves bought too much eggnog again - 150 liters this time. To fit it all into your refrigerator,
# you'll need to move it into smaller containers. You take an inventory of the capacities of the available containers.
#
# For example, suppose you have containers of size 20, 15, 10, 5, and 5 liters. If you need to store 25 liters,
# there are four ways to do it:
#
# - 15 and 10
# - 20 and 5 (the first 5)
# - 20 and 5 (the second 5)
# - 15, 5, and 5
# Filling all containers entirely, how many different combinations of containers can exactly fit all 150
# liters of eggnog?


from itertools import combinations


def prepare_data() -> list:
    # read file
    with open('year2015_day17_challenge_input.txt', 'r') as f:
        values = list(map(int, f.read().splitlines()))
    return values


def find_num_of_fitting(containers: list, sum_to_find: int) -> int:
    total = 0
    for i in range(len(containers)):
        for comb in combinations(containers, i):
            if sum(comb) == sum_to_find:
                total += 1
    return total


if __name__ == '__main__':
    data = prepare_data()
    result = find_num_of_fitting(data, 150)
    print(result)
