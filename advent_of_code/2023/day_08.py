from collections import defaultdict, deque
from math import lcm
from typing import TYPE_CHECKING
import re 

import aoc_helper
from aoc_helper import (
    Grid,
    PrioQueue,
    SparseGrid,
    decode_text,
    extract_ints,
    extract_iranges,
    extract_ranges,
    extract_uints,
    frange,
    irange,
    iter,
    list,
    map,
    range,
    search,
    tail_call,
)

raw = aoc_helper.fetch(8, 2023)


def parse_raw(raw: str):
    return raw


data = parse_raw(raw)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    directions = data.splitlines()[0]
    maps = {}
    for line in data.splitlines()[2:]:
        a, b, c = re.findall("\w{3}", line)
        maps[a] = (b, c)
    
    current = "AAA"
    number = 0
    while current != "ZZZ":
        for direction in directions:
            if direction == "L":
                current = maps[current][0]
            elif direction == "R":
                current = maps[current][1]
            number += 1
    return number


aoc_helper.lazy_test(day=8, year=2023, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    directions = data.splitlines()[0]
    maps = {}
    for line in data.splitlines()[2:]:
        a, b, c = re.findall("\w{3}", line)
        maps[a] = (b, c)

    locations = [location for location in maps if location.endswith("A")]
    
    cycle_times = []
    for location in locations:
        current = location
        count = 0
        while not current.endswith("Z"):
            for direction in directions:
                if direction == "L":
                    current = maps[current][0]
                elif direction == "R":
                    current = maps[current][1]
                count += 1
        cycle_times.append(count)
    return lcm(*cycle_times)


aoc_helper.lazy_test(day=8, year=2023, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=8, year=2023, solution=part_one, data=data)
aoc_helper.lazy_submit(day=8, year=2023, solution=part_two, data=data)
