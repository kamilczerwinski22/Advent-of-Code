# --- Part Two --- Now, let's go the other way. In addition to finding the number of characters of code, you should
# now encode each code representation as a new string and find the number of characters of the new encoded
# representation, including the surrounding double quotes.
#
# For example:
#
# - "" encodes to "\"\"", an increase from 2 characters to 6.
# - "abc" encodes to "\"abc\"", an increase from 5 characters 9.
# - "aaa\"aaa" encodes to "\"aaa\\\"aaa\"", an increase from 10 characters to 16.
# - "\x27" encodes to "\"\\x27\"", an increase from 6 characters to 11. Your task is to find the total number of
# characters to represent the newly
# encoded strings minus the number of characters of code in each original string literal. For example,
# for the strings above, the total encoded length (6 + 9 + 16 + 11 = 42) minus the characters in the original code
# representation (23, just like in the first part of this puzzle) is 42 - 23 = 19.


def calculate_difference() -> int:
    # read file
    with open('year2015_day8_challenge_input.txt', 'r', encoding='UTF-8') as f:
        input_strings = f.read().splitlines()

    # main logic
    string_literals = 0
    string_values_longer = 0
    for seq in input_strings:
        string_literals += len(seq)
        # Python abuse :x (let's have some fun!)
        string_values_longer += len(seq.replace('\\', '\\\\').replace('"', '\\"')) + 2

    return string_values_longer - string_literals


if __name__ == '__main__':
    result = calculate_difference()
    print(result)
