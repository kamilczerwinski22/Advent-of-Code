# --- Part Two ---
# For added security, yet another system policy has been put in place. Now, a valid passphrase must contain no
# two words that are anagrams of each other - that is, a passphrase is invalid if any word's letters can be rearranged
# to form any other word in the passphrase.
#
# For example:
#
# - abcde fghij is a valid passphrase.
# - abcde xyz ecdab is not valid - the letters from the third word can be rearranged to form the first word.
# - a ab abc abd abf abj is a valid passphrase, because all letters need to be used when forming another word.
# - iiii oiii ooii oooi oooo is valid.
# - oiii ioii iioi iiio is not valid - any of these words can be rearranged to form any other word.
#
# Under this new system policy, how many passphrases are valid?


from collections import Counter


def validate_phrases() -> int:
    # read file
    with open('year2017_day4_challenge_input.txt', 'r') as f:
        data = f.read().splitlines()

    # main logic
    valid_passphrases_num = 0
    for line in data:
        if check_for_rearranged_words(line):
            valid_passphrases_num += 1

    return valid_passphrases_num


def check_for_rearranged_words(line: str) -> bool:
    prepared_data = [Counter(word) for word in line.split(' ')]
    for i in range(len(prepared_data)):
        if prepared_data[i] in (prepared_data[:i] + prepared_data[i + 1:]):
            return False
    return True


if __name__ == '__main__':
    result = validate_phrases()
    print(f"Number of valid passphrases: {result}")
