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

raw = aoc_helper.fetch(9, 2023)


def parse_raw(raw: str):
    return raw


data = parse_raw(raw)


def find_diff_sequence(sequences: list[list[int]]) -> list[list[int]]:
    s = []
    for i in range(len(sequences[-1]) - 1):
        s.append(sequences[-1][i + 1] - sequences[-1][i])
    if all(a == 0 for a in s):
        return [*sequences, s]
    return find_diff_sequence([*sequences, s])


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    def find_next_term(line: str) -> int:
        sequences = find_diff_sequence([list(map(int, line.split(" ")))])
        next_add = 0
        for sequence in sequences[::-1]:
            next_add = sequence[-1] + next_add
        return next_add

    total = 0
    for line in data.splitlines():
        total += find_next_term(line)
    return total

aoc_helper.lazy_test(day=9, year=2023, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    def find_prev_term(line: str) -> int:
        sequences = find_diff_sequence([list(map(int, line.split(" ")))])
        prev_add = 0
        for sequence in sequences[::-1]:
            prev_add = sequence[0] - prev_add
        return prev_add

    total = 0
    for line in data.splitlines():
        total += find_prev_term(line)
    return total


aoc_helper.lazy_test(day=9, year=2023, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=9, year=2023, solution=part_one, data=data)
aoc_helper.lazy_submit(day=9, year=2023, solution=part_two, data=data)
