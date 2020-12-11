# --- Day 2: Password Philosophy ---
# Your flight departs in a few days from the coastal airport; the easiest way down to the coast from here is via toboggan.
#
# The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day. "Something's wrong with our computers; we can't log in!" You ask if you can take a look.
#
# Their password database seems to be a little corrupted: some of the passwords wouldn't have been allowed by the Official Toboggan Corporate Policy that was in effect when they were chosen.
#
# To try to debug the problem, they have created a list (your puzzle input) of passwords (according to the corrupted database) and the corporate policy when that password was set.
#
# For example, suppose you have the following list:
#
# 1-3 a: abcde
# 1-3 b: cdefg
# 2-9 c: ccccccccc
# Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.
#
# In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b, but needs at least 1. The first and third passwords are valid: they contain one a or nine c, both within the limits of their respective policies.
#
# How many passwords are valid according to their policies?



def make_dict_from_file(file_name: str) -> dict:
    """Return triple nested dictionary, as {idx: {password: {char, num_of_occurencies}}}"""
    inputs = dict()
    with open(file_name, 'r+', encoding="UTF-8") as f:
        for idx, line in enumerate(f.readlines()):
            occurencies, password = line.split(':')
            num, char = occurencies.split(' ')
            inputs[idx] = {password.strip(): {char: num}}
            # print(f"{idx} {line.strip()}")
    return inputs

def validate_occurencies_number(dic: dict) -> int:
    counter = 0
    for idx, password_dict in dic.items():  # idx is needed for dic keys not to overlap
        password = "".join(password_dict.keys())
        restrictions = dict(*password_dict.values())
        char = "".join(restrictions.keys())
        minimum, maximum = [int(x) for x in "".join(restrictions.values()).split('-')]
        if maximum >= password.count(char) >= minimum:
            counter += 1
        # print(f"{counter} Hasło: {password}, with {minimum} to {maximum} occurencies of char {char}")
    return counter

def main():
    passwords = make_dict_from_file('Challange_input.txt')
    print(validate_occurencies_number(passwords))

if __name__ == '__main__':
    main()