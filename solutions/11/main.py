#!/usr/bin/env python3

from sys import stdin
import re

# (6,1) to (11,5) -> |x1-x2| + |y1-y2| = 9
# (0,4) to (1,9) -> |x1-x2| + |y1-y2| = 6


def shortest_path(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)


def transpose(X):
    return [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]


def empty(x: str):
    for ch in x:
        if ch != '.':
            return False
    return True


def expand(galaxy: list[str]):
    expanded = []
    for x in galaxy:
        expanded.append(x)
        if empty(x):
            expanded.append(x)
    return expanded


def solve() -> None:
    input = stdin.read().splitlines()
    expanded = transpose(expand(transpose(expand(input))))
    sum, galaxies = 0, []
    for i in range(len(expanded)):
        for j in range(len(expanded[i])):
            if expanded[i][j] == '#':
                for x1, y1 in galaxies:
                    sum += shortest_path(x1, y1, i, j)
                galaxies.append((i, j))
    print(sum)


if __name__ == '__main__':
    solve()
