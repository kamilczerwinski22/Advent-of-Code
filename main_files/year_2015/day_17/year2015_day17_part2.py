# --- Part Two ---
# While playing with all the containers in the kitchen, another load of eggnog arrives!
# The shipping and receiving department is requesting as many containers as you can spare.
#
# Find the minimum number of containers that can exactly fit all 150 liters of eggnog. How many different ways can
# you fill that number of containers and still hold exactly 150 litres?
#
# In the example above, the minimum number of containers was two. There were three ways to use that many containers,
# and so the answer there would be 3.


from itertools import combinations


def prepare_data() -> list:
    # read file
    with open('year2015_day17_challenge_input.txt', 'r') as f:
        values = list(map(int, f.read().splitlines()))
    return values


def find_num_of_fitting(containers: list, sum_to_find: int) -> int:
    for i in range(len(containers)):
        sub_total = 0
        for comb in combinations(containers, i):
            if sum(comb) == sum_to_find:
                sub_total += 1
        if sub_total > 0:
            return sub_total


if __name__ == '__main__':
    data = prepare_data()
    result = find_num_of_fitting(data, 150)
    print(result)
