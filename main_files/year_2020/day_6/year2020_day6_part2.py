# --- Part Two ---
# As you finish the last group's customs declaration, you notice that you misread one word in the instructions:
#
# You don't need to identify the questions to which anyone answered "yes"; you need to identify the questions to which everyone answered "yes"!
#
# Using the same example as above:
#
# abc
#
# a
# b
# c
#
# ab
# ac
#
# a
# a
# a
# a
#
# b
# This list represents answers from five groups:
#
# In the first group, everyone (all 1 person) answered "yes" to 3 questions: a, b, and c.
# In the second group, there is no question to which everyone answered "yes".
# In the third group, everyone answered yes to only 1 question, a. Since some people did not answer "yes" to b or c, they don't count.
# In the fourth group, everyone answered yes to only 1 question, a.
# In the fifth group, everyone (all 1 person) answered "yes" to 1 question, b.
# In this example, the sum of these counts is 3 + 0 + 1 + 1 + 1 = 6.
#
# For each group, count the number of questions to which everyone answered "yes". What is the sum of those counts?


from functools import reduce

def prepare_data(file_name: str) -> list:
    """Function for creating data for calculations. Each set of people is list in a list - one line is one string."""
    data_to_return = []
    with open(file_name, 'r', encoding='UTF-8') as f:
        current_ppl_set = []
        for line in f:
            line = line.strip()
            if line == '':  # if line is empty, next set of people
                data_to_return.append(current_ppl_set)
                current_ppl_set = []  # reset current set
            else:
                current_ppl_set.append(line)
        data_to_return.append(current_ppl_set)  # add last element
    return data_to_return

def calculate_num_of_yes_sec(data: list) -> int:
    sum_number = 0
    for ppl_set in data:
        counter_ppl_set = [set(x) for x in ppl_set]  # sets for using intersection
        sum_number += len(reduce(lambda x, y: x.intersection(y), counter_ppl_set))
    return sum_number

def main():
    data = prepare_data('year2020_day6_challenge_input.txt')
    result = calculate_num_of_yes_sec(data)
    # print(data)
    print(f"Number of all yes'es is {result}")

if __name__ == '__main__':
    main()