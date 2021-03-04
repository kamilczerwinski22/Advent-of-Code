# --- Part Two ---
# Time to check the rest of the slopes - you need to minimize the probability of a sudden arboreal stop, after all.
#
# Determine the number of trees you would encounter if, for each of the following slopes, you start at the top-left corner and traverse the map all the way to the bottom:
#
# Right 1, down 1.
# Right 3, down 1. (This is the slope you already checked.)
# Right 5, down 1.
# Right 7, down 1.
# Right 1, down 2.
# In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s) respectively; multiplied together, these produce the answer 336.
#
# What do you get if you multiply together the number of trees encountered on each of the listed slopes?


def calculate_tree_number(row_jump: int, col_jump: int) -> int:
    tree_counter = 0
    with open('day3_challange_input.txt', 'r+', encoding='UTF-8') as f:
        max_index = len(f.readline().strip()) - 1
    with open('day3_challange_input.txt', 'r+', encoding='UTF-8') as f:
        current_col = 0
        for idx, line in enumerate(f):
            if idx % row_jump == 0:
                line = line.strip()
                if line[current_col] == '#':
                    tree_counter += 1
                current_col += col_jump
                if current_col > max_index:
                    current_col %= max_index
                    current_col -= 1
    return tree_counter

def calculate_handler(values: list) ->int:
    result = 1
    for row, col in values:
        result *= calculate_tree_number(row, col)
    return result
    # maybe possible with reduce?

def main():
    # list with tuples as values (row_jump, col_jump)
    values_list = [
        (1, 1),
        (1, 3),
        (1, 5),
        (1, 7),
        (2, 1),
    ]

    print(calculate_handler(values_list))

if __name__ == '__main__':
    main()