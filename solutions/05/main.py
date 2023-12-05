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
    res = float('inf')
    for seed in seeds:
        min_seed = seed
        for m in maps:
            for line in m:
                # destination start range, source range, range length 
                s, sr, rl = line
                if sr + rl - 1 >= min_seed and sr <= min_seed:
                    min_seed = min_seed - sr + s
                    break
        res = min(res, min_seed)
    print(res)


if __name__ == '__main__':
    solve()
