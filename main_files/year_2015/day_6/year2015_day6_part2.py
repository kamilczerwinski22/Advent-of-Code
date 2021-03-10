# --- Part Two --- You just finish implementing your winning light pattern when you realize you mistranslated Santa's
# message from Ancient Nordic Elvish.
#
# The light grid you bought actually has individual brightness controls; each light can have a brightness of zero or
# more. The lights all start at zero.
#
# The phrase turn on actually means that you should increase the brightness of those lights by 1.
#
# The phrase turn off actually means that you should decrease the brightness of those lights by 1, to a minimum of zero.
#
# The phrase toggle actually means that you should increase the brightness of those lights by 2.
#
# What is the total brightness of all lights combined after following Santa's instructions?
#
# For example:
# - turn on 0,0 through 0,0 would increase the total brightness by 1.
# - toggle 0,0 through 999,999 would increase the total brightness by 2000000.


import re


def lights_brightness_manager() -> int:
    # initial variables
    grid_size = 1000
    lights_grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]  # 0/1 = off/on

    # read instructions file
    with open('year2015_day6_challenge_input.txt', 'r', encoding='UTF-8') as f:
        instructions = f.read().splitlines()

    # main function logic
    for instruction in instructions:
        row_start, col_start, row_end, col_end = [int(num) for num in re.findall(r'[0-9]+', instruction)]
        # toggle
        if 'toggle' in instruction:
            for row in range(row_start, row_end + 1):
                for col in range(col_start, col_end + 1):
                    lights_grid[row][col] += 2

        # turn on
        elif 'turn on' in instruction:
            for row in range(row_start, row_end + 1):
                for col in range(col_start, col_end + 1):
                    lights_grid[row][col] += 1

        # turn off
        elif 'turn off' in instruction:
            for row in range(row_start, row_end + 1):
                for col in range(col_start, col_end + 1):
                    if lights_grid[row][col] > 0:
                        lights_grid[row][col] -= 1

    return sum(map(sum, lights_grid))


if __name__ == '__main__':
    result = lights_brightness_manager()
    print(result)
