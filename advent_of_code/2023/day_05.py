from collections import defaultdict, deque
import re
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
    map,
    range,
    search,
    tail_call,
)

raw = aoc_helper.fetch(5, 2023)


def parse_raw(raw: str):
    return raw


data = parse_raw(raw)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    seeds = map(int, re.findall(r"(\d+)", data.splitlines()[0]))
    min_location = float("inf")

    for seed in seeds:
        carry = seed
        for map_ in data.split("map:")[1:]:
            for line in map_.splitlines():
                if not line or not line[0].isdigit():
                    continue
            
                numbers = list(map(int, re.findall(r"(\d+)", line)))
                if numbers[1] <= carry <= numbers[1] + numbers[2]:
                    carry = (carry - numbers[1]) + numbers[0]
                    break
        min_location = min(min_location, carry) 
    return min_location


# aoc_helper.lazy_test(day=5, year=2023, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    # BROKEN
    seeds = list(map(int, re.findall(r"(\d+)", data.splitlines()[0])))
    ranges = [[seeds[i], seeds[i] + seeds[i + 1]] for i in range(len(seeds) - 1)]

    for map_ in data.split("map:")[1:]:
        r = []
        for range_ in ranges:
            for line in map_.splitlines():
                if not line or not line[0].isdigit():
                    continue
            
                numbers = list(map(int, re.findall(r"(\d+)", line)))
                if numbers[1] <= range_[0] <= numbers[1] + numbers[2]:
                    r.append(range(numbers[1], min(numbers[1] + numbers[2])))
            
        ranges = r
    return min(ranges)[0]

aoc_helper.lazy_test(day=5, year=2023, parse=parse_raw, solution=part_two)

# aoc_helper.lazy_submit(day=5, year=2023, solution=part_one, data=data)
aoc_helper.lazy_submit(day=5, year=2023, solution=part_two, data=data)
