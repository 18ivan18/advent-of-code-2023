#!/usr/bin/env python3

from math import ceil
from sys import stdin


def transpose(X: list[list[str]]):
    return [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]

# 0 -> (0,1)
# 1 -> (0,3),(1,2)
# 2 -> (0,5),(1,4),(2,3)


def find_mirror_index(pattern: list[list[str]]) -> int | None:
    sz = len(pattern)
    for i in range(sz - 1):
        mirror = True
        end = 2*(i+1)
        start = 0 if end < sz else end - sz
        end = end if end < sz else sz
        for j in range(start, (start + end + 1) // 2):
            if pattern[j] != pattern[end - j + start - 1]:
                mirror = False
                break
        if mirror:
            return i + 1  # ith row means i+1
    return None


def solve() -> None:
    input = stdin.read().split('\n\n')
    notes = 0
    for pattern in input:
        lines = [list(x) for x in pattern.splitlines()]
        by_row = find_mirror_index(lines)
        if by_row:
            notes += by_row*100
            continue
        by_column = find_mirror_index(transpose(lines))
        notes += by_column
    print(notes)


if __name__ == '__main__':
    solve()
