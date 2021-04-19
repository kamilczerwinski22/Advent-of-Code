# --- Part Two ---
# Then, you notice the instructions continue on the back of the Recruiting Document.
# Easter Bunny HQ is actually at the first location you visit twice.
#
# For example, if your instructions are R8, R4, R4, R8, the first location you visit twice is 4 blocks away, due East.
#
# How many blocks away is the first location you visit twice?


def simulate_road() -> int:
    # read file
    with open('year2016_day1_challenge_input.txt', 'r') as f:
        instructions = [seq.strip() for seq in f.read().split(',')]

    # simulation
    current_coordinates = [0, 0]
    direction = 0  # each number from 0 to 3 represents current direction
    all_visited_locations = set()

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

        # go to location step by step
        for i in range(steps):
            # update coordinates
            if direction == 0:  # go north
                current_coordinates[0] += 1
            elif direction == 1:  # go east
                current_coordinates[1] += 1
            elif direction == 2:  # go south
                current_coordinates[0] -= 1
            elif direction == 3:  # go west
                current_coordinates[1] -= 1

            # save all visited locations and return fist location visited twice
            coordinates_tuple = tuple(current_coordinates)  # tuple cuz needs to be hashable
            if coordinates_tuple in all_visited_locations:
                return sum(abs(x) for x in coordinates_tuple)
            else:
                all_visited_locations.add(coordinates_tuple)


if __name__ == '__main__':
    result = simulate_road()
    print(result)
