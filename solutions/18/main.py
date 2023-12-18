#!/usr/bin/env python3

from sys import stdin

digit_to_dir = {'0': 'R', '1': 'D', '2': 'L', '3': 'U'}


def shoelace(vertices: list[tuple[int, int]], border: int):
    # something called shoelace formula for finding the area of a polygon
    s1, s2 = 0, 0
    for i in range(len(vertices)-1):
        s1 += vertices[i][0]*vertices[i+1][1]
        s2 += vertices[i][1]*vertices[i+1][0]
    # print(s1, s2, border)
    return int(0.5*(abs(s1-s2) + border) + 1)


def do_move(vertices: list[tuple[int, int]], direction: str, len: int):
    x, y = vertices[-1]
    dx, dy = 0, 0
    if direction == 'U':
        dx -= 1
    if direction == 'D':
        dx += 1
    if direction == 'R':
        dy += 1
    if direction == 'L':
        dy -= 1
    x, y = x+dx*len, y+dy*len
    vertices.append((x, y))


def solve() -> None:
    input = stdin.read().splitlines()
    vertices1, vertices2 = [(0, 0)], [(0, 0)]
    border1, border2 = 0, 0
    for line in input:
        direction1, length1, color = line.split()
        length2 = int(color[2:-2], base=16)
        direction2 = digit_to_dir[color[-2]]
        length1 = int(length1)
        border1 += length1
        border2 += length2
        do_move(vertices1, direction1, length1)
        do_move(vertices2, direction2, length2)
    print(shoelace(vertices1, border1))
    print(shoelace(vertices2, border2))


if __name__ == '__main__':
    solve()
