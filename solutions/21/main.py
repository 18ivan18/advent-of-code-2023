#!/usr/bin/env python3

from sys import stdin

UP, DOWN, LEFT, RIGHT = (-1, 0), (1, 0), (0, -1), (0, 1)
directions = [UP, DOWN, LEFT, RIGHT]


def find_s(input: list[str]):
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] == 'S':
                return (i, j)
    return None


def solve() -> None:
    input = stdin.read().splitlines()
    start = find_s(input)
    sz = len(input)
    def in_maze(x, y): return 0 <= x < sz and 0 <= y < sz
    q = [start]

    for _ in range(64):
        if not q:
            break
        q_size = len(q)
        for i in range(q_size):
            x, y = q.pop(0)
            for dx, dy in directions:
                n_x, n_y = x+dx, y+dy
                if not in_maze(n_x, n_y) or input[n_x][n_y] == '#' or (n_x, n_y) in q:
                    continue
                q.append((n_x, n_y))
    print(len(q))


if __name__ == '__main__':
    solve()
