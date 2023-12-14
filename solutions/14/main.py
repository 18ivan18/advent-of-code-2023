#!/usr/bin/env python3

from collections import defaultdict
from sys import stdin


def solve() -> None:
    input = [list(x) for x in stdin.read().splitlines()]
    available_slots = defaultdict(list)
    sum = 0
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
                sum += len(input) - slot
            if input[i][j] == 'O':
                sum += len(input) - i

    print(sum)


if __name__ == '__main__':
    solve()
