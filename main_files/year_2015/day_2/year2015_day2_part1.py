# --- Day 2: I Was Told There Would Be No Math --- The elves are running low on wrapping paper, and so they need to
# submit an order for more. They have a list of the dimensions (length l, width w, and height h) of each present,
# and only want to order exactly as much as they need.
#
# Fortunately, every present is a box (a perfect right rectangular prism), which makes calculating the required
# wrapping paper for each gift a little easier: find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l. The
# elves also need a little extra paper for each present: the area of the smallest side.
#
# For example:
#
# A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of wrapping paper plus 6 square feet of
# slack, for a total of 58 square feet. A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square feet
# of wrapping paper plus 1 square foot of slack, for a total of 43 square feet. All numbers in the elves' list are in
# feet. How many total square feet of wrapping paper should they order?


def calculate_single_box(length: int, width: int, height: int) -> int:
    dimensions = [length, width, height]
    surfaces_list = [2 * length * width, 2 * width * height, 2 * height * length]
    additional_surface = dimensions.pop(dimensions.index(min(dimensions))) * dimensions.pop(
        dimensions.index(min(dimensions)))
    return sum(surfaces_list) + additional_surface


def main() -> int:
    # read file
    with open('year2015_day2_challenge_input.txt', 'r', encoding='UTF-8') as f:
        boxes_list = f.read().splitlines()

    # main function logic
    paper_sum = 0
    for box in boxes_list:
        paper_sum += calculate_single_box(*[int(value) for value in box.split('x')])
    return paper_sum


if __name__ == '__main__':
    result = main()
    print(result)
