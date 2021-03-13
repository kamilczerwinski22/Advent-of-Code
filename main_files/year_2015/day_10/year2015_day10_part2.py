# --- Part Two --- Neat, right? You might also enjoy hearing John Conway talking about this sequence (that's Conway
# of Conway's Game of Life fame).
#
# Now, starting again with the digits in your puzzle input, apply this process 50 times. What is the length of the
# new result?


from itertools import groupby


def find_look_and_say_lenght(inp_str: str) -> int:
    prev_seq_value = inp_str
    for _ in range(50):
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
