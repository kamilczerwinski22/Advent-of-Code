# --- Part Two ---
# As you're about to send the thank you note, something in the MFCSAM's instructions catches your eye.
# Apparently, it has an outdated retroencabulator, and so the output from the machine isn't exact values - some
# of them indicate ranges.
#
# In particular, the cats and trees readings indicates that there are greater than that many (due to the
# unpredictable nuclear decay of cat dander and tree pollen), while the pomeranians and goldfish readings indicate
# that there are fewer than that many (due to the modial interaction of magnetoreluctance).
#
# What is the number of the real Aunt Sue?


import re
from collections import defaultdict


def prepare_data() -> dict:
    # collect data
    aunts_data = defaultdict(dict)
    with open('year2015_day16_challenge_input.txt', 'r', encoding='UTF-8') as f:
        for line in f.read().splitlines():
            aunt_num = int(re.findall(r'\d+', line[:line.find(':')])[0])
            current_properties = [tuple(x.split(':')) for x in line[line.find(':') + 1:].split(',')]

            # add to dict with all aunts data
            for key, val in current_properties:
                aunts_data[aunt_num][key.strip()] = int(val.strip())
    return aunts_data


def find_aunt(aunts_data: dict, aunt_to_find: dict) -> int:
    for num, properties in aunts_data.items():
        for element, val in properties.items():
            if element in ['cats', 'trees']:  # special conditions
                if val <= aunt_to_find[element]:
                    break
            elif element in ['pomeranians', 'goldfish']:  # special conditions
                if val >= aunt_to_find[element]:
                    break
                pass
            elif val != aunt_to_find[element]:  # if any property is not the same as aunts' to find, break
                break
        else:  # if for loop didn't break (all properties are the same), return aunts number
            return num
    return 0


if __name__ == '__main__':
    aunt_properties = {
        'children': 3,
        'cats': 7,
        'samoyeds': 2,
        'pomeranians': 3,
        'akitas': 0,
        'vizslas': 0,
        'goldfish': 5,
        'trees': 3,
        'cars': 2,
        'perfumes': 1
    }
    data = prepare_data()
    result = find_aunt(data, aunt_properties)
    print(result)
