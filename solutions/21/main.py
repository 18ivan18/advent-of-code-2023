#!/usr/bin/env python3

from math import ceil
from sys import stdin

UP, DOWN, LEFT, RIGHT = (-1, 0), (1, 0), (0, -1), (0, 1)
directions = [UP, DOWN, LEFT, RIGHT]


def find_s(input: list[str]):
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] == 'S':
                return (i, j)
    return None


def part_1_neighbors(x: int, y: int, input: list[str]):
    sz = len(input)
    def in_maze(x, y): return 0 <= x < sz and 0 <= y < sz

    neighbors = []
    for dx, dy in directions:
        n_x, n_y = x+dx, y+dy
        if not in_maze(n_x, n_y) or input[n_x][n_y] == '#':
            continue
        neighbors.append((n_x, n_y))
    return neighbors


def part_2_neighbors(x: int, y: int, input: list[str]):
    sz = len(input)

    neighbors = []
    for dx, dy in directions:
        n_x, n_y = x+dx, y+dy
        if input[n_x % sz][n_y % sz] == '#':
            continue
        neighbors.append((n_x, n_y))
    return neighbors


def bfs(input: list[str], times: int, get_neighbors):
    start = find_s(input)
    q = set([start])

    for _ in range(times):
        n_q = set()
        while q:
            x, y = q.pop()
            for neighbor in get_neighbors(x, y, input):
                n_q.add(neighbor)
        q = n_q
    return len(q)


def solve() -> None:
    input = stdin.read().splitlines()

    print(bfs(input, 64, part_1_neighbors))

    # https://www.radfordmathematics.com/algebra/sequences-series/difference-method-sequences/quadratic-sequences.html
    sz = len(input)
    mod = 26501365 % sz
    # quotient = 26501365 / sz
    u1 = bfs(input, mod, part_2_neighbors)
    u2 = bfs(input, mod + sz, part_2_neighbors)
    u3 = bfs(input, mod + 2*sz, part_2_neighbors)

    first_diff1 = u2 - u1
    first_diff2 = u3 - u2
    second_diff = first_diff2 - first_diff1

    A = second_diff // 2
    B = first_diff1 - 3 * A
    C = u1 - B - A
    def f(n): return A*n**2 + B*n + C

    print(f(ceil(26501365/sz)))


if __name__ == '__main__':
    solve()
