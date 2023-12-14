#!/usr/bin/env python3

from sys import stdin


def transpose(X: list[list[str]]):
    return [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]

# 0 -> (0,1)
# 1 -> (0,3),(1,2)
# 2 -> (0,5),(1,4),(2,3)


def diff(x: list[str], y: list[str]):
    d = 0
    for a, b in zip(x, y):
        if a != b:
            d += 1
    return d


def find_mirror_index(pattern: list[list[str]], threshold: int = None) -> int | None:
    sz = len(pattern)
    for i in range(sz - 1):
        end = 2*(i+1)
        start = 0 if end < sz else end - sz
        end = end if end < sz else sz
        diff_sum = 0
        for j in range(start, (start + end + 1) // 2):
            diff_sum += diff(pattern[j], pattern[end - j + start - 1])
        if diff_sum == threshold:
            return i + 1  # ith row means i+1
    return None


def sum_of_mirror_indexes(s: str, threshold: int = None):
    notes = 0
    for pattern in s:
        lines = [list(x) for x in pattern.splitlines()]
        by_row = find_mirror_index(lines, threshold)
        if by_row:
            notes += by_row*100
            continue
        by_column = find_mirror_index(transpose(lines), threshold)
        notes += by_column
    return notes


def solve() -> None:
    input = stdin.read().split('\n\n')
    print(sum_of_mirror_indexes(input, 0))
    print(sum_of_mirror_indexes(input, 1))


if __name__ == '__main__':
    solve()
