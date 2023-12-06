#!/usr/bin/env python3

from sys import stdin


def create_map(line):
    return [[int(y) for y in x.split()] for x in line.splitlines()[1:]]


def to_pairs(l):
   return list(zip(l[::2], l[1::2]))

def trace(x, maps):
  for m in maps:
    # destination start range, source range, range length 
    for s, sr, rl in m:
        if sr + rl - 1 >= x and sr <= x:
            x = x - sr + s
            break
  return x

def solve():
    input = stdin.read().split('\n\n')
    seeds = list(map(int, input[0].split(': ')[1].split()))
    maps = [create_map(x) for x in input[1:]]
    print(min(trace(x, maps) for x in seeds))

    res = float('inf')
    for start, length in to_pairs(seeds):
        for x in range(start, start + length):
            res=min(res,trace(x, maps))
    print(res)


if __name__ == '__main__':
    solve()
