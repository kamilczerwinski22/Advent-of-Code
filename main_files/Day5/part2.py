# --- Part Two ---
# Ding! The "fasten seat belt" signs have turned on. Time to find your seat.
#
# It's a completely full flight, so your seat should be the only missing boarding pass in your list. However, there's a catch: some of the seats at the very front and back of the plane don't exist on this aircraft, so they'll be missing from your list as well.
#
# Your seat wasn't at the very front or back, though; the seats with IDs +1 and -1 from yours will be in your list.
#
# What is the ID of your seat?


from part1_binary_boarding import prepare_data

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

def iteration_seat(row_min: int, row_max: int, col_min: int, col_max: int, data: list) -> list:
    # formula for id is : row * 8 + col
    id_list = []
    for ticket in data:
        current_id = iteration_seat_calculate(row_min, row_max, ticket[:7]) * 8 + \
                     iteration_seat_calculate(col_min, col_max, ticket[7:])
        id_list.append(current_id)
    return id_list

def calculate_your_seat(data_list: list) -> int:
        min_id = min(data_list)
        max_id = max(data_list)
        return sum(range(min_id, max_id + 1)) - sum(data_list)


def main():
    data = prepare_data('Challange_input.txt')
    row_min, row_max = 0, 127
    col_min, col_max = 0, 7
    # Iteration
    iteration_result_list = iteration_seat(row_min, row_max, col_min, col_max, data)
    your_seat = calculate_your_seat(iteration_result_list)
    print(f"Your seat id is: {your_seat}")

if __name__ == '__main__':
    main()