#!/usr/bin/env python3

from collections import defaultdict
from sys import stdin
from functools import cmp_to_key


FIVE_OF_A_KIND = 7
FOUR_OF_A_KIND = 6
FULL_HOUSE = 5
THREE_OF_A_KIND = 4
TWO_PAIR = 3
ONE_PAIR = 2
NONE = 1


def hand_type(input: str, wildcard: str = None):
    hand = input.split()[0]
    if wildcard is not None:
        if hand == wildcard * 5:
            return FIVE_OF_A_KIND
        hand = sorted(hand.replace(wildcard or '', 'a'))
    d = defaultdict(int)
    for x in hand:
        if wildcard is not None and x == 'a':
            max_value = max(d, key=d.get)
            d[max_value] += 1
            continue
        d[x] += 1
    if len(d) == 1:
        return FIVE_OF_A_KIND
    if len(d) == 5:
        return NONE
    # 3-2 or 4-1
    if len(d) == 2:
        v1, _ = sorted(list(d.values()))
        if v1 == 2:
            return FULL_HOUSE
        return FOUR_OF_A_KIND
    # 3-1-1 or 2-2-1
    if len(d) == 3:
        _, v, _ = sorted(list(d.values()))
        if v == 1:
            return THREE_OF_A_KIND
        return TWO_PAIR
    return ONE_PAIR


def compare(first: str, second: str):
    t1, t2 = hand_type(first), hand_type(second)
    if t1 == t2:
        first = first.replace('A', 'E').replace('K', 'D').replace(
            'Q', 'C').replace('J', 'B').replace('T', 'A')
        second = second.replace('A', 'E').replace('K', 'D').replace(
            'Q', 'C').replace('J', 'B').replace('T', 'A')

        return 1 if first > second else -1
    return 1 if t1 > t2 else -1


def compare_with_wildcard(first: str, second: str):
    t1, t2 = hand_type(first, wildcard='J'), hand_type(second, wildcard='J')
    if t1 == t2:
        first = first.replace('A', 'E').replace('K', 'D').replace(
            'Q', 'C').replace('J', '1').replace('T', 'A')
        second = second.replace('A', 'E').replace('K', 'D').replace(
            'Q', 'C').replace('J', '1').replace('T', 'A')

        return 1 if first > second else -1
    return 1 if t1 > t2 else -1


def solve() -> None:
    input = stdin.read().splitlines()
    input.sort(key=cmp_to_key(compare))
    print(sum([int(x.split()[1]) * idx for idx, x in enumerate(input, 1)]))
    input.sort(key=cmp_to_key(compare_with_wildcard))
    print(sum([int(x.split()[1]) * idx for idx, x in enumerate(input, 1)]))


if __name__ == '__main__':
    solve()
