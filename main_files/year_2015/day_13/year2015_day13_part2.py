# --- Part Two --- In all the commotion, you realize that you forgot to seat yourself. At this point, you're pretty
# apathetic toward the whole thing, and your happiness wouldn't really go up or down regardless of who you sit next
# to. You assume everyone else would be just as ambivalent about sitting next to you, too.
#
# So, add yourself to the list, and give all happiness relationships that involve you a score of 0.
#
# What is the total change in happiness for the optimal seating arrangement that actually includes yourself?

from collections import defaultdict
from itertools import permutations


def find_optimal_arrangement() -> int:
    # read file
    with open('year2015_day13_challenge_input.txt', 'r', encoding='UTF-8') as f:
        arrangement_instructions = f.read().replace('gain ', '').replace('lose ', '-').splitlines()

    # main logic
    my_name = "ME"
    all_people = {my_name}
    happiness = defaultdict(dict)
    for seq in arrangement_instructions:
        first_person, _, value, *_, second_person = seq[:-1].split(' ')

        all_people.add(first_person)
        all_people.add(second_person)

        # add happiness to the graph (dictionary) from both sides. If connection between people doesn't exist,
        # make it. Add myself to all guests list with connection value as 0
        happiness[first_person][second_person] = int(value)
        happiness[my_name][second_person] = 0
        happiness[first_person][my_name] = 0

    # create all possible arrangements using available nodes (present people). Create a list with the sum of the
    # happiness for each arrangement
    arrangement_happiness_list = []
    for permutation in permutations(all_people):
        current_happiness = 0
        for seat_1, seat_2 in zip(permutation, permutation[1:] + permutation[:1]):
            current_happiness += happiness[seat_1][seat_2]
            current_happiness += happiness[seat_2][seat_1]
            arrangement_happiness_list.append(current_happiness)
    return max(arrangement_happiness_list)


if __name__ == '__main__':
    result = find_optimal_arrangement()
    print(result)
