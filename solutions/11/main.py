#!/usr/bin/env python3

from sys import stdin


def transpose(X):
    return [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]


expansion_rate1 = 2
expansion_rate2 = 1_000_000

expanded_cols = set()
expanded_rows = set()

# (6,1) to (11,5) -> |x1-x2| + |y1-y2| = 9
# (0,4) to (1,9) -> |x1-x2| + |y1-y2| = 6


def shortest_path(x1, y1, x2, y2, expansion_rate):
    # return abs(x1-x2) + abs(y1-y2)
    min_x, max_x = min(x1, x2), max(x1, x2)
    min_y, max_y = min(y1, y2), max(y1, y2)
    path = 0
    for i in range(min_x, max_x):
        path += expansion_rate if i in expanded_rows else 1
    for i in range(min_y, max_y):
        path += expansion_rate if i in expanded_cols else 1
    return path


def empty(x: str):
    for ch in x:
        if ch != '.':
            return False
    return True


def expand(galaxy: list[str]):
    for i in range(len(galaxy)):
        if empty(galaxy[i]):
            expanded_rows.add(i)
    t = transpose(galaxy)
    for j in range(len(t)):
        if empty(t[j]):
            expanded_cols.add(j)


def solve() -> None:
    input = stdin.read().splitlines()
    expand(input)
    sum1, sum2, galaxies = 0, 0, []
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] == '#':
                for x1, y1 in galaxies:
                    sum1 += shortest_path(x1, y1, i, j, expansion_rate1)
                    sum2 += shortest_path(x1, y1, i, j, expansion_rate2)
                galaxies.append((i, j))
    print(sum1)
    print(sum2)


if __name__ == '__main__':
    solve()
