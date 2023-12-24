#!/usr/bin/env python3

from sys import stdin
from z3 import Solver, Real, sat


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
            # print(i, j, paths_crossed_x, paths_crossed_y)
            if min <= paths_crossed_x <= max and min <= paths_crossed_y <= max:
                r += 1
    return r


def solve2(stones: list[Hailstore]):
    # Create Z3 variables
    pxs0, vxs0, pys0, vys0, pzs0, vzs0, t01, t02, t03 = \
        Real('pxs0'), Real('vxs0'), Real('pys0'), Real('vys0'), Real('pzs0'), Real('vzs0'), \
        Real('t01'), Real('t02'), Real('t03')

    eq1 = pxs0+(vxs0-stones[0].v_x)*t01-stones[0].p_x == 0
    eq2 = pys0+(vys0-stones[0].v_y)*t01-stones[0].p_y == 0
    eq3 = pzs0+(vzs0-stones[0].v_z)*t01-stones[0].p_z == 0

    eq4 = pxs0+(vxs0-stones[1].v_x)*t02-stones[1].p_x == 0
    eq5 = pys0+(vys0-stones[1].v_y)*t02-stones[1].p_y == 0
    eq6 = pzs0+(vzs0-stones[1].v_z)*t02-stones[1].p_z == 0

    eq7 = pxs0+(vxs0-stones[2].v_x)*t03-stones[2].p_x == 0
    eq8 = pys0+(vys0-stones[2].v_y)*t03-stones[2].p_y == 0
    eq9 = pzs0+(vzs0-stones[2].v_z)*t03-stones[2].p_z == 0

    solver = Solver()

    solver.add(eq1, eq2, eq3, eq4, eq5, eq6, eq7, eq8, eq9)

    if solver.check() == sat:
        model = solver.model()

        pxs0_val = model[pxs0].as_decimal(10)
        vxs0_val = model[vxs0].as_decimal(10)
        pys0_val = model[pys0].as_decimal(10)
        vys0_val = model[vys0].as_decimal(10)
        pzs0_val = model[pzs0].as_decimal(10)
        vzs0_val = model[vzs0].as_decimal(10)
        # t01_val = model[t01].as_decimal(10)
        # t02_val = model[t02].as_decimal(10)
        # t03_val = model[t03].as_decimal(10)

        print(f"pxs0: {pxs0_val}, vxs0: {vxs0_val}")
        print(f"pys0: {pys0_val}, vys0: {vys0_val}")
        print(f"pzs0: {pzs0_val}, vzs0: {vzs0_val}")
        # print(f"t01: {t01_val}, t02: {t02_val}, t03: {t03_val}")
        # TODO: debug later
        # this does not work for some reason
        # return pxs0_val+pys0_val+pzs0_val
    else:
        print("No solution found.")


def solve() -> None:
    input = stdin.read().splitlines()
    stones = [Hailstore(x) for x in input]
    # print(number_of_meetups(stones, 7, 27))
    print(number_of_meetups(stones, 200000000000000, 400000000000000))
    print(solve2(stones))


if __name__ == '__main__':
    solve()
