# --- Part Two --- The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa,
# to deliver presents with him.
#
# Santa and Robo-Santa start at the same location (delivering two presents to the same starting house),
# then take turns moving based on instructions from the elf, who is eggnoggedly reading from the same script as the
# previous year.
#
# This year, how many houses receive at least one present?
#
# For example:
#
# - ^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa goes south.
# - ^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back where they started.
# - ^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and Robo-Santa going the other.


def calculate_num_of_houses_robot() -> int:
    # read file
    with open('year2015_day3_challenge_input.txt', 'r', encoding='UTF-8') as f:
        input_string = f.read()

    # main function logic
    houses_dict = {'0, 0': 1}  # initial starting position of the Santa
    current_santa_x_coordinate = 0
    current_santa_y_coordinate = 0
    current_robot_x_coordinate = 0
    current_robot_y_coordinate = 0

    for idx, direction in enumerate(input_string):
        # depending on the index, gifts are distributed by different people
        if idx % 2 == 0:
            # Santa's coordinates
            if direction == '^':
                current_santa_y_coordinate += 1
            elif direction == 'v':
                current_santa_y_coordinate -= 1
            elif direction == '<':
                current_santa_x_coordinate -= 1
            elif direction == '>':
                current_santa_x_coordinate += 1
            houses_dict[f'{current_santa_x_coordinate}, {current_santa_y_coordinate}'] = \
                houses_dict.get(f'{current_santa_x_coordinate}, {current_santa_y_coordinate}', 0) + 1
        else:
            # Robot coordinates
            if direction == '^':
                current_robot_y_coordinate += 1
            elif direction == 'v':
                current_robot_y_coordinate -= 1
            elif direction == '<':
                current_robot_x_coordinate -= 1
            elif direction == '>':
                current_robot_x_coordinate += 1
            houses_dict[f'{current_robot_x_coordinate}, {current_robot_y_coordinate}'] = \
                houses_dict.get(f'{current_robot_x_coordinate}, {current_robot_y_coordinate}', 0) + 1

    return len(houses_dict)


if __name__ == '__main__':
    result = calculate_num_of_houses_robot()
    print(result)
