# --- Day 12: JSAbacusFramework.io --- Santa's Accounting-Elves need help balancing the books after a recent order.
# Unfortunately, their accounting software uses a peculiar storage format. That's where you come in.
#
# They have a JSON document which contains a variety of things: arrays ([1,2,3]), objects ({"a":1, "b":2}), numbers,
# and strings. Your first job is to simply find all of the numbers throughout the document and add them together.
#
# For example:
#
# [1,2,3] and {"a":2,"b":4} both have a sum of 6.
# [[[3]]] and {"a":{"b":4},"c":-1} both have a sum of 3.
# {"a":[-1,1]} and [-1,{"a":1}] both have a sum of 0.
# [] and {} both have a sum of 0.
# You will not encounter any strings containing numbers.
#
# What is the sum of all numbers in the document?

import re
import json


def find_all_numbers() -> int:
    # read json file as plain text and find all numbers
    with open('year2015_day12_challenge_input.json', 'r', encoding='UTF-8') as f:
        string_json = str(json.load(f))

    return sum(int(x) for x in re.findall(r'-?\d+', string_json))


if __name__ == '__main__':
    result = find_all_numbers()
    print(result)
