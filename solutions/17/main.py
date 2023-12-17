#!/usr/bin/env python3

from sys import stdin
import heapq
UP, DOWN, LEFT, RIGHT = (-1, 0), (1, 0), (0, -1), (0, 1)
dirs = {'^': UP, 'v': DOWN, '>': RIGHT, '<': LEFT}
opposite = {'v': '^', '^': 'v', '>': '<', '<': '>'}


def in_maze(x, y, sz):
    return 0 <= x < sz and 0 <= y < sz


def a_star(input: list[str], start: tuple[int, int], end: tuple[int, int], min: int, max: int):
    visited = set()
    q = [(0, start, '>'), (0, start, 'v')]
    while q:
        dist, position, path = heapq.heappop(q)
        if (position, path) in visited:
            continue
        visited.add((position, path))
        for direction in dirs:
            dx, dy = dirs[direction]
            if path[-1] == opposite[direction]:
                continue
            x, y = position[0]+dx, position[1]+dy
            if not in_maze(x, y, len(input)):
                continue
            if (x, y) == end:
                return d
            if len(path) == max and direction == path[-1]:
                continue
            if len(path) < min and direction != path[-1]:
                continue
            d = dist + int(input[x][y])
            new_path = path+direction if direction == path[-1] else direction
            if ((x, y), new_path) in visited:
                continue
            heapq.heappush(q, (d, (x, y), new_path))

    return None


def solve() -> None:
    input = stdin.read().splitlines()
    start, end = (0, 0), (len(input)-1, len(input)-1)
    print(a_star(input, start, end, min=0, max=3))
    print(a_star(input, start, end, min=4, max=10))


if __name__ == '__main__':
    solve()
