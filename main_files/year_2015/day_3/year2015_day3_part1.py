# --- Day 3: Perfectly Spherical Houses in a Vacuum ---
# Santa is delivering presents to an infinite two-dimensional grid of houses.
#
# He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls
# him via radio and tells him where to move next. Moves are always exactly one house to the north (^), south (v),
# east (>), or west (<). After each move, he delivers another present to the house at his new location.
#
# However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off,
# and Santa ends up visiting some houses more than once. How many houses receive at least one present?
#
# For example:
#
# - > delivers presents to 2 houses: one at the starting location, and one to the east.
# - ^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
# - ^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.


def calculate_num_of_houses() -> int:
    # read file
    with open('year2015_day3_challenge_input.txt', 'r', encoding='UTF-8') as f:
        input_string = f.read()

    # main function logic
    houses_dict = {'0, 0': 1}  # initial starting position of the Santa
    current_x_coordinate = 0
    current_y_coordinate = 0
    for direction in input_string:
        # change current coordinate
        if direction == '^':
            current_y_coordinate += 1
        elif direction == 'v':
            current_y_coordinate -= 1
        elif direction == '<':
            current_x_coordinate -= 1
        elif direction == '>':
            current_x_coordinate += 1

        # add to dictionary
        houses_dict[f'{current_x_coordinate}, {current_y_coordinate}'] = houses_dict.get(f'{current_x_coordinate}, '
                                                                                         f'{current_y_coordinate}',
                                                                                         0) + 1
    return len(houses_dict)


if __name__ == '__main__':
    result = calculate_num_of_houses()
    print(result)
