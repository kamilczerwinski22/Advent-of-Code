# --- Part Two ---
# Of course, that would be the message - if you hadn't agreed to use a modified repetition code instead.
#
# In this modified code, the sender instead transmits what looks like random data, but for each character,
# the character they actually want to send is slightly less likely than the others. Even after signal-jamming
# noise, you can look at the letter distributions in each column and choose the least common letter to reconstruct
# the original message.
#
# In the above example, the least common character in the first column is a; in the second, d, and so on.
# Repeating this process for the remaining characters produces the original message, advent.
#
# Given the recording in your puzzle input and this new decoding methodology, what is the original message
# that Santa is trying to send?

from collections import Counter


def recover_message() -> str:
    # read file, prepare data
    with open('year2016_day6_challenge_input.txt', 'r') as f:
        data = zip(*f.read().splitlines())

    # find least common, then extract from tuple
    return "".join(Counter(seq).most_common()[-1][0] for seq in data)


if __name__ == '__main__':
    result = recover_message()
    print(f"Recovered message: {result}")
