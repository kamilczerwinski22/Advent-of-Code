# --- Part Two ---
# You notice a progress bar that jumps to 50% completion. Apparently, the door isn't yet satisfied, but it did emit a
# star as encouragement. The instructions change:
#
# Now, instead of considering the next digit, it wants you to consider the digit halfway around the circular list.
# That is, if your list contains 10 items, only include a digit in your sum if the digit 10/2 = 5 steps forward
# matches it. Fortunately, your list has an even number of elements.
#
# For example:
#
# - 1212 produces 6: the list contains 4 items, and all four digits match the digit 2 items ahead.
# - 1221 produces 0, because every comparison is between a 1 and a 2.
# - 123425 produces 4, because both 2s match each other, but no other digit has a match.
# - 123123 produces 12.
# - 12131415 produces 4.
# What is the solution to your new captcha?


def solve_captcha() -> int:
    # read sequence and prepare data
    with open('year2017_day1_challenge_input.txt', 'r') as f:
        sequence = [int(dig) for dig in f.read()]

    # main function logic
    list_of_digits = []
    len_of_seq = len(sequence)
    for idx, digit in enumerate(sequence):
        if digit == sequence[(idx + (len_of_seq // 2)) % len_of_seq]:
            list_of_digits.append(digit)

    return sum(list_of_digits)


if __name__ == '__main__':
    result = solve_captcha()
    print(f"Result is {result}")
