#!/usr/bin/env python3

from sys import stdin


def hash(line: str):
    h = 0
    for s in line:
        h += ord(s)
        h *= 17
        h %= 256
    return h


def test():
    assert (hash("HASH") == 52)
    assert (hash("cm-") == 253)
    assert (hash("qp=3") == 97)


def solve() -> None:
    input = stdin.read().split(',')
    print(sum(map(hash, input)))


if __name__ == '__main__':
    solve()
    # test()
