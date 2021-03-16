# --- Part Two ---
# Uh oh - the Accounting-Elves have realized that they double-counted everything red.
#
# Ignore any object (and all of its children) which has any property with the value "red". Do this only for objects (
# {...}), not arrays ([...]).
#
# [1,2,3] still has a sum of 6.
# [1,{"c":"red","b":2},3] now has a sum of 4, because the middle object is ignored.
# {"d":"red","e":[1,2,3,4],"f":5} now has a sum of 0, because the entire structure is ignored.
# [1,"red",5] has a sum of 6, because "red" in an array has no effect.

import re
import json


def find_all_numbers_without_red() -> int:
    # read json file as plain text and find all numbers
    with open('year2015_day12_challenge_input.json', 'r', encoding='UTF-8') as f:
        # if json object contains red, clear it (use empty dict instead), else use given object
        string_json = str(json.load(f, object_hook=lambda obj: {} if 'red' in obj.values() else obj))

    return sum(int(x) for x in re.findall(r'-?\d+', string_json))


if __name__ == '__main__':
    result = find_all_numbers_without_red()
    print(result)
