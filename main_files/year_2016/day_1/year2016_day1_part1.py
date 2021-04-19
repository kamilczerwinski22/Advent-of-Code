# --- Day 1: No Time for a Taxicab ---
# Santa's sleigh uses a very high-precision clock to guide its movements, and the clock's oscillator
# is regulated by stars. Unfortunately, the stars have been stolen... by the Easter Bunny. To save Christmas,
# Santa needs you to retrieve all fifty stars by December 25th.
#
# Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second
# puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!
#
# You're airdropped near Easter Bunny Headquarters in a city somewhere. "Near", unfortunately, is as close as you can
# get - the instructions on the Easter Bunny Recruiting Document the Elves intercepted start here, and nobody had
# time to work them out further.
#
# The Document indicates that you should start at the given coordinates (where you just landed) and face North. Then,
# follow the provided sequence: either turn left (L) or right (R) 90 degrees, then walk forward the given number of
# blocks, ending at a new intersection.
#
# There's no time to follow such ridiculous instructions on foot, though, so you take a moment and work out the
# destination. Given that you can only walk on the street grid of the city, how far is the shortest path to the
# destination?
#
# For example:
#
# Following R2, L3 leaves you 2 blocks East and 3 blocks North, or 5 blocks away.
# R2, R2, R2 leaves you 2 blocks due South of your starting position, which is 2 blocks away.
# R5, L5, R5, R3 leaves you 12 blocks away.
# How many blocks away is Easter Bunny HQ?


def simulate_road() -> int:
    # read file
    with open('year2016_day1_challenge_input.txt', 'r') as f:
        instructions = [seq.strip() for seq in f.read().split(',')]

    # simulation
    current_coordinates = [0, 0]
    direction = 0  # each number from 0 to 3 represents current direction

    # North = 0, East = 1, South = 2, West = 3
    for inst in instructions:
        current_direction, steps = inst[0], int(inst[1:])

        # change direction
        if current_direction == 'R':
            direction += 1
        elif current_direction == 'L':  # explicit
            direction -= 1

        # North-West transition
        if direction > 3:
            direction = 0
        elif direction < 0:
            direction = 3

        # update coordinates
        if direction == 0:  # go north
            current_coordinates[0] += steps
        elif direction == 1:  # go east
            current_coordinates[1] += steps
        elif direction == 2:  # go south
            current_coordinates[0] -= steps
        elif direction == 3:  # go west
            current_coordinates[1] -= steps

    return sum(abs(x) for x in current_coordinates)


if __name__ == '__main__':
    result = simulate_road()
    print(result)
