# --- Part Two ---
# Now that you've helpfully marked up their design documents, it occurs to you that triangles are specified in groups
# of three vertically. Each set of three numbers in a column specifies a triangle. Rows are unrelated.
#
# For example, given the following specification, numbers with the same hundreds digit would be part of the
# same triangle:
#
# 101 301 501
# 102 302 502
# 103 303 503
# 201 401 601
# 202 402 602
# 203 403 603
# In your puzzle input, and instead reading by columns, how many of the listed triangles are possible?

import re


def find_num_of_valid_triangles() -> int:
    # read file
    with open('year2016_day3_challenge_input.txt', 'r') as f:
        triangles = []
        temp_data = []

        # every 3 lines, transpose and add to main data list
        for idx, line in enumerate([list(map(int, re.findall(r'\d+', seq))) for seq in f.read().splitlines()], 1):
            temp_data.append(line)
            if idx % 3 == 0:
                triangles += [list(a) for a in zip(*temp_data)]
                temp_data.clear()

    # main logic - find all triangles
    counter = 0
    for triangle in triangles:  # check if largest number is less that the sum of the other two
        max_value = triangle.pop(triangle.index(max(triangle)))
        if max_value < sum(triangle):
            counter += 1

    return counter


if __name__ == '__main__':
    result = find_num_of_valid_triangles()
    print(result)
