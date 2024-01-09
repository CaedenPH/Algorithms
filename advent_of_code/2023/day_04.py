import re

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

raw = aoc_helper.fetch(4, 2023)


def parse_raw(raw: str):
    return raw


data = parse_raw(raw)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    total = 0
    for line in data.splitlines():
        winning, ours = line.split("|")
        winning = winning.split(":")[1]
        winning_numbers = re.findall(r"(\d{1,2})", winning)
        our_numbers = re.findall(r"(\d{1,2})", ours)
        x = 0
        for number in our_numbers:
            if number in winning_numbers:
                if x == 0: x = 1
                else: x *= 2
        total += x
    return total

aoc_helper.lazy_test(day=4, year=2023, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    card_counts = {c: 1 for c in range(1, 213)}
    for line in data.splitlines():
        winning, ours = line.split("|")
        card_number = int(winning.split(":")[0][4:].strip())
        winning = winning.split(":")[1]
        winning_numbers = re.findall(r"(\d{1,2})", winning)
        our_numbers = re.findall(r"(\d{1,2})", ours)
        extend = len([number for number in our_numbers if number in winning_numbers])
        for i in range(card_number + 1, card_number + 1 + extend):
            card_counts[i] += card_counts[card_number]
    return sum(card_counts.values())


aoc_helper.lazy_test(day=4, year=2023, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=4, year=2023, solution=part_one, data=data)
aoc_helper.lazy_submit(day=4, year=2023, solution=part_two, data=data)
