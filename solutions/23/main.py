#!/usr/bin/env python3
from collections import defaultdict
from sys import stdin, setrecursionlimit

UP, DOWN, LEFT, RIGHT = (-1, 0), (1, 0), (0, -1), (0, 1)
all_dirs = [UP, DOWN, LEFT, RIGHT]
dirs = {'.': all_dirs,
        'v': [DOWN], '^': [UP], '>': [RIGHT], '<': [LEFT]}

longest = 0
visited = set()

# part 2, collapse the graph
graph = defaultdict(list)


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


def dfs2(node, end, len):
    global longest, longest_path
    if node == end:
        longest = max(longest, len)
        return

    visited.add(node)
    for next, dist in graph[node]:
        if next not in visited:
            dfs2(next, end, len+dist)

    visited.remove(node)


def solve() -> None:
    input = stdin.read().splitlines()
    sz = len(input)
    start_x, start_y, end = 0, 1, (sz-1, sz-2)
    visited.add((start_x, start_y))
    # lol
    setrecursionlimit(1_000_000)
    dfs((start_x+1, start_y), end, input)
    print(longest)

    # current coords, start, len
    s = [((start_x+1, start_y), (start_x, start_y), 1)]
    while s:
        curr, start, l = s.pop()
        if curr == end:
            graph[start].append((curr, l))
            graph[curr].append((start, l))
            continue
        visited.add(curr)
        x, y = curr
        possible = []
        nodes = []
        for dx, dy in all_dirs:
            n_x, n_y = x+dx, y+dy
            if (n_x, n_y) not in visited and input[n_x][n_y] != '#':
                possible.append((n_x, n_y))
            if (n_x, n_y) in graph:
                nodes.append((n_x, n_y))

        for node in nodes:
            if l > 1:
                graph[start].append((node, l+1))
                graph[node].append((start, l+1))

        if len(possible) > 1:
            graph[start].append((curr, l))
            graph[curr].append((start, l))
        for next in possible:
            l = 1 if len(possible) > 1 else l + 1
            start = start if len(possible) == 1 else curr
            s.append((next, start, l))

    visited.clear()
    dfs2((start_x, start_y), end, 0)
    print(longest)


if __name__ == '__main__':
    solve()
