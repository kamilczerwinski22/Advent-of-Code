# --- Part Two --- The elves are also running low on ribbon. Ribbon is all the same width, so they only have to worry
# about the length they need to order, which they would again like to be exact.
#
# The ribbon required to wrap a present is the shortest distance around its sides, or the smallest perimeter of any
# one face. Each present also requires a bow made out of ribbon as well; the feet of ribbon required for the perfect
# bow is equal to the cubic feet of volume of the present. Don't ask how they tie the bow, though; they'll never tell.
#
# For example:
#
# A present with dimensions 2x3x4 requires 2+2+3+3 = 10 feet of ribbon to wrap the present plus 2*3*4 = 24 feet of
# ribbon for the bow, for a total of 34 feet. A present with dimensions 1x1x10 requires 1+1+1+1 = 4 feet of ribbon to
# wrap the present plus 1*1*10 = 10 feet of ribbon for the bow, for a total of 14 feet. How many total feet of ribbon
# should they order?


def calculate_single_ribon(length: int, width: int, height: int) -> int:
    dimensions = [length, width, height]
    smallest_perimeter = (dimensions.pop(dimensions.index(min(dimensions))) + dimensions.pop(
        dimensions.index(min(dimensions)))) * 2
    ribbon_bow = length * width * height
    return smallest_perimeter + ribbon_bow


def main() -> int:
    # read file
    with open('year2015_day2_challenge_input.txt', 'r', encoding='UTF-8') as f:
        boxes_list = f.read().splitlines()

    # main function logic
    ribbon_length_sum = 0
    for box in boxes_list:
        ribbon_length_sum += calculate_single_ribon(*[int(value) for value in box.split('x')])
    return ribbon_length_sum


if __name__ == '__main__':
    result = main()
    print(result)
