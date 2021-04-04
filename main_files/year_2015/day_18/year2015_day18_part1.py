# --- Day 18: Like a GIF For Your Yard ---
# After the million lights incident, the fire code has gotten stricter: now, at most ten thousand lights are allowed.
# You arrange them in a 100x100 grid.
#
# Never one to let you down, Santa again mails you instructions on the ideal lighting configuration. With so few
# lights, he says, you'll have to resort to animation.
#
# Start by setting your lights to the included initial configuration (your puzzle input). A # means "on",
# and a . means "off".
#
# Then, animate your grid in steps, where each step decides the next configuration based on the current one. Each
# light's next state (either on or off) depends on its current state and the current states of the eight lights
# adjacent to it (including diagonals). Lights on the edge of the grid might have fewer than eight neighbors; the
# missing ones always count as "off".
#
# For example, in a simplified 6x6 grid, the light marked A has the neighbors numbered 1 through 8, and the light
# marked B, which is on an edge, only has the neighbors marked 1 through 5:
#
# 1B5...
# 234...
# ......
# ..123.
# ..8A4.
# ..765.
# The state a light should have next is based on its current state (on or off) plus the number of neighbors that are on:
#
# A light which is on stays on when 2 or 3 neighbors are on, and turns off otherwise.
# A light which is off turns on if exactly 3 neighbors are on, and stays off otherwise.
# All of the lights update simultaneously; they all consider the same current state before moving to the next.
#
# Here's a few steps from an example configuration of another 6x6 grid:
#
# Initial state:
# .#.#.#
# ...##.
# #....#
# ..#...
# #.#..#
# ####..
#
# After 1 step:
# ..##..
# ..##.#
# ...##.
# ......
# #.....
# #.##..
#
# After 2 steps:
# ..###.
# ......
# ..###.
# ......
# .#....
# .#....
#
# After 3 steps:
# ...#..
# ......
# ...#..
# ..##..
# ......
# ......
#
# After 4 steps:
# ......
# ......
# ..##..
# ..##..
# ......
# ......
# After 4 steps, this example has four lights on.
#
# In your grid of 100x100 lights, given your initial configuration, how many lights are on after 100 steps?


def calculate_lights_after_n_steps(n_steps: int) -> int:
    # prepare data. On == 1, off == 0 for convenient reasons
    with open('year2015_day18_challenge_input.txt', 'r') as f:
        grid_dim = len(f.readline()) - 1  # don't know if it's the fastest way yet

    grid = [[0] * (grid_dim + 2)]  # additional circumference with lights turned off to avoid try/except statements
    # grid.append([0] * (grid_dim + 2))
    with open('year2015_day18_challenge_input.txt', 'r') as f:
        for line in f.read().splitlines():
            current_line = [0] + [0 if element == '.' else 1 for element in line] + [0]  # create additional
            # circumference
            grid.append(current_line)
    grid.append([0] * (grid_dim + 2))  # additional circumference at the end

    # repeat n times
    for _ in range(n_steps):
        grid = single_step(grid, 1)

    # sum all turned on lights in result grid
    return sum(sum(row) for row in grid)


def single_step(input_grid: list, matrix_circumference: int) -> list:
    # circumference at the top
    new_grid = []
    for i in range(matrix_circumference):
        new_grid.append([0] * len(input_grid))

    # using only lights inside circumference
    for row in range(matrix_circumference, len(input_grid) - matrix_circumference):
        current_row = [0] * matrix_circumference  # circumference at the left
        for col in range(matrix_circumference, len(input_grid) - matrix_circumference):
            # check neighbours around
            neighbours_on = input_grid[row][col - 1] + \
                            input_grid[row][col + 1] + \
                            sum(input_grid[row - 1][col - 1:col + 2]) + \
                            sum(input_grid[row + 1][col - 1:col + 2])

            # conditions
            current_light = input_grid[row][col]
            if current_light == 1:
                if neighbours_on not in [2, 3]:
                    current_light = 0
            else:
                if neighbours_on == 3:
                    current_light = 1
            current_row.append(current_light)

        current_row += [0] * matrix_circumference  # circumference at the right
        new_grid.append(current_row)

    # circumference at the bottom
    for i in range(matrix_circumference):
        new_grid.append([0] * len(input_grid))

    return new_grid


if __name__ == '__main__':
    result = calculate_lights_after_n_steps(100)
    print(result)
