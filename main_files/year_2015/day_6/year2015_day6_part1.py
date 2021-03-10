# --- Day 6: Probably a Fire Hazard --- Because your neighbors keep defeating you in the holiday house decorating
# contest year after year, you've decided to deploy one million lights in a 1000x1000 grid.
#
# Furthermore, because you've been especially nice this year, Santa has mailed you instructions on how to display the
# ideal lighting configuration.
#
# Lights in your grid are numbered from 0 to 999 in each direction; the lights at each corner are at 0,0, 0,999, 999,
# 999, and 999,0. The instructions include whether to turn on, turn off, or toggle various inclusive ranges given as
# coordinate pairs. Each coordinate pair represents opposite corners of a rectangle, inclusive; a coordinate pair
# like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square. The lights all start turned off.
#
# To defeat your neighbors this year, all you have to do is set up your lights by doing the instructions Santa sent
# you in order.
#
# For example:
#
# - turn on 0,0 through 999,999 would turn on (or leave on) every light.
# - toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones that were on,
# and turning on the ones that were off.
# - turn off 499, 499 through 500,500 would turn off (or leave off) the middle four lights.
# After following the instructions, how many lights are lit?


import re


def lights_manager() -> int:
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
            for row_toggle in range(row_start, row_end + 1):
                for col_toggle in range(col_start, col_end + 1):
                    current_status = lights_grid[row_toggle][col_toggle]
                    if current_status:
                        lights_grid[row_toggle][col_toggle] = 0
                    else:
                        lights_grid[row_toggle][col_toggle] = 1

        # turn on
        elif 'turn on' in instruction:
            for row_on in range(row_start, row_end + 1):
                for col_on in range(col_start, col_end + 1):
                    lights_grid[row_on][col_on] = 1

        # turn off
        elif 'turn off' in instruction:
            for row_off in range(row_start, row_end + 1):
                for col_off in range(col_start, col_end + 1):
                    lights_grid[row_off][col_off] = 0

    return sum(map(sum, lights_grid))


if __name__ == '__main__':
    result = lights_manager()
    print(result)
