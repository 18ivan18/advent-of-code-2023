#!/usr/bin/env python3

from enum import Enum
from collections import defaultdict
import re
from sys import stdin
from functools import cmp_to_key, total_ordering


def enum_ordering(cls):
    def __lt__(self, other):
        if type(other) == type(self):
            return self.value < other.value

        raise ValueError("Cannot compare different Enums")

    setattr(cls, '__lt__', __lt__)
    return total_ordering(cls)


@enum_ordering
class Combination(Enum):
    FIVE_OF_A_KIND = 7
    FOUR_OF_A_KIND = 6
    FULL_HOUSE = 5
    THREE_OF_A_KIND = 4
    TWO_PAIR = 3
    ONE_PAIR = 2
    NONE = 1


def hand_type(input: str):
    hand = input.split()[0]
    d = defaultdict(int)
    for x in hand:
        d[x] += 1
    if len(d) == 1:
        return Combination.FIVE_OF_A_KIND
    if len(d) == 5:
        return Combination.NONE
    # 3-2 or 4-1
    if len(d) == 2:
        v1, _ = sorted(list(d.values()))
        if v1 == 2:
            return Combination.FULL_HOUSE
        return Combination.FOUR_OF_A_KIND
    # 3-1-1 or 2-2-1
    if len(d) == 3:
        _, v, _ = sorted(list(d.values()))
        if v == 1:
            return Combination.THREE_OF_A_KIND
        return Combination.TWO_PAIR
    return Combination.ONE_PAIR


def compare(first: str, second: str):
    t1, t2 = hand_type(first), hand_type(second)
    if t1 == t2:
        first = first.replace('A', 'E').replace('K', 'D').replace(
            'Q', 'C').replace('J', 'B').replace('T', 'A')
        second = second.replace('A', 'E').replace('K', 'D').replace(
            'Q', 'C').replace('J', 'B').replace('T', 'A')

        return 1 if first > second else -1
    return 1 if t1 > t2 else -1


def solve() -> None:
    input = stdin.read().splitlines()
    input.sort(key=cmp_to_key(compare))
    print(input)
    print(sum([int(x.split()[1]) * idx for idx, x in enumerate(input, 1)]))


def test():
    print(hand_type("ASDFW"))
    print(hand_type("AAAAA"))
    print(hand_type("AA2AA"))
    print(hand_type("AQAQQ"))
    print(hand_type("A4234"))
    print(hand_type("A8QA8"))
    print(hand_type("T55J5"))
    print(hand_type("KK677"))
    print(hand_type("AA6AJ"))


if __name__ == '__main__':
    solve()
