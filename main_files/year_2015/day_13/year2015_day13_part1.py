# --- Day 13: Knights of the Dinner Table --- In years past, the holiday feast with your family hasn't gone so well.
# Not everyone gets along! This year, you resolve, will be different. You're going to find the optimal seating
# arrangement and avoid all those awkward conversations.
#
# You start by writing up a list of everyone invited and the amount their happiness would increase or decrease if
# they were to find themselves sitting next to each other person. You have a circular table that will be just big
# enough to fit everyone comfortably, and so each person will have exactly two neighbors.
#
# For example, suppose you have only four attendees planned, and you calculate their potential happiness as follows:
#
# Alice would gain 54 happiness units by sitting next to Bob. Alice would lose 79 happiness units by sitting next to
# Carol. Alice would lose 2 happiness units by sitting next to David. Bob would gain 83 happiness units by sitting
# next to Alice. Bob would lose 7 happiness units by sitting next to Carol. Bob would lose 63 happiness units by
# sitting next to David. Carol would lose 62 happiness units by sitting next to Alice. Carol would gain 60 happiness
# units by sitting next to Bob. Carol would gain 55 happiness units by sitting next to David. David would gain 46
# happiness units by sitting next to Alice. David would lose 7 happiness units by sitting next to Bob. David would
# gain 41 happiness units by sitting next to Carol. Then, if you seat Alice next to David, Alice would lose 2
# happiness units (because David talks so much), but David would gain 46 happiness units (because Alice is such a
# good listener), for a total change of 44.
#
# If you continue around the table, you could then seat Bob next to Alice (Bob gains 83, Alice gains 54). Finally,
# seat Carol, who sits next to Bob (Carol gains 60, Bob loses 7) and David (Carol gains 55, David gains 41). The
# arrangement looks like this:
#
# +41 +46 +55   David    -2 Carol       Alice +60    Bob    +54 -7  +83 After trying every other seating arrangement
# in this hypothetical scenario, you find that this one is the most optimal, with a total change in happiness of 330.
#
# What is the total change in happiness for the optimal seating arrangement of the actual guest list?

from collections import defaultdict
from itertools import permutations


def find_optimal_arrangement() -> int:
    # read file
    with open('year2015_day13_challenge_input.txt', 'r', encoding='UTF-8') as f:
        arrangement_instructions = f.read().replace('gain ', '').replace('lose ', '-').splitlines()

    # main logic
    all_people = set()
    happiness = defaultdict(dict)
    for seq in arrangement_instructions:
        first_person, _, value, *_, second_person = seq[:-1].split(' ')

        all_people.add(first_person)
        all_people.add(second_person)

        # add happiness to the graph (dictionary) from both sides. If connection between people doesn't exist, make it
        happiness[first_person][second_person] = int(value)

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
