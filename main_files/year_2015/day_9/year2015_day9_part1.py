# --- Day 9: All in a Single Night ---
# Every year, Santa manages to deliver all of his presents in a single night.
#
# This year, however, he has some new locations to visit; his elves have provided him the distances between every
# pair of locations. He can start and end at any two (different) locations he wants, but he must visit each location
# exactly once. What is the shortest distance he can travel to achieve this?
#
# For example, given the following distances:
#
# London to Dublin = 464
# London to Belfast = 518
# Dublin to Belfast = 141
# The possible routes are therefore:
#
# Dublin -> London -> Belfast = 982
# London -> Dublin -> Belfast = 605
# London -> Belfast -> Dublin = 659
# Dublin -> Belfast -> London = 659
# Belfast -> Dublin -> London = 605
# Belfast -> London -> Dublin = 982
# The shortest of these is London -> Dublin -> Belfast = 605, and so the answer is 605 in this example.
#
# What is the distance of the shortest route?


from collections import defaultdict
from itertools import permutations


# Function to build the graph
def find_shortest_route() -> int:
    # read file
    with open('year2015_day9_challenge_input.txt', 'r', encoding='UTF-8') as f:
        routes = f.read().splitlines()

    # main logic
    possible_places = set()
    distances_graph = defaultdict(dict)
    for route in routes:
        source, _, destination, _, distance = route.split(' ')
        possible_places.add(source)
        possible_places.add(destination)
        distances_graph[source][destination] = int(distance)
        distances_graph[destination][source] = int(distance)

    distances = []
    for permutation in permutations(possible_places):
        distances.append(sum(map(lambda x, y: distances_graph[x][y], permutation[:-1], permutation[1:])))

    return min(distances)


if __name__ == "__main__":
    graph = find_shortest_route()
    print(graph)
