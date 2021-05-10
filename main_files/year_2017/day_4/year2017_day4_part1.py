# --- Day 4: High-Entropy Passphrases ---
# A new system policy has been put in place that requires all accounts to use a passphrase instead of simply a password.
# A passphrase consists of a series of words (lowercase letters) separated by spaces.
#
# To ensure security, a valid passphrase must contain no duplicate words.
#
# For example:
#
# - aa bb cc dd ee is valid.
# - aa bb cc dd aa is not valid - the word aa appears more than once.
# - aa bb cc dd aaa is valid - aa and aaa count as different words.
# The system's full passphrase list is available as your puzzle input. How many passphrases are valid?


def validate_phrases() -> int:
    # read file
    with open('year2017_day4_challenge_input.txt', 'r') as f:
        data = f.read().splitlines()

    # main logic
    valid_passphrases_num = 0
    for seq in data:
        phrase_list = seq.split(' ')
        if len(phrase_list) == len(set(phrase_list)):
            valid_passphrases_num += 1
    return valid_passphrases_num


if __name__ == '__main__':
    result = validate_phrases()
    print(f"Number of valid passphrases: {result}")
