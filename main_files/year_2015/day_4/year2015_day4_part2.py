# --- Part Two ---
# Now find one that starts with six zeroes.


import hashlib


def find_santa_coin_six_zeros() -> int:
    # read input
    with open('year2015_day4_challenge_input.txt', 'r', encoding='UTF-8') as f:
        input_code = f.read()

    # find md5
    counter = 1
    while True:
        current_result = hashlib.md5(f'{input_code}{counter}'.encode()).hexdigest()
        if current_result.startswith('000000'):
            return counter
        counter += 1


if __name__ == '__main__':
    result = find_santa_coin_six_zeros()
    print(result)