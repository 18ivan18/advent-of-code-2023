#!/usr/bin/env python3

from itertools import cycle
from math import lcm
from sys import stdin
import re

d = dict()


def find_way_to(start: str, finish, directions: str):
    directions = cycle(directions)
    steps = 0
    while not re.match(finish, start):
        steps += 1
        dir = next(directions)
        if dir == 'L':
            start = d[start][0]
        if dir == 'R':
            start = d[start][1]
    return steps


def solve() -> None:
    input = stdin.read().splitlines()
    directions, _, *rest = input
    for directions_line in rest:
        _from, left, right = re.findall(r'(\w+)', directions_line)
        d[_from] = (left, right)
    print(find_way_to('AAA', 'ZZZ', directions))

    starts = list(filter(lambda x: x.endswith('A'), d.keys()))
    print(lcm(*map(lambda x: find_way_to(x, r'..Z', directions), starts)))


if __name__ == '__main__':
    solve()
