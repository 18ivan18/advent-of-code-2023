#!/usr/bin/env python3
from sys import stdin
import re

def get_digits(x: str):
    return re.sub('\D+', '', x)

def solve() -> None:
    input = stdin.read().splitlines()
    print(sum([int(get_digits(x)[0] + get_digits(x)[-1]) for x in input]))
    


if __name__ == '__main__':
    solve()
