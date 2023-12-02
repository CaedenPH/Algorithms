from collections import defaultdict, deque
from math import prod
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
    list,
    map,
    range,
    search,
    tail_call,
)

raw = aoc_helper.fetch(2, 2023)


def parse_raw(raw: str):
    return raw


data = parse_raw(raw)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    total = 0

    maxes = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    for game in data.splitlines():
        cubes = game.split(';')
        failed = False

        for cube in cubes:
            for colour in ("red", "blue", "green"):
                match = re.search(fr"(\d+) {colour}", cube)
                number = int(match.group(1)) if match else 0
                if number > maxes[colour]:
                    failed = True
        
        if not failed:
            total += int(game[4:game.index(":")])
    return total


aoc_helper.lazy_test(day=2, year=2023, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    total = 0

    for game in data.splitlines():
        cubes = game.split(';')
        largest_colours = {"green": 0, "red": 0, "blue": 0}

        for cube in cubes:
            for colour in ("red", "blue", "green"):
                match = re.search(fr"(\d+) {colour}", cube)
                number = int(match.group(1)) if match else 0
                if number > largest_colours[colour]:
                    largest_colours[colour] = number

        total += prod(largest_colours.values())
    return total


aoc_helper.lazy_test(day=2, year=2023, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=2, year=2023, solution=part_one, data=data)
aoc_helper.lazy_submit(day=2, year=2023, solution=part_two, data=data)
