# --- Part Two ---
# With all the decoy data out of the way, it's time to decrypt this list and get moving.
#
# The room names are encrypted by a state-of-the-art shift cipher, which is nearly unbreakable without the right
# software. However, the information kiosk designers at Easter Bunny HQ were not expecting to deal with a master
# cryptographer like yourself.
#
# To decrypt a room name, rotate each letter forward through the alphabet a number of times equal to the room's
# sector ID. A becomes B, B becomes C, Z becomes A, and so on. Dashes become spaces.
#
# For example, the real name for qzmt-zixmtkozy-ivhz-343 is very encrypted name.
#
# What is the sector ID of the room where North Pole objects are stored?

import re
from string import ascii_lowercase


def decrypt_name(sequence: str, rotations: int) -> str:
    result_string = ''
    for char in sequence:  # for each char
        if char == '-':  # change '-' to whitespace
            result_string += ' '
            continue
        result_string += ascii_lowercase[(ascii_lowercase.index(char) + rotations) % 26]  # rotate by rotations number

    return result_string


def calculate_sectors_sum(string_to_find: str) -> int:
    # read file and look for given string
    with open('year2016_day4_challenge_input.txt', 'r') as f:
        for idx, line in enumerate(f.read().splitlines()):
            # extract data
            sector_id = re.findall(r'\d+', line)[0]
            sequence = line[:line.find(sector_id)].strip('-')
            sector_id = int(sector_id)

            # find string
            if decrypt_name(sequence, sector_id) == string_to_find:
                return sector_id

    return 0


if __name__ == '__main__':
    result = calculate_sectors_sum("northpole object storage")
    print(f"North Pole objects are stored in {result} sector ID")
