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

raw = aoc_helper.fetch(1, 2023)


def parse_raw(raw: str):
    return raw


data = parse_raw(raw)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    import re

    number_list = []
    for line in data.splitlines():
        numbers = re.findall(r"\d{1}", line)
        number_list.append(int(f"{numbers[0]}{numbers[0 if len(numbers) == 1 else -1]}"))
    return sum(number_list)


aoc_helper.lazy_test(day=1, year=2023, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    import regex

    digits = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }

    number_list = []
    for line in data.splitlines():
        numbers = regex.findall(r"(?:\d{1}|one|two|three|four|five|six|seven|eight|nine)", line, overlapped=True)
        
        first_number = digits.get(numbers[0], numbers[0])
        second_number = digits.get(numbers[-1], numbers[-1])
        number_list.append(int(f"{first_number}{second_number}"))
    return sum(number_list)




aoc_helper.lazy_test(day=1, year=2023, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=1, year=2023, solution=part_one, data=data)
aoc_helper.lazy_submit(day=1, year=2023, solution=part_two, data=data)
