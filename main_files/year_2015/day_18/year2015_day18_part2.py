# --- Part Two ---
# You flip the instructions over; Santa goes on to point out that this is all just an implementation of
# Conway's Game of Life. At least, it was, until you notice that something's wrong with the grid of lights you bought:
# four lights, one in each corner, are stuck on and can't be turned off. The example above will actually run like this:
#
# Initial state:
# ##.#.#
# ...##.
# #....#
# ..#...
# #.#..#
# ####.#
#
# After 1 step:
# #.##.#
# ####.#
# ...##.
# ......
# #...#.
# #.####
#
# After 2 steps:
# #..#.#
# #....#
# .#.##.
# ...##.
# .#..##
# ##.###
#
# After 3 steps:
# #...##
# ####.#
# ..##.#
# ......
# ##....
# ####.#
#
# After 4 steps:
# #.####
# #....#
# ...#..
# .##...
# #.....
# #.#..#
#
# After 5 steps:
# ##.###
# .##..#
# .##...
# .##...
# #.#...
# ##...#
# After 5 steps, this example now has 17 lights on.
#
# In your grid of 100x100 lights, given your initial configuration, but with the four corners always in the on state,
# how many lights are on after 100 steps?


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
            current_light = input_grid[row][col]

            # check if current light is not in 'stuck lights' (4 corners that stays on included in list as tuples)
            if (row, col) in [(matrix_circumference, matrix_circumference),
                              (matrix_circumference, len(input_grid) - 2 * matrix_circumference),
                              (len(input_grid) - 2 * matrix_circumference, matrix_circumference),
                              (len(input_grid) - 2 * matrix_circumference, len(input_grid) - 2 * matrix_circumference)]:
                current_row.append(current_light)
                continue

            # check neighbours around
            neighbours_on = input_grid[row][col - 1] + \
                            input_grid[row][col + 1] + \
                            sum(input_grid[row - 1][col - 1:col + 2]) + \
                            sum(input_grid[row + 1][col - 1:col + 2])

            # conditions
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
