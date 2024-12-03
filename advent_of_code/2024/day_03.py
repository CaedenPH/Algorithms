from collections import defaultdict, deque, Counter
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
    multirange,
    search,
    tail_call,
)

raw = aoc_helper.fetch(3, 2024)


def parse_raw(raw: str):
    return raw


data = parse_raw(raw)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    pattern = r"mul\((\d+?),(\d+?)\)"
    m = re.findall(pattern, data)
    return sum(int(a)*int(b) for a,b in m)

aoc_helper.lazy_test(day=3, year=2024, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    # Potentially use regex for this
    # data = "do()"+data
    # pattern = r"(?<=do\(\)(?!don't\(\))(.*?))mul\((\d+?),(\d+?)\)"
    # m = re.findall(pattern, data)
    # return sum(int(a)*int(b) for a,b in m)

    pattern = r"mul\((\d+?),(\d+?)\)"
    data = "do()" + data
    m = re.findall(pattern, data)
    
    # Find all indexes of do and dont
    do_indexes = [i for i in range(len(data)) if data.startswith("do()", i)]
    dont_indexes = [i for i in range(len(data)) if data.startswith("don't()", i)]

    t = 0
    for a,b in m:
        index = data.index(f"mul({a},{b})")
        latest_do_index = max(z for z in do_indexes if index > z)
        latest_dont_index = max([0, *[z for z in dont_indexes if index > z]])
        if latest_dont_index > latest_do_index:
            continue
        t += int(a)*int(b)
    return t

# Favourite solution
# def parse_muls2(line):
#     import re
#     line = re.sub(r'don\'t\(\).*?do\(\)', '', line)
#     line = re.sub(r'don\'t\(\).*$', '', line)
#     numbers = re.findall(r'mul\((\d+),(\d+)\)', line)
#     return [int(a) * int(b) for a, b in numbers]

aoc_helper.lazy_test(day=3, year=2024, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=3, year=2024, solution=part_one, data=data)
aoc_helper.lazy_submit(day=3, year=2024, solution=part_two, data=data)
