#!/usr/bin/env python3

from sys import stdin
from functools import cache


@cache
def brute_force(s: str, groups: tuple):
    if not s:
        return len(groups) == 0
    if not groups:
        return s.find('#') == -1
    if len(s) < sum(groups) + len(groups) - 1:
        return 0

    if s[0] == '?':
        return brute_force('#' + s[1:], groups) + brute_force('.' + s[1:], groups)

    if s[0] == '#':
        group, *rest = groups
        for x in range(group):
            if s[x] == '.':
                return 0
        if group < len(s) and s[group] == '#':
            return 0
        return brute_force(s[group + 1:], tuple(rest))

    return brute_force(s[1:], groups)


def solve() -> None:
    input = [l.split() for l in stdin.read().splitlines()]
    input = [(springs, tuple(map(int, groups.split(','))))
             for springs, groups in input]
    print(sum(brute_force(springs + ".", groups) for springs, groups in input))
    print(sum(brute_force("?".join([group] * 5), sizes * 5)
          for group, sizes in input))


if __name__ == '__main__':
    solve()
