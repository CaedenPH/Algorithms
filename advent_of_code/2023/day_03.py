from collections import defaultdict, deque
from math import prod
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

raw = aoc_helper.fetch(3, 2023)

def parse_raw(raw: str):
    return raw.splitlines()


data = parse_raw(raw)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    total = 0
    locations = []
    
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] in "0123456789.":
                continue
            
            surrounding_locations = [
                (i, j - 1),
                (i, j + 1),

                (i - 1, j - 1),
                (i - 1, j),
                (i - 1, j + 1),

                (i + 1, j - 1),
                (i + 1, j),
                (i + 1, j + 1)
            ]
            for location in surrounding_locations:
                try:
                    x, y = location 
                    number = data[x][y]
                except IndexError:
                    continue
                
                if not number.isdigit():    
                    continue

                for direction in (1, -1):
                    m = y + direction
                    while 0 <= m < len(data[x]) and data[x][m].isdigit():
                        number = data[x][m] + number if direction == -1 else number + data[x][m]
                        m += direction

                start = (x, m)
                if start not in locations:
                    locations.append(start)
                    total += int(number)
    return total

aoc_helper.lazy_test(day=3, year=2023, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    total = 0
    locations = []
    
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] in "0123456789.":
                continue

            surrounding_locations = [
                (i, j - 1),
                (i, j + 1),

                (i - 1, j - 1),
                (i - 1, j),
                (i - 1, j + 1),

                (i + 1, j - 1),
                (i + 1, j),
                (i + 1, j + 1)
            ]
            numbers = []
            for location in surrounding_locations:
                try:  # Easier than writing checks
                    x, y = location 
                    number = data[x][y]
                except IndexError:
                    continue
                
                if not number.isdigit():    
                    continue

                for direction in (1, -1):
                    m = y + direction
                    while 0 <= m < len(data[x]) and data[x][m].isdigit():
                        number = data[x][m] + number if direction == -1 else number + data[x][m]
                        m += direction

                start = (x, m)
                if start not in locations:
                    locations.append(start)
                    numbers.append(int(number))

            if len(numbers) > 1:
                total += prod(numbers)
    return total

aoc_helper.lazy_test(day=3, year=2023, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=3, year=2023, solution=part_one, data=data)
aoc_helper.lazy_submit(day=3, year=2023, solution=part_two, data=data)
