# --- Part Two ---
# As a stress test on the system, the programs here clear the grid and then store the value 1 in square 1.
# Then, in the same allocation order as shown above, they store the sum of the values in all adjacent squares,
# including diagonals.
#
# So, the first few squares' values are chosen as follows:
#
# - Square 1 starts with the value 1.
# - Square 2 has only one adjacent filled square (with value 1), so it also stores 1.
# - Square 3 has both of the above squares as neighbors and stores the sum of their values, 2.
# - Square 4 has all three of the aforementioned squares as neighbors and stores the sum of their values, 4.
# - Square 5 only has the first and fourth squares as neighbors, so it gets the value 5.
#
# Once a square is written, its value does not change. Therefore, the first few squares would receive the following
# values:
#
# 147  142  133  122   59
# 304    5    4    2   57
# 330   10    1    1   54
# 351   11   23   25   26
# 362  747  806--->   ...
# What is the first value written that is larger than your puzzle input?

# ALGORITHMIC APPROACH: https://oeis.org/A141481


from itertools import count


def calculate_next_larger_value(number_to_check: int) -> int:
    # initial variables
    coordinates = [0, 0]
    coordinates_values_dict = {"0, 0": 1}

    # main logic
    direction = 1  # South = 0, East = 1, North = 2, West = 3
    line_len = 1
    for idx in count(start=1):
        # making new numbers
        for _ in range(line_len):
            if direction == 0:
                coordinates[0] += 1
            elif direction == 1:
                coordinates[1] += 1
            elif direction == 2:
                coordinates[0] -= 1
            elif direction == 3:
                coordinates[1] -= 1
            next_value = sum_neighbours(coordinates, coordinates_values_dict)
            coordinates_values_dict[f"{coordinates[0]}, {coordinates[1]}"] = next_value

            # check for larger value
            if next_value > number_to_check:
                return next_value

        # change line length and direction
        direction += 1
        # North-West transition
        if direction > 3:
            direction = 0

        if idx % 2 == 0:
            line_len += 1


def sum_neighbours(coords: list, values: dict) -> int:
    neighbours_sum = 0
    pos_x, pos_y = coords
    for i in range(-1, 2):
        neighbours_sum += values.get(f"{pos_x + i}, {pos_y - 1}", 0)
        neighbours_sum += values.get(f"{pos_x + i}, {pos_y}", 0)
        neighbours_sum += values.get(f"{pos_x + i}, {pos_y + 1}", 0)
    return neighbours_sum


if __name__ == '__main__':
    puzzle_input = 361527
    result = calculate_next_larger_value(puzzle_input)
    print(f"Next larger value is: {result}")
