# --- Day 3: Spiral Memory ---
# You come across an experimental new kind of memory stored on an infinite two-dimensional grid.
#
# Each square on the grid is allocated in a spiral pattern starting at a location marked 1 and then counting up while
# spiraling outward. For example, the first few squares are allocated like this:
#
# 17  16  15  14  13 18   5   4   3  12 19   6   1   2  11 20   7   8   9  10 21  22  23---> ... While this is very
# space-efficient (no squares are skipped), requested data must be carried back to square 1 (the location of the only
# access port for this memory system) by programs that can only move up, down, left, or right. They always take the
# shortest path: the Manhattan Distance between the location of the data and square 1.
#
# For example:
#
# - Data from square 1 is carried 0 steps, since it's at the access port.
# - Data from square 12 is carried 3 steps, such as: down, left, left.
# - Data from square 23 is carried only 2 steps: up twice.
# - Data from square 1024 must be carried 31 steps.
#
# How many steps are required to carry the data from the square identified in your puzzle input all the way to the
# access port?

from math import ceil, sqrt


def calculate_distance(number_to_check: int) -> int:
    # initial variables
    full_power = ceil(sqrt(number_to_check))
    if full_power % 2 == 0:
        full_power += 1
    full_power_distance = full_power ** 2 - number_to_check

    # main logic - algorithmic approach for best time complexity
    if full_power_distance < full_power:  # bottom wall
        coordinates = [(full_power - 1) // 2, ((full_power - 1) // 2) - (full_power_distance % (full_power - 1))]

    elif full_power_distance < full_power * 2 - 1:  # left wall
        coordinates = [((full_power - 1) // 2) - (full_power_distance % (full_power - 1)), -((full_power - 1) // 2)]

    elif full_power_distance < full_power * 3 - 2:  # up wall
        coordinates = [(full_power - 1) // 2, -((full_power - 1) // 2) + (full_power_distance % (full_power - 1))]

    else:  # right wall
        coordinates = [-((full_power - 1) // 2) + (full_power_distance % (full_power - 1)), (full_power - 1) // 2]

    return sum(abs(x) for x in coordinates)


if __name__ == '__main__':
    puzzle_input = 361527
    result = calculate_distance(puzzle_input)
    print(f"Distance is: {result}")
