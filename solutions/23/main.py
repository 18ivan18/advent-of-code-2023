#!/usr/bin/env python3
from sys import stdin, setrecursionlimit

UP, DOWN, LEFT, RIGHT = (-1, 0), (1, 0), (0, -1), (0, 1)
dirs = {'.': [UP, DOWN, LEFT, RIGHT],
        'v': [DOWN], '^': [UP], '>': [RIGHT], '<': [LEFT]}

longest = 0
visited = set()


def dfs(coords, end, grid, len=1):
    global longest
    if coords == end:
        longest = max(longest, len)
        return

    visited.add(coords)
    x, y = coords
    for dx, dy in dirs[grid[x][y]]:
        n_x, n_y = x+dx, y+dy
        if (n_x, n_y) not in visited and grid[n_x][n_y] != '#':
            dfs((n_x, n_y), end, grid, len+1)

    visited.remove(coords)


def solve() -> None:
    input = stdin.read().splitlines()
    sz = len(input)
    start_x, start_y, end = 0, 1, (sz-1, sz-2)
    visited.add((start_x, start_y))
    # lol
    setrecursionlimit(1_000_000)
    dfs((start_x+1, start_y), end, input)
    print(longest)


if __name__ == '__main__':
    solve()
