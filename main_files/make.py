import os

for i in range(1, 26):
    os.mkdir(f"day_{i}")
    open(f"day_{i}/year2016_day{i}_challenge_input.txt", 'a').close()
    open(f"day_{i}/year2016_day{i}_part1.py", 'a').close()
    open(f"day_{i}/year2016_day{i}_part2.py", 'a').close()