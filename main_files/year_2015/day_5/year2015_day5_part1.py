# --- Day 5: Doesn't He Have Intern-Elves For This? ---
# Santa needs help figuring out which strings in his text file are naughty or nice.
#
# A nice string is one with all of the following properties:
#
# - It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
# - It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
# - It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
# For example:
#
# - ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...),
# and none of the disallowed substrings.
# - aaa is nice because it has at least three vowels and a double letter,
# even though the letters used by different rules overlap.
# - jchzalrnumimnmhp is naughty because it has no double
# letter.
# - haegwjzuvuyypxyu is naughty because it contains the string xy. dvszwmarrgswjxmb is naughty because it
# contains only one vowel. How many strings are nice?


def check_string(string: str) -> bool:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    prohibited_strings = {"ab", "cd", "pq", "xy"}
    num_of_vowels = 0
    double_letters = False
    prev_element = None
    for char in string:
        if char in vowels:
            num_of_vowels += 1

        if prev_element is None:
            prev_element = char
            continue

        if prev_element == char:
            double_letters = True

        if prev_element + char in prohibited_strings:
            return False
        prev_element = char

    return num_of_vowels > 2 and double_letters


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
