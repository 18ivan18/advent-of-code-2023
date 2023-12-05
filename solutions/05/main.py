#!/usr/bin/env python3

from collections import defaultdict
from functools import reduce
from sys import stdin


def create_map(x: str):
    map_values = x.splitlines()[1:]
    m: list[list[int]] = []
    for x in map_values:
        mapped = list(map(int, x.split()))
        m.append(mapped)

    return m


def solve() -> None:
    input = stdin.read().split('\n\n')
    seeds = list(map(int, input[0].split(': ')[1].split()))
    maps: list[list[list[int]]] = []
    for x in input[1:]:
        maps.append(create_map(x))
    # a = list(map(lambda seed: reduce(lambda prev,
    #                                  m: m[prev] if prev in m else prev, maps, seed), seeds))
    # print(min(a))
    res = float('inf')
    for seed in seeds:
        s = seed
        for m in maps:
            # TODO:
            pass
        res = min(res, s)
    print(res)


if __name__ == '__main__':
    solve()
