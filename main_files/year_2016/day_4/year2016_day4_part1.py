# --- Day 4: Security Through Obscurity ---
# Finally, you come across an information kiosk with a list of rooms. Of course, the list is encrypted and full of
# decoy data, but the instructions to decode the list are barely hidden nearby. Better remove the decoy data first.
#
# Each room consists of an encrypted name (lowercase letters separated by dashes) followed by a dash, a sector ID,
# and a checksum in square brackets.
#
# A room is real (not a decoy) if the checksum is the five most common letters in the encrypted name, in order, with
# ties broken by alphabetization. For example:
#
# - aaaaa-bbb-z-y-x-123[abxyz] is a real room because the most common letters are a (5), b (3), and then a tie between
# x, y, and z, which are listed alphabetically.
# - a-b-c-d-e-f-g-h-987[abcde] is a real room because although the letters are all tied (1 of each), the first five
# are listed alphabetically.
# - not-a-real-room-404[oarel] is a real room.
# - totally-real-room-200[decoy] is not.

# Of the real rooms from the list above, the sum of their sector IDs is 1514.
#
# What is the sum of the sector IDs of the real rooms?

import re
from collections import Counter


def proper_room(sequence: str, checksum: str) -> bool:
    # extract 5 most common letters and compare with checksum
    most_common = sorted(Counter(sequence).items(), key=lambda item: (-item[1], item[0]))[:5]
    return checksum == "".join(char for char, _ in most_common)


def calculate_sectors_sum() -> int:
    # initial variables
    sectors_ids_sum = 0

    # read file, prepare data and find sectors sum
    with open('year2016_day4_challenge_input.txt', 'r') as f:
        for idx, line in enumerate(f.read().splitlines()):
            # extract data
            sector_id = re.findall(r'\d+', line)[0]
            checksum = re.findall(r'\[(.*?)\]', line)[0]
            sequence = line[:line.find(sector_id)].replace('-', '')

            if proper_room(sequence, checksum):
                sectors_ids_sum += int(sector_id)

    return sectors_ids_sum


if __name__ == '__main__':
    result = calculate_sectors_sum()
    print(result)
