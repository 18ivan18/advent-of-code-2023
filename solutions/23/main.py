#!/usr/bin/env python3

from functools import cache
from sys import stdin, setrecursionlimit

UP, DOWN, LEFT, RIGHT = (-1, 0), (1, 0), (0, -1), (0, 1)
dirs = {'^': [UP], 'v': [DOWN], '>': [RIGHT],
        '<': [LEFT], '.': [UP, DOWN, LEFT, RIGHT]}
dir_to_char = {UP: '^',  DOWN: 'v', RIGHT: '>',
               LEFT: '<'}


def in_maze(x, y, input):
    return 0 <= x < len(input) and 0 <= y < len(input)


all_paths = []
visited = set()
input = []


@cache
def dfs(coords, end, path):
    if coords == end:
        return all_paths.append(path)

    x, y = coords
    visited.add((x, y))

    for dx, dy in dirs[input[x][y]]:
        n_x, n_y = x+dx, y+dy
        if not in_maze(n_x, n_y, input) or (n_x, n_y) in visited or input[n_x][n_y] == '#':
            continue
        path += dir_to_char[(dx, dy)]
        dfs((n_x, n_y), end, path)
        path = path[:-1]

    visited.remove((x, y))


def solve():
    global input
    input = stdin.read().splitlines()
    sz = len(input)

    start, end = (0, 1), (sz-1, sz-2)
    path = ''
    setrecursionlimit(200000)
    dfs(start, end, path)
    print(max(map(len, all_paths)))


if __name__ == '__main__':
    solve()
