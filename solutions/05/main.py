#!/usr/bin/env python3

from sys import stdin


def create_map(x):
    map_values = x.splitlines()[1:]
    m = []
    for x in map_values:
        mapped = list(map(int, x.split()))
        m.append(mapped)

    return m

def to_pairs(l):
    out = []
    for i in range(0, len(l), 2):
        out.append((l[i], l[i+1]))
    return out


def solve():
    input = stdin.read().split('\n\n')
    seeds = to_pairs(list(map(int, input[0].split(': ')[1].split())))
    maps = []
    for x in input[1:]:
        maps.append(create_map(x))
    res = float('inf')
    for start, length in seeds:
        for seed in range(start, start + length):
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
