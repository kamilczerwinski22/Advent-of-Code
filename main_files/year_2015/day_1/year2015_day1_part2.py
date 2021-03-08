# --- Part Two --- Now, given the same instructions, find the position of the first character that causes him to
# enter the basement (floor -1). The first character in the instructions has position 1, the second character has
# position 2, and so on.
#
# For example:
#
# ) causes him to enter the basement at character position 1.
# ()()) causes him to enter the basement at character position 5.
# What is the position of the character that causes Santa to first enter the basement?


def calculate_first_basement_position() -> int:
    # open file and parse it to string
    with open('year2015_day1_challenge_input.txt', 'r+', encoding='UTF-8') as f:
        input_string = f.read()

    # main function logic
    current_floor = 0
    num_of_parenthesis = 0
    while True:
        for char in input_string:
            if char == '(':
                current_floor += 1
            else:
                current_floor -= 1
            num_of_parenthesis += 1

            if current_floor < 0:
                return num_of_parenthesis


if __name__ == '__main__':
    result = calculate_first_basement_position()
    print(result)
