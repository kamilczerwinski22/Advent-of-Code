# --- Day 3: Squares With Three Sides ---
# Now that you can think clearly, you move deeper into the labyrinth of hallways and office furniture that makes up
# this part of Easter Bunny HQ. This must be a graphic design department; the walls are covered in specifications for
# triangles.
#
# Or are they?
#
# The design document gives the side lengths of each triangle it describes, but... 5 10 25? Some of these aren't
# triangles. You can't help but mark the impossible ones.
#
# In a valid triangle, the sum of any two sides must be larger than the remaining side. For example, the "triangle"
# given above is impossible, because 5 + 10 is not larger than 25.
#
# In your puzzle input, how many of the listed triangles are possible?

import re


def find_num_of_valid_triangles() -> int:
    # read file
    with open('year2016_day3_challenge_input.txt', 'r') as f:
        triangles = [list(map(int, re.findall(r'\d+', seq))) for seq in f.read().splitlines()]

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
