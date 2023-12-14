#!/usr/bin/env python3

from collections import defaultdict
from copy import deepcopy
from sys import stdin


def tilt(input: list[list[str]]):
    available_slots = defaultdict(list)
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] == '#':
                available_slots[j] = []
            if input[i][j] == '.':
                available_slots[j].append(i)
            if input[i][j] == 'O' and available_slots[j]:
                slot = available_slots[j].pop(0)
                input[i][j], input[slot][j] = input[slot][j], input[i][j]
                available_slots[j].append(i)
    return input


def rotate(input: list[list[str]]):
    n = len(input)

    for i in range(n):
        for j in range(i + 1, n):
            input[i][j], input[j][i] = input[j][i], input[i][j]

    for i in range(n):
        input[i].reverse()

    return input


def count(input: list[list[str]]):
    sum = 0
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] == 'O':
                sum += len(input) - i
    return sum


def solve() -> None:
    input1 = [list(x) for x in stdin.read().splitlines()]
    input2 = deepcopy(input1)

    # part1
    print(count(tilt(input1)))

    # pat2
    cycles, total_cycles, cache = 0, 1e9, {}
    while cycles < total_cycles:
        state = str(input2)
        if state in cache:
            prev = cycles - cache[state]
            remaining = total_cycles - cycles
            cycles += (remaining//prev) * prev
        cache[state] = cycles
        tilt(input2)   # up
        tilt(rotate(input2))   # left
        tilt(rotate(input2))    # down
        tilt(rotate(input2))    # right
        rotate(input2)
        cycles += 1
    print(count(input2))


if __name__ == '__main__':
    solve()
