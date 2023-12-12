#!/usr/bin/env python3

from sys import stdin
import re

pattern = r'#+'


def brute_force(s: list[str], i: int, groups: list[int]):
    if len(s) == i:
        final = ''.join(s)
        matches = list(map(len, re.findall(pattern, final)))
        return 1 if matches == groups else 0
    if s[i] == '?':
        original = s
        s = original[0:i] + '.' + original[i+1:]
        not_damaged = brute_force(s, i + 1, groups)
        s = original[0:i] + '#' + original[i+1:]
        damaged = brute_force(s, i+1, groups)
        s = original
        return damaged + not_damaged
    return brute_force(s, i+1, groups)


def arrangements(line: str):
    springs, groups = line.split()
    groups = [int(x) for x in groups.split(',')]

    return brute_force(springs, 0, groups)


def solve() -> None:
    input = stdin.read().splitlines()
    print(sum(map(arrangements, input)))


if __name__ == '__main__':
    solve()
