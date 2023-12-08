#!/usr/bin/env python3

from itertools import cycle
from sys import stdin
import re


def is_finished(finish):
    return all([x.endswith('Z') for x in finish])


def find_way_to2(start, directions, d):
    directions = cycle(directions)
    steps = 0
    while not is_finished(start):
        steps += 1
        dir = next(directions)
        if dir == 'L':
            start = [d[s][0] for s in start]
        if dir == 'R':
            start = [d[s][1] for s in start]
    return steps


def solve():
    input = stdin.read().splitlines()
    d = dict()
    for directions_line in input[2:]:
        _from, left, right = re.findall(r'(\w+)', directions_line)
        d[_from] = (left, right)

    start = list(filter(lambda x: x.endswith('A'), d.keys()))
    print(find_way_to2(start, input[0], d))


if __name__ == '__main__':
    solve()
