# --- Day 14: Reindeer Olympics --- This year is the Reindeer Olympics! Reindeer can fly at high speeds,
# but must rest occasionally to recover their energy. Santa would like to know which of his reindeer is fastest,
# and so he has them race.
#
# Reindeer can only either be flying (always at their top speed) or resting (not moving at all), and always spend
# whole seconds in either state.
#
# For example, suppose you have the following Reindeer:
#
# Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds. Dancer can fly 16 km/s for 11 seconds,
# but then must rest for 162 seconds. After one second, Comet has gone 14 km, while Dancer has gone 16 km. After ten
# seconds, Comet has gone 140 km, while Dancer has gone 160 km. On the eleventh second, Comet begins resting (staying
# at 140 km), and Dancer continues on for a total distance of 176 km. On the 12th second, both reindeer are resting.
# They continue to rest until the 138th second, when Comet flies for another ten seconds. On the 174th second,
# Dancer flies for another 11 seconds.
#
# In this example, after the 1000th second, both reindeer are resting, and Comet is in the lead at 1120 km (poor
# Dancer has only gotten 1056 km by that point). So, in this situation, Comet would win (if the race ended at 1000
# seconds).
#
# Given the descriptions of each reindeer (in your puzzle input), after exactly 2503 seconds, what distance has the
# winning reindeer traveled?

import re
from itertools import cycle


def calculate_winner(finish_seconds: int) -> int:
    # read file
    reindeers = dict()  # store each reindeer properties
    regex_string = r'(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.'
    with open('year2015_day14_challenge_input.txt', 'r', encoding='UTF-8') as f:
        for line in f.read().splitlines():
            reindeer_name, speed, seconds, rest_time = re.findall(regex_string, line)[0]
            reindeers[reindeer_name] = {
                'speed': int(speed),
                'seconds': int(seconds),
                'rest': int(rest_time)
            }

    # main function logic
    reindeers_times = [check_distance_at_finish(values, finish_seconds) for values in reindeers.values()]
    return max(reindeers_times)


def check_distance_at_finish(reindeer: dict, finish_seconds: int) -> int:
    distance_after_given_time = 0
    time = 0
    distance_per_second = reindeer['speed']
    seq = cycle([1] * reindeer['seconds'] + [reindeer['rest']])  # iterator with passing time (when reindeer is
    # moving one second , if reindeer is resting given amount of time)
    while time < finish_seconds:
        current_status = next(seq)
        if current_status == 1:  # if 1, reindeer is moving - add one second to time and distance
            distance_after_given_time += distance_per_second
            time += 1
        else:  # reindeer is resting, add time only
            time += current_status

    return distance_after_given_time


if __name__ == '__main__':
    winner_distance = calculate_winner(2503)
    print(winner_distance)
