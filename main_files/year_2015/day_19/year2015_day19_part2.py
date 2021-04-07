# --- Part Two ---
# Now that the machine is calibrated, you're ready to begin molecule fabrication.
#
# Molecule fabrication always begins with just a single electron, e, and applying replacements one at a time,
# just like the ones during calibration.
#
# For example, suppose you have the following replacements:
#
# e => H
# e => O
# H => HO
# H => OH
# O => HH
# If you'd like to make HOH, you start with e, and then make the following replacements:
#
# - e => O to get O
# - O => HH to get HH
# - H => OH (on the second H) to get HOH
# So, you could make HOH after 3 steps. Santa's favorite molecule, HOHOHO, can be made in 6 steps.
#
# How long will it take to make the medicine? Given the available replacements and the medicine molecule in your
# puzzle input, what is the fewest number of steps to go from e to the medicine molecule?

from random import shuffle


def calculate_num_of_replacements() -> int:
    # read file
    data = {}
    with open('year2015_day19_challenge_input.txt', 'r') as f:
        for line in f.read().splitlines():
            if '=>' not in line:  # medicine molecule for which you need to calibrate the machine
                initial_sequence = line
                continue

            # add possible replacements to dictionary
            key, replacement = [text.strip() for text in line.split('=>')]
            data[replacement] = key

    # main logic
    data_keys = list(data.keys())
    initial_sequence_backup = initial_sequence
    num_of_replacements = 0
    while initial_sequence != 'e':
        for idx, element in enumerate(data_keys, 1):
            pos = initial_sequence.find(element)

            # if found in the initial sequence, replace and start for the loop all over again (use all available keys)
            if pos != -1:
                initial_sequence = initial_sequence[:pos] + data[element] + initial_sequence[pos + len(element):]
                num_of_replacements += 1
                break

            else:
                # if couldn't replace anything from keys and initial_sequence is still not 'e',
                # start all over again with shuffled data_keys (different combination)
                if idx == len(data_keys):
                    shuffle(data_keys)
                    initial_sequence = initial_sequence_backup
                    num_of_replacements = 0

    # if loop ended, return num of replacements
    return num_of_replacements


if __name__ == '__main__':
    result = calculate_num_of_replacements()
    print(f"Result is: {result}")
