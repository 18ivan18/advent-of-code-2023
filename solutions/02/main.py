#!/usr/bin/env python3

import re
from sys import stdin
from functools import reduce
import operator

game_pattern = re.compile(r'Game (\d+): ')
cubes_pattern = re.compile(r'(\d+) (\w+)')


class Game():
    def __init__(self, x: str, red_cubes: int, blue_cubes: int, green_cubes: int) -> None:
        self.cubes = {"red": red_cubes,
                      "blue": blue_cubes, "green": green_cubes}
        self.maxs = {"red": 0,
                     "blue": 0, "green": 0}
        self.possible = True
        _, id, rest = game_pattern.split(x)
        self.id = int(id)
        for amount, color in cubes_pattern.findall(rest):
            if int(amount) > self.cubes[color]:
                self.possible = False

            if int(amount) > self.maxs[color]:
                self.maxs[color] = int(amount)

    def get_id(self):
        return self.id if self.possible else 0

    def get_min_cubes_required(self):
        return reduce(operator.mul, list(self.maxs.values()), 1)


def solve() -> None:
    input = stdin.read().splitlines()
    games = [Game(x, red_cubes=12, blue_cubes=14, green_cubes=13)
             for x in input]
    print(sum([game.get_id() for game in games]))
    print(sum([game.get_min_cubes_required() for game in games]))


if __name__ == '__main__':
    solve()
