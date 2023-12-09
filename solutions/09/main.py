#!/usr/bin/env python3

from sys import stdin


def solve() -> None:
    input = stdin.read().splitlines()
    sum = 0
    for x in [list(map(int, y.split())) for y in input]:
        n_nums = [x]
        while not all(map(lambda x: x == 0, n_nums[-1])):
            n_sum = []
            arr = n_nums[-1]
            for idx in range(len(arr) - 1):
                n_sum.append(arr[idx + 1] - arr[idx])
            n_nums.append(n_sum)
        for idx in range(len(n_nums) - 2, -1, -1):
            n_nums[idx].append(n_nums[idx][-1] + n_nums[idx + 1][-1])
        sum += n_nums[0][-1]
    print(sum)


if __name__ == '__main__':
    solve()
