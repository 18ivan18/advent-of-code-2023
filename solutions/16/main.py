#!/usr/bin/env python3

from sys import stdin

UP, DOWN, LEFT, RIGHT = (-1, 0), (1, 0), (0, -1), (0, 1)


def get_reflection(input: list[str], coords: tuple[int, int], dir: tuple[int, int]):
    x, y = coords
    c = input[x][y]
    if c == '\\':
        if dir == UP:
            return ((x, y-1), LEFT)
        if dir == DOWN:
            return ((x, y+1), RIGHT)
        if dir == LEFT:
            return ((x-1, y), UP)
        if dir == RIGHT:
            return ((x+1, y), DOWN)
    if c == '/':
        if dir == UP:
            return ((x, y+1), RIGHT)
        if dir == DOWN:
            return ((x, y-1), LEFT)
        if dir == LEFT:
            return ((x+1, y), DOWN)
        if dir == RIGHT:
            return ((x-1, y), UP)
    raise Exception("No other way, wrong input")


def get_reflections_from_splitter(input: list[str], coords: tuple[int, int], dir: tuple[int, int]):
    x, y = coords
    c = input[x][y]
    dx, dy = dir
    if c == '-':
        if dir == UP or dir == DOWN:
            return [((x, y-1), LEFT), ((x, y+1), RIGHT)]
        if dir == LEFT or dir == RIGHT:
            return [((x+dx, y+dy), dir)]
    if c == '|':
        if dir == UP or dir == DOWN:
            return [((x+dx, y+dy), dir)]
        if dir == LEFT or dir == RIGHT:
            return [((x+1, y), DOWN), ((x-1, y), UP)]
    raise Exception("No other way, wrong input")


def get_energized_tiles(input: list[str], start: tuple[int, int], dir: tuple[int, int]):
    visited = set()
    visited.add((start, dir))
    q = [(start, dir)]
    sz = len(input)
    def in_maze(x, y): return 0 <= x < sz and 0 <= y < sz

    while len(q) != 0:
        (x, y), (dx, dy) = q.pop(0)
        if input[x][y] == '.':
            next_tile = ((x+dx, y+dy), (dx, dy))
            if next_tile not in visited and in_maze(*next_tile[0]):
                visited.add(next_tile)
                q.append(next_tile)
        if input[x][y] == '\\' or input[x][y] == '/':
            reflection = get_reflection(input, (x, y), (dx, dy))
            if reflection not in visited and in_maze(*reflection[0]):
                visited.add(reflection)
                q.append(reflection)
        if input[x][y] == '-' or input[x][y] == '|':
            reflections = get_reflections_from_splitter(
                input, (x, y), (dx, dy))
            for reflection in reflections:
                if reflection not in visited and in_maze(*reflection[0]):
                    visited.add(reflection)
                    q.append(reflection)
    seen = set()
    unique = [seen.add(x) or x for x, _ in visited if x not in seen]
    return len(unique)


def solve() -> None:
    input = stdin.read().splitlines()
    print(get_energized_tiles(input, (0, 0), RIGHT))

    starts = []
    for i in range(len(input)):
        starts.append(((0, i), DOWN))
        starts.append(((len(input)-1, i), UP))
        starts.append(((i, 0), RIGHT))
        starts.append(((i, len(input)-1), DOWN))
    print(max(map(lambda x: get_energized_tiles(input, x[0], x[1]), starts)))


if __name__ == '__main__':
    solve()
