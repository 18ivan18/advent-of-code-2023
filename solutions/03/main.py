#!/usr/bin/env python3

from collections import defaultdict
from sys import stdin

adjasents = defaultdict(list)


def isAdjasent(mat, x: int, y: int):
    for i in range(-1, 2):
        for j in range(-1, 2):
            dx, dy = x+i, y+j
            if dx >= 0 and dx < len(mat) and dy >= 0 and dy < len(mat[0]) and mat[dx][dy] != '.' and not mat[dx][dy].isdigit():
                return True, (dx, dy) if mat[dx][dy] == '*' else None
    return False, None


def solve() -> None:
    input = stdin.read().splitlines()
    result = 0
    for i, x in enumerate(input):
        num, include, last_coords = 0, False, None
        for j, y in enumerate(x + '.'):
            if y.isdigit():
                num = num*10+int(y)
                if not include:
                    adj, coords = isAdjasent(input, i, j)
                    if adj:
                        include = adj
                        last_coords = coords
            else:
                if include:
                    result += num
                    adjasents[last_coords].append(num)
                num, include = 0, False

    print(result)
    print(sum([x[0]*x[1] if len(x) == 2 else 0 for x in adjasents.values()]))


if __name__ == '__main__':
    solve()
