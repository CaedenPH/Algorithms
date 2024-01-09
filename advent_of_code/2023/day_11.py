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
    # list,
    map,
    # range,
    search,
    tail_call,
)

raw = aoc_helper.fetch(11, 2023)


def parse_raw(raw: str):
    return [list(r) for r in raw.splitlines()] 


data = parse_raw(raw)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    x, y = range(len(data)), range(len(data[0]))
    rows, cols = list(x), list(y)

    for i in x:
        for j in y:
            if data[i][j] == ".":
                continue
            if i in rows:
                rows.remove(i)
            if j in cols:
                cols.remove(j)

    for j, col in enumerate(cols):
        [data[i].insert(col + j, ".") for i in range(len(data))]

    for j, row in enumerate(rows):
        data.insert(row + j, ["."]*len(list(data[0])))

    locations = [(i, j) for i in range(len(data)) for j in range(len(data[0])) if data[i][j] != "."]
    total = 0
    for i in range(len(locations)):
        for j in range(i + 1, len(locations)):
            total += abs(locations[i][0] - locations[j][0]) + abs(locations[i][1] - locations[j][1])
    return total


aoc_helper.lazy_test(day=11, year=2023, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    x, y = range(len(data)), range(len(data[0]))
    rows, cols = list(x), list(y)

    for i in x:
        for j in y:
            if data[i][j] == ".":
                continue
            if i in rows:
                rows.remove(i)
            if j in cols:
                cols.remove(j)

    locations = [(j, i) for i in range(len(data)) for j in range(len(data[0])) if data[i][j] != "."]

    total = 0
    for i in range(len(locations)):
        for j in range(i + 1, len(locations)):
            x, y = locations[i]
            m, n = locations[j]

            x += len([c for c in cols if c <= x]) * 999999
            m += len([c for c in cols if c <= m]) * 999999

            y += len([c for c in rows if c <= y]) * 999999
            n += len([c for c in rows if c <= n]) * 999999

            total += abs(x - m) + abs(y - n)
    return total


aoc_helper.lazy_test(day=11, year=2023, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=11, year=2023, solution=part_one, data=data)
aoc_helper.lazy_submit(day=11, year=2023, solution=part_two, data=data)
