# --- Part Two --- Realizing the error of his ways, Santa has switched to a better model of determining whether a
# string is naughty or nice. None of the old rules apply, as they are all clearly ridiculous.
#
# Now, a nice string is one with all of the following properties:
#
# - It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy)
# or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
# - It contains at least one letter which repeats with
# exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa. For example:
#
# - qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a letter that repeats with exactly one
# letter between them (zxz).
# - xxyxx is nice because it has a pair that appears twice and a letter that repeats with
# one between, even though the letters used by each rule overlap.
# - uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a single letter between them.
# - ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo), but no pair that appears
# twice.
# How many strings are nice under these new rules?


import re


def check_string(string: str) -> bool:
    pair_letter_rule = r'([a-z][a-z]).*\1'
    repeating_letter_rule = r'([a-z])[a-z]\1'
    return (re.search(pair_letter_rule, string) is not None) and (re.search(repeating_letter_rule, string) is not None)


def calculate_num_of_nice_strings() -> int:
    # read file
    with open('year2015_day5_challenge_input.txt', 'r', encoding='UTF-8') as f:
        words = f.read().splitlines()

    # main function logic
    num_of_nice_strings = 0
    for word in words:
        if check_string(word):
            num_of_nice_strings += 1

    return num_of_nice_strings


if __name__ == '__main__':
    result = calculate_num_of_nice_strings()
    print(result)
