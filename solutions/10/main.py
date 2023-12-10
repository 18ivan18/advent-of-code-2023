#!/usr/bin/env python3

from sys import stdin

UP, DOWN, LEFT, RIGH = (-1, 0), (1, 0), (0, -1), (0, 1)

connection_map = {'|': [UP, DOWN], '-': [LEFT, RIGH],
                  'L': [UP, RIGH], 'J': [UP, LEFT],
                  '7': [LEFT, DOWN], 'F': [RIGH, DOWN], '.': []}


def find_s(map: list[list[str]], s: str = 'F'):
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == 'S':
                map[i][j] = s
                return (i, j)


def solve() -> None:
    input = [list(x) for x in stdin.read().splitlines()]
    start = find_s(input, 'J')
    q, d = [start], 0
    visited = set(q)
    while len(q) != 0:
        l = len(q)
        for _ in range(l):
            x, y = q.pop(0)
            directions = connection_map[input[x][y]]
            for i, j in directions:
                dx, dy = x+i, y+j
                if dx >= 0 and dx < len(input) and dy >= 0 and dy < len(input[0]) and not (dx, dy) in visited:
                    visited.add((dx, dy))
                    q.append((dx, dy))
        d += 1

    print(d - 1)

    for i in range(len(input)):
        norths = 0
        for j in range(len(input[i])):
            tile = input[i][j]
            if (i, j) in visited:
                if tile in ['|', 'L', 'J']:
                    norths += 1
                continue
            input[i][j] = "O" if norths % 2 == 0 else "I"

    inside_count = "\n".join(["".join(line) for line in input]).count("I")
    print(inside_count)


if __name__ == '__main__':
    solve()
