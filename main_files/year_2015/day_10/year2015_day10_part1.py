# --- Day 10: Elves Look, Elves Say --- Today, the Elves are playing a game called look-and-say. They take turns
# making sequences by reading aloud the previous sequence and using that reading as the next sequence. For example,
# 211 is read as "one two, two ones", which becomes 1221 (1 2, 2 1s).
#
# Look-and-say sequences are generated iteratively, using the previous value as input for the next step. For each
# step, take the previous value, and replace each run of digits (like 111) with the number of digits (3) followed by
# the digit itself (1).
#
# For example:
#
# 1 becomes 11 (1 copy of digit 1).
# 11 becomes 21 (2 copies of digit 1).
# 21 becomes 1211 (one 2 followed by one 1).
# 1211 becomes 111221 (one 1, one 2, and two 1s).
# 111221 becomes 312211 (three 1s, two 2s, and one 1).
# Starting with the digits in your puzzle input, apply this process 40 times. What is the length of the result?


from itertools import groupby


def find_look_and_say_lenght(inp_str: str) -> int:
    prev_seq_value = inp_str
    for _ in range(40):
        # group sequence values in list separating them when the value changes, e.q. "1211" becomes ['1', '2', '11']
        current_seq_list = ["".join(grp) for _, grp in groupby(prev_seq_value)]

        # take element from list and connect it like (len)(single element), e.g. '111' is three ones, so: len = 3,
        # single element = 1; result: '111' -> '31'
        prev_seq_value = "".join(f"{len(value)}{value[0]}" for value in current_seq_list)
    return len(prev_seq_value)


if __name__ == '__main__':
    input_str = "1321131112"
    result = find_look_and_say_lenght(input_str)
    print(result)
