# --- Part Two ---
# While it appears you validated the passwords correctly, they don't seem to be what the Official Toboggan Corporate Authentication System is expecting.
#
# The shopkeeper suddenly realizes that he just accidentally explained the password policy rules from his old job at the sled rental place down the street! The Official Toboggan Corporate Policy actually works a little differently.
#
# Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.
#
# Given the same example list from above:
#
# 1-3 a: abcde is valid: position 1 contains a and position 3 does not.
# 1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
# 2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
# How many passwords are valid according to the new interpretation of the policies?

from day2_part1_password_philosophy import make_dict_from_file

def validate_occurencies_positions(dic: dict) -> int:
    counter = 0
    for idx, password_dict in dic.items():  # idx is needed for dic keys not to overlap
        password = "".join(password_dict.keys())
        restrictions = dict(*password_dict.values())
        char = "".join(restrictions.keys())

        # int - 1 cuz we need index, and comapny is using "no 0 index policy"
        first_occurence, second_occurence = [int(x) - 1 for x in "".join(restrictions.values()).split('-')]

        # print(f"{idx} Hasło: {password}, with {first_occurence} to {second_occurence} occurencies of char {char}")
        try:  # long if, ik
            if (password[first_occurence] == char and password[second_occurence] != char) or \
                    (password[first_occurence] != char and password[second_occurence] == char):
                counter += 1
        except IndexError:  # if second occurence is out of range, and first is correct
            if password[first_occurence] == char:
                counter += 1
    return counter

def main():
    passwords = make_dict_from_file('year2020_day2_challenge_input.txt')
    print(validate_occurencies_positions(passwords))

if __name__ == '__main__':
    main()