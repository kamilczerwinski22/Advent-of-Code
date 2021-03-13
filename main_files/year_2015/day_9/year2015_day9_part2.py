# --- Part Two ---
# The next year, just to show off, Santa decides to take the route with the longest distance instead.
#
# He can still start and end at any two (different) locations he wants, and he still must visit each location exactly
# once.
#
# For example, given the distances above, the longest route would be 982 via (for example) Dublin -> London -> Belfast.
#
# What is the distance of the longest route?

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

    return max(distances)


if __name__ == "__main__":
    graph = find_shortest_route()
    print(graph)
