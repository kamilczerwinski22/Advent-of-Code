# --- Day 11: Corporate Policy ---
# Santa's previous password expired, and he needs help choosing a new one.
#
# To help him remember his new password after the old one expires, Santa has devised a method of coming up with a
# password based on the previous one. Corporate policy dictates that passwords must be exactly eight lowercase
# letters (for security reasons), so he finds his new password by incrementing his old password string repeatedly
# until it is valid.
#
# Incrementing is just like counting with numbers: xx, xy, xz, ya, yb, and so on. Increase the rightmost letter one
# step; if it was z, it wraps around to a, and repeat with the next letter to the left until one doesn't wrap around.
#
# Unfortunately for Santa, a new Security-Elf recently started, and he has imposed some additional password
# requirements:
#
# - Passwords must include one increasing straight of at least three letters, like abc, bcd, cde, and so on,
# up to xyz. They cannot skip letters; abd doesn't count.
# - Passwords may not contain the letters i, o, or l, as these letters can be mistaken for other characters and are
# therefore confusing.
# - Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb, or zz.
# For example:
#
# - hijklmmn meets the first requirement (because it contains the straight hij) but fails the second requirement
# requirement (because it contains i and l).
# - abbceffg meets the third requirement (because it repeats bb and ff) but fails the first requirement.
# - abbcegjk fails the third requirement, because it only has one double letter (bb).
# - The next password after abcdefgh is abcdffaa.
# - The next password after ghijklmn is ghjaabcc, because you eventually skip all the passwords that start with
# ghi..., since i is not allowed.
# Given Santa's current password (your puzzle input), what should his next password be?

import re
from string import ascii_lowercase


def generate_password(input_password: str) -> str:
    new_password = increment_password(input_password)
    while not validate(new_password):
        new_password = increment_password(new_password)
    return new_password


def increment_password(password: str) -> str:
    # find how many 'z' are at the end
    if password.endswith('z'):
        first_z_idx = password.index('z')  # find first 'z'
        num_of_z = len(password) - first_z_idx  # num of 'z'
        letter_to_change = password[first_z_idx - 1]  # find last letter in password which should be changed (not 'z')
        # remaining password + changed letter + 'a' times number of 'z' in the input password
        return password[:first_z_idx - 1] + generate_next_letter(letter_to_change) + 'a' * num_of_z
    else:
        return password[:-1] + generate_next_letter(password[-1])


def generate_next_letter(char: str) -> str:
    return ascii_lowercase[(ascii_lowercase.index(char) + 1) % len(ascii_lowercase)]


def validate(input_password: str) -> bool:
    # Requirement 2 (fastest to check)
    if re.search(r'(\w)\1.*\1', input_password):
        return False

    # Requirement 2
    if not re.search(r'(\w)\1.*(\w)\2', input_password):
        return False

    # Requirement 1 (e.g. 'abc' will be present in 'abcdefg...')
    for idx in range(len(input_password) - 2):
        if input_password[idx: idx + 3] in ascii_lowercase:
            return True
    else:
        return False


if __name__ == '__main__':
    main_password = "hepxcrrq"  # my input password
    result = generate_password(main_password)
    print(f"Next password is: {result}")
    next_result = generate_password(result)
    print(f"Future next password is: {next_result}")
