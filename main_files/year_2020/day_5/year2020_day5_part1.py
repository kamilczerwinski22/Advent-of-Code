# --- Day 5: Binary Boarding ---
# You board your plane only to discover a new problem: you dropped your boarding pass! You aren't sure which seat is yours, and all of the flight attendants are busy with the flood of people that suddenly made it through passport control.
#
# You write a quick program to use your phone's camera to scan all of the nearby boarding passes (your puzzle input); perhaps you can find your seat through process of elimination.
#
# Instead of zones or groups, this airline uses binary space partitioning to seat people. A seat might be specified like FBFBBFFRLR, where F means "front", B means "back", L means "left", and R means "right".
#
# The first 7 characters will either be F or B; these specify exactly one of the 128 rows on the plane (numbered 0 through 127). Each letter tells you which half of a region the given seat is in. Start with the whole list of rows; the first letter indicates whether the seat is in the front (0 through 63) or the back (64 through 127). The next letter indicates which half of that region the seat is in, and so on until you're left with exactly one row.
#
# For example, consider just the first seven characters of FBFBBFFRLR:
#
# Start by considering the whole range, rows 0 through 127.
# F means to take the lower half, keeping rows 0 through 63.
# B means to take the upper half, keeping rows 32 through 63.
# F means to take the lower half, keeping rows 32 through 47.
# B means to take the upper half, keeping rows 40 through 47.
# B keeps rows 44 through 47.
# F keeps rows 44 through 45.
# The final F keeps the lower of the two, row 44.
# The last three characters will be either L or R; these specify exactly one of the 8 columns of seats on the plane (numbered 0 through 7). The same process as above proceeds again, this time with only three steps. L means to keep the lower half, while R means to keep the upper half.
#
# For example, consider just the last 3 characters of FBFBBFFRLR:
#
# Start by considering the whole range, columns 0 through 7.
# R means to take the upper half, keeping columns 4 through 7.
# L means to take the lower half, keeping columns 4 through 5.
# The final R keeps the upper of the two, column 5.
# So, decoding FBFBBFFRLR reveals that it is the seat at row 44, column 5.
#
# Every seat also has a unique seat ID: multiply the row by 8, then add the column. In this example, the seat has ID 44 * 8 + 5 = 357.
#
# Here are some other boarding passes:
#
# BFFFBBFRRR: row 70, column 7, seat ID 567.
# FFFBBBFRRR: row 14, column 7, seat ID 119.
# BBFFBBFRLL: row 102, column 4, seat ID 820.
# As a sanity check, look through your list of boarding passes. What is the highest seat ID on a boarding pass?


def prepare_data(file_name):
    with open(file_name, 'r+', encoding='UTF-8') as f:
        return [line.strip() for line in f]

# ITERATION VERSION
def iteration_seat_calculate(min_value: int, max_value: int, text: str) -> int:
    for element in text:
        mid_value = (max_value - min_value + 1) // 2  # mid value is half the current numbers -> 0-127 has 128 numbers
                                                      # as 0,1,2,3...127 etc.
        if element in 'BR':  # B and R are for upper half
            min_value += mid_value
        else:
            max_value -= mid_value
        if (max_value - min_value == 0):  # accumulate in one value
            return min_value

def iteration_seat(row_min: int, row_max: int, col_min: int, col_max: int, data: list) -> int:
    # formula for id is : row * 8 + col
    max_id = 0
    for ticket in data:
        current_id = iteration_seat_calculate(row_min, row_max, ticket[:7]) * 8 + \
                     iteration_seat_calculate(col_min, col_max, ticket[7:])
        if current_id > max_id:
            max_id = current_id
    return max_id


# RECURSION VERSION
def recursion_seat_calculate(min_value: int, max_value: int, text: str, counter: int=0) -> int:
    if (max_value - min_value == 0):  # accumulate in one value
        return min_value
    middle_value = (max_value - min_value + 1) // 2  # Same as iteration, half the current numbers
    if text[counter] in 'BR':  # B and R are for upper half
        min_value += middle_value
    else:
        max_value -= middle_value
    return recursion_seat_calculate(min_value, max_value, text, counter + 1)

def recursion_seat(row_min: int, row_max: int, col_min: int, col_max: int, data: list):
    # formula for id is : row * 8 + col
    max_id = 0
    for ticket in data:
        current_id = recursion_seat_calculate(row_min, row_max, ticket[:7]) * 8 + \
                     recursion_seat_calculate(col_min, col_max, ticket[7:])
        if current_id > max_id:
            max_id = current_id
    return max_id


def main():
    data = prepare_data('year2020_day5_challenge_input.txt')

    row_min, row_max = 0, 127
    col_min, col_max = 0, 7
    # Iteration
    iteration_result = iteration_seat(row_min, row_max, col_min, col_max, data)
    print(f"Iteration result is: {iteration_result}")

    # Recursion
    recursion_result = recursion_seat(row_min, row_max, col_min, col_max, data)
    print(f"Recursion result is: {recursion_result}")

if __name__ == '__main__':
    main()