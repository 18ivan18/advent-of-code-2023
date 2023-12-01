#!/usr/bin/env python3
from sys import stdin
import re

def solve() -> None:
    input = stdin.read().splitlines()
    pattern_digits = re.compile(r'(\d)')
    print(sum([int(pattern_digits.findall(x)[0] + pattern_digits.findall(x)[-1]) for x in input]))
    pattern_digits_and_words = re.compile(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))')
    m = dict()

    for idx, x in enumerate(["one","two","three","four","five","six","seven","eight","nine"], 1):
        m[str(idx)] = str(idx)
        m[x] = str(idx)

    print(sum([int(m[pattern_digits_and_words.findall(x)[0]] + m[pattern_digits_and_words.findall(x)[-1]]) for x in input]))

if __name__ == '__main__':
    solve()