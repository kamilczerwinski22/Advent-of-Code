# --- Part Two --- Now, take the signal you got on wire a, override wire b to that signal, and reset the other wires
# (including wire a). What new signal is ultimately provided to wire a?

import functools


def wiring_system() -> int:
    instructions = {}
    # read file
    with open('year2015_day7_challenge_input.txt', 'r', encoding='UTF-8') as f:
        for line in f.readlines():
            instruction, key = line.split(' -> ')
            instructions[key.strip()] = instruction

    # recursive function calling with cache
    @functools.lru_cache
    def get_value(val: str) -> int:
        try:  # try return it right away
            return int(val)
        except ValueError:
            pass

        seq = instructions[val].split(" ")
        if "NOT" in seq:
            return ~get_value(seq[1])
        elif "AND" in seq:
            return get_value(seq[0]) & get_value(seq[2])
        elif "OR" in seq:
            return get_value(seq[0]) | get_value(seq[2])
        elif "LSHIFT" in seq:
            return get_value(seq[0]) << get_value(seq[2])
        elif "RSHIFT" in seq:
            return get_value(seq[0]) >> get_value(seq[2])
        else:
            return get_value(seq[0])

    instructions["b"] = str(get_value("a"))  # first find value from wire 'a' and override wire 'b' to that signal
    get_value.cache_clear()  # clear cache so previous results won't interrupt
    return get_value("a")


if __name__ == '__main__':
    result = wiring_system()
    print(result)
