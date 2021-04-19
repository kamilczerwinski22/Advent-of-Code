# --- Part Two ---
# You finally arrive at the bathroom (it's a several minute walk from the lobby so visitors can behold the many fancy
# conference rooms and water coolers on this floor) and go to punch in the code. Much to your bladder's dismay,
# the keypad is not at all like you imagined it. Instead, you are confronted with the result of hundreds of man-hours
# of bathroom-keypad-design meetings:
#
#     1
#   2 3 4
# 5 6 7 8 9
#   A B C
#     D
# You still start at "5" and stop when you're at an edge, but given the same instructions as above, the outcome is very
# different:
#
# You start at "5" and don't move at all (up and left are both edges), ending at 5.
# Continuing from "5", you move right twice and down three times (through "6", "7", "B", "D", "D"), ending at D.
# Then, from "D", you move five more times (through "D", "B", "C", "C", "B"), ending at B.
# Finally, after five more moves, you end at 3.
# So, given the actual keypad layout, the code would be 5DB3.
#
# Using the same instructions in your puzzle input, what is the correct bathroom code?


def find_pin() -> str:
    # initial variables
    keypad = [['0', '0', '0', '0', '0', '0', '0'],
              ['0', '0', '0', '1', '0', '0', '0'],
              ['0', '0', '2', '3', '4', '0', '0'],
              ['0', '5', '6', '7', '8', '9', '0'],
              ['0', '0', 'A', 'B', 'C', '0', '0'],
              ['0', '0', '0', 'D', '0', '0', '0'],
              ['0', '0', '0', '0', '0', '0', '0']]  # imitate keypad with border made of '0's
    position_x, position_y = 3, 1  # starting at 5 on the keypad
    result_pin = ''

    # read input
    with open('year2016_day2_challenge_input.txt', 'r') as f:
        instructions = f.read().splitlines()

    # main function logic
    for seq in instructions:
        for direction in seq:
            # change current position on keypad if possible
            if direction == 'U':  # up
                if keypad[position_x - 1][position_y] != '0':
                    position_x -= 1
            elif direction == 'D':  # down
                if keypad[position_x + 1][position_y] != '0':
                    position_x += 1
            elif direction == 'R':  # right
                if keypad[position_x][position_y + 1] != '0':
                    position_y += 1
            elif direction == 'L':  # left
                if keypad[position_x][position_y - 1] != '0':
                    position_y -= 1

        result_pin += keypad[position_x][position_y]
    return result_pin


if __name__ == '__main__':
    result = find_pin()
    print(result)
