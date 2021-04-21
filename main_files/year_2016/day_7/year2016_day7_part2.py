# --- Part Two ---
# You would also like to know which IPs support SSL (super-secret listening).
#
# An IP supports SSL if it has an Area-Broadcast Accessor, or ABA, anywhere in the supernet sequences (outside any
# square bracketed sections), and a corresponding Byte Allocation Block, or BAB, anywhere in the hypernet sequences.
# An ABA is any three-character sequence which consists of the same character twice with a different character
# between them, such as xyx or aba. A corresponding BAB is the same characters but in reversed positions: yxy and
# bab, respectively.
#
# For example:
#
# - aba[bab]xyz supports SSL (aba outside square brackets with corresponding bab within square brackets).
# - xyx[xyx]xyx does not support SSL (xyx, but no corresponding yxy).
# - aaa[kek]eke supports SSL (eke in supernet with corresponding kek in hypernet; the aaa sequence is not related,
# because the interior character must be different).
# - zazbz[bzb]cdb supports SSL (zaz has no corresponding aza, but zbz has a corresponding bzb, even though zaz and zbz
# overlap).
# How many IPs in your puzzle input support SSL?

import re


def ssl_checker(inside_brackets: list, outside_brackets: list) -> bool:
    inside_brackets_sequences = set()
    outside_brackets_sequences = set()

    # standard ABA check
    for in_element in inside_brackets:
        for i in range(len(in_element) - 2):
            left, middle, right = in_element[i], in_element[i + 1], in_element[i + 2]
            if left == right:
                inside_brackets_sequences.add(left + middle + right)

    # BAB check with conversion to ABA convention
    for out_element in outside_brackets:
        for j in range(len(out_element) - 2):
            left, middle, right = out_element[j], out_element[j + 1], out_element[j + 2]
            if left == right:
                outside_brackets_sequences.add(middle + left + middle)
    # check if any elements inside brackets are opposite to elements outside brackets
    return bool(inside_brackets_sequences.intersection(outside_brackets_sequences))


def check_ips() -> int:
    # read file
    with open('year2016_day7_challenge_input.txt', 'r') as f:
        raw_data = f.read().splitlines()

    # main function logic
    supporting_ips_num = 0
    for ip in raw_data:
        inside_brackets = re.findall(r'\[(.*?)\]', ip)

        # outside brackets
        for element in inside_brackets:
            ip = ip.replace(f"[{element}]", ';')
        outside_brackets = ip.split(';')

        # check if IP supports SSL
        if ssl_checker(inside_brackets, outside_brackets):
            supporting_ips_num += 1

    return supporting_ips_num


if __name__ == '__main__':
    result = check_ips()
    print(f"{result} IPs support SSL")
