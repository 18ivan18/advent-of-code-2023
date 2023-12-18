#!/usr/bin/env python3

from sys import stdin


def solve() -> None:
    input = stdin.read().splitlines()
    x, y = 0, 0
    vertices = [(x, y)]
    border = 0
    for line in input:
        direction, length, color = line.split()
        l = int(length)
        dx, dy = 0, 0
        border += l
        if direction == 'U':
            dx -= 1
        if direction == 'D':
            dx += 1
        if direction == 'R':
            dy += 1
        if direction == 'L':
            dy -= 1
        x, y = x+dx*l, y+dy*l
        vertices.append((x, y))

    # something called shoelace formula for finding the area of a polygon
    s1, s2 = 0, 0
    for i in range(len(vertices)-1):
        s1 += vertices[i][0]*vertices[i+1][1]
        s2 += vertices[i][1]*vertices[i+1][0]
    # print(s1, s2, border)
    print(int(0.5*(abs(s1-s2) + border) + 1))


if __name__ == '__main__':
    solve()
