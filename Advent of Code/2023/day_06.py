from collections import defaultdict, deque
from typing import TYPE_CHECKING

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

raw = aoc_helper.fetch(6, 2023)


def parse_raw(raw: str):
    return raw


data = parse_raw(raw)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    times = extract_ints(data.splitlines()[0])
    distances = extract_ints(data.splitlines()[1])

    total = 1
    for i in range(len(times)):
        nways = 0
        for j in range(times[i]):
            
            if j * (times[i] - j) > distances[i]:
                nways += 1
        total *= nways
    return total


aoc_helper.lazy_test(day=6, year=2023, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    time = int("".join(map(str, extract_ints(data.splitlines()[0]))))
    distance = int("".join(map(str, extract_ints(data.splitlines()[1]))))

    total = 0
    for j in range(time):
        if j * (time - j) > distance:
            total += 1
    return total


aoc_helper.lazy_test(day=6, year=2023, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=6, year=2023, solution=part_one, data=data)
aoc_helper.lazy_submit(day=6, year=2023, solution=part_two, data=data)
