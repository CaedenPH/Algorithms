from collections import Counter, defaultdict, deque
from functools import cmp_to_key
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

raw = aoc_helper.fetch(7, 2023)


def parse_raw(raw: str):
    return raw


data = parse_raw(raw)


def solve(types, p2=False):
    flatten = []
    for type in types[::-1]:
        def sorter(card):
            hierachy = {
                "A": 14,
                "K": 13,
                "Q": 12,
                "J": 1 if p2 else 11,
                "T": 10
            }
            vcard = 0
            for i in range(len(card)):
                value = hierachy.get(card[i]) or int(card[i])
                vcard += (16 ** (4 - i)) * value
            return vcard
        
        type.sort(key=sorter)
        flatten.extend(type)

    lines = data.splitlines()
    total = 0
    for i, hand in enumerate(flatten, start=1):
        for n, line in enumerate(lines):
            if hand in line:
                break
        bid = lines[n].split(" ")[1]
        total += i * int(bid)
    return total

# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    types=[[], [], [], [], [], [], []]
    for hand in [line[:5] for line in data.splitlines()]:
        charcount = Counter(hand)

        # High cards
        if len(charcount) == 5:
            types[6].append(hand)
        # One pair
        elif len(charcount) == 4:
            types[5].append(hand)
        # Five of a kind
        elif len(charcount) == 1:
            types[0].append(hand)
        # Four of a kind
        elif len(charcount) == 2 and list(charcount.values())[0] in [1, 4]:
            types[1].append(hand)
        elif any(v == 3 for v in list(charcount.values())):
            # Full house 
            if len(charcount) == 2:
                types[2].append(hand)
            else:
                # Three of a kind
                types[3].append(hand)
        else:
            # Two pair
            types[4].append(hand)
    return solve(types)


aoc_helper.lazy_test(day=7, year=2023, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    types=[[], [], [], [], [], [], []]
    for hand in [line[:5] for line in data.splitlines()]:
        charcount = Counter(hand)

        if len(charcount) == 1:
            types[0].append(hand)
            continue

        jokers = charcount.get("J", 0)
        no_jokers = charcount.copy()
        if "J" in no_jokers: no_jokers.pop("J")
        
        most_common = jokers + sorted(list(no_jokers.values()), reverse=True)[0]
        if most_common == 5:
            types[0].append(hand)
        elif most_common == 4:
            types[1].append(hand)
        if most_common == 3:
            if len(charcount) == 2 or (len(charcount) == 3 and jokers >= 1):
                types[2].append(hand)
            else:
                types[3].append(hand)
        elif most_common == 2:
            if (len(charcount) == 3 and jokers == 0) or (len(charcount) == 4 and jokers == 1):
                types[4].append(hand)
            if (len(charcount) == 4 and jokers == 0) or (len(charcount) == 5 and jokers == 1):
                types[5].append(hand)
        elif most_common == 1 and len(charcount) == 5:
            types[6].append(hand)
    return solve(types, True)


aoc_helper.lazy_test(day=7, year=2023, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=7, year=2023, solution=part_one, data=data)
aoc_helper.lazy_submit(day=7, year=2023, solution=part_two, data=data)