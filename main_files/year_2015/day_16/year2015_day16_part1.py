# --- Day 16: Aunt Sue ---
# Your Aunt Sue has given you a wonderful gift, and you'd like to send her a thank you card.
# However, there's a small problem: she signed it "From, Aunt Sue".
#
# You have 500 Aunts named "Sue".
#
# So, to avoid sending the card to the wrong person, you need to figure out which Aunt Sue (which you conveniently
# number 1 to 500, for sanity) gave you the gift. You open the present and, as luck would have it, good ol' Aunt Sue
# got you a My First Crime Scene Analysis Machine! Just what you wanted. Or needed, as the case may be.
#
# The My First Crime Scene Analysis Machine (MFCSAM for short) can detect a few specific compounds in a given sample,
# as well as how many distinct kinds of those compounds there are. According to the instructions, these are what the
# MFCSAM can detect:
#
# - children, by human DNA age analysis.
# - cats. It doesn't differentiate individual breeds.
# - Several seemingly random breeds of dog: samoyeds, pomeranians, akitas, and vizslas.
# - goldfish. No other kinds of fish.
# - trees, all in one group.
# - cars, presumably by exhaust or gasoline or something.
# - perfumes, which is handy, since many of your Aunts Sue wear a few kinds.
# In fact, many of your Aunts Sue have many of these. You put the wrapping from the gift into the MFCSAM.
# It beeps inquisitively at you a few times and then prints out a message on ticker tape:
# - children: 3
# - cats: 7
# - samoyeds: 2
# - pomeranians: 3
# - akitas: 0
# - vizslas: 0
# - goldfish: 5
# - trees: 3
# - cars: 2
# - perfumes: 1
# You make a list of the things you can remember about each Aunt Sue.
# Things missing from your list aren't zero - you simply don't remember the value.
#
# What is the number of the Sue that got you the gift?

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
            if aunt_to_find[element] != val:  # if any property is not the same as aunts' to find, break
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
