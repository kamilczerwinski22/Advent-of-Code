# --- Part Two ---
# Seeing how reindeer move in bursts, Santa decides he's not pleased with the old scoring system.
#
# Instead, at the end of each second, he awards one point to the reindeer currently in the lead. (If there are
# multiple reindeer tied for the lead, they each get one point.) He keeps the traditional 2503 second time limit,
# of course, as doing otherwise would be entirely ridiculous.
#
# Given the example reindeer from above, after the first second, Dancer is in the lead and gets one point. He stays
# in the lead until several seconds into Comet's second burst: after the 140th second, Comet pulls into the lead and
# gets his first point. Of course, since Dancer had been in the lead for the 139 seconds before that,
# he has accumulated 139 points by the 140th second.
#
# After the 1000th second, Dancer has accumulated 689 points, while poor Comet, our old champion, only has 312. So,
# with the new scoring system, Dancer would win (if the race ended at 1000 seconds).
#
# Again given the descriptions of each reindeer (in your puzzle input), after exactly 2503 seconds, how many points
# does the winning reindeer have?

import re
from itertools import cycle


def simulate_race(finish_time: int) -> int:
    # initial variables
    reindeers = dict()  # store each reindeer properties
    helper_dict = dict()  # each reindeer score, cycle iterator, current distance

    # read file
    regex_string = r'(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.'
    with open('year2015_day14_challenge_input.txt', 'r', encoding='UTF-8') as f:
        for line in f.read().splitlines():
            reindeer_name, speed, seconds, rest_time = re.findall(regex_string, line)[0]

            # add to properties dictionary
            reindeers[reindeer_name] = {
                'speed': int(speed),
                'seconds': int(seconds),
                'rest': int(rest_time),
            }

            # add iterator
            helper_dict[reindeer_name] = {
                'iterator': cycle([1] * int(seconds) + [0] * int(rest_time)),
                'distance': 0,
                'score': 0
            }

    # main function logic
    for t in range(1, finish_time + 1):
        current_second_scores = []  # list of tuples with name and distance

        # for each second check who is in the lead and give points
        for current_reindeer, values in reindeers.items():
            # if reindeer is moving add distance
            if next(helper_dict[current_reindeer]['iterator']) == 1:
                helper_dict[current_reindeer]['distance'] += reindeers[current_reindeer]['speed']

            # add current reindeer distance
            current_second_scores.append((current_reindeer, helper_dict[current_reindeer]['distance']))

        # check furthest distance at time 't' and add points to the winners
        winning_distance = max(current_second_scores, key=lambda x: x[1])[1]
        for current_reindeer, current_distance in current_second_scores:
            if current_distance == winning_distance:
                helper_dict[current_reindeer]['score'] += 1

    return max(dic['score'] for dic in helper_dict.values())


if __name__ == '__main__':
    max_distance = simulate_race(2503)
    print(max_distance)
