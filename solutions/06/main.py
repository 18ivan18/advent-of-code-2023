#!/usr/bin/env python3

from functools import reduce
import operator
from sys import stdin


def process_race(race):
    time, distance = race
    number_of_ways = 0
    for i in range(time):
        max = i * (time - i)
        if max > distance:
            number_of_ways += 1
    return number_of_ways


def solve() -> None:
    input = stdin.read().splitlines()
    races = [list(map(int, x.split(':')[1].split())) for x in input]
    races = list(zip(races[0], races[1]))
    race = [int(x.split(':')[1].replace(' ', '')) for x in input]
    print(reduce(operator.mul, [process_race(race) for race in races], 1))
    print(process_race(race))


if __name__ == '__main__':
    solve()
