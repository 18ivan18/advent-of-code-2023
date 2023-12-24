#!/usr/bin/env python3

from sys import stdin


class Hailstore():
    def __init__(self, line: str) -> None:
        pos, vel = line.split(' @ ')
        self.p_x, self.p_y, self.p_z = list(map(int, pos.split(', ')))
        self.v_x, self.v_y, self.v_z = list(map(int, vel.split(', ')))

    def __repr__(self) -> str:
        return f"{self.p_x},{self.p_y},{self.p_z}@{self.v_x},{self.v_y},{self.v_z}"


def sign(n):
    if n >= 0:
        return 1
    return -1


def meetup_point(A: Hailstore, B: Hailstore):
    are_parallel = ((B.v_y*A.v_x) - (B.v_x*A.v_y)) == 0
    if are_parallel:
        return (0, 0)

    t2 = (A.v_x*(A.p_y - B.p_y) + A.v_y*(B.p_x - A.p_x)) / \
        ((B.v_y*A.v_x) - (B.v_x*A.v_y))

    paths_crossed = (B.p_x + B.v_x*t2, B.p_y + B.v_y*t2)
    paths_crossed_in_the_past_for_A = [sign(d) for d in
                                       (A.p_x-paths_crossed[0], A.p_y-paths_crossed[1])] == [sign(d) for d in (A.v_x, A.v_y)]
    paths_crossed_in_the_past_for_B = [sign(d) for d in
                                       (B.p_x-paths_crossed[0], B.p_y-paths_crossed[1])] == [sign(d) for d in (B.v_x, B.v_y)]
    if paths_crossed_in_the_past_for_A or paths_crossed_in_the_past_for_B:
        return (0, 0)

    return paths_crossed


def number_of_meetups(stones: list[Hailstore], min: int, max: int):
    r = 0
    for i in range(len(stones)):
        for j in range(i+1, len(stones)):
            paths_crossed_x, paths_crossed_y = meetup_point(
                stones[i], stones[j])
            print(i, j, paths_crossed_x, paths_crossed_y)
            if min <= paths_crossed_x <= max and min <= paths_crossed_y <= max:
                r += 1
    return r


def solve() -> None:
    input = stdin.read().splitlines()
    stones = [Hailstore(x) for x in input]
    # print(number_of_meetups(stones, 7, 27))
    print(number_of_meetups(stones, 200000000000000, 400000000000000))


if __name__ == '__main__':
    solve()
