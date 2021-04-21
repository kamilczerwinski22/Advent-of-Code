# --- Day 7: Internet Protocol Version 7 ---
# While snooping around the local network of EBHQ, you compile a list of IP addresses (they're IPv7, of course;
# IPv6 is much too limited). You'd like to figure out which IPs support TLS (transport-layer snooping).
#
# An IP supports TLS if it has an Autonomous Bridge Bypass Annotation, or ABBA. An ABBA is any four-character
# sequence which consists of a pair of two different characters followed by the reverse of that pair, such as xyyx or
# abba. However, the IP also must not have an ABBA within any hypernet sequences, which are contained by square
# brackets.
#
# For example:
#
# - abba[mnop]qrst supports TLS (abba outside square brackets).
# - abcd[bddb]xyyx does not support TLS (bddb is within square brackets, even though xyyx is outside square brackets).
# - aaaa[qwer]tyui does not support TLS (aaaa is invalid; the interior characters must be different).
# - ioxxoj[asdfgh]zxcvbn supports TLS (oxxo is outside square brackets, even though it's within a larger string).

# How many IPs in your puzzle input support TLS?

import re


def abba_checker(sequence: str) -> bool:
    for i in range(len(sequence) - 3):  # slice and check every 4 consecutive letters combination inside
        left = sequence[i:i + 2]
        right = sequence[i + 2:i + 4]

        if left == right[::-1]:  # check if reversed is the same ('ab' == 'ba')
            if left != right:  # check if the interior characters are different
                return True

    return False


def check_handler(sequence: list) -> bool:
    for seq in sequence:
        if abba_checker(seq):
            return True
    return False


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

        # if ABBA inside brackets and outside brackets
        if not check_handler(inside_brackets) and check_handler(outside_brackets):
            supporting_ips_num += 1

    return supporting_ips_num


if __name__ == '__main__':
    result = check_ips()
    print(f"{result} IPs support TLS")
