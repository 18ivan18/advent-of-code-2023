#!/usr/bin/env python3

from copy import deepcopy
from sys import stdin


def part1(n_nums):
    for idx in range(len(n_nums) - 2, -1, -1):
        n_nums[idx].append(n_nums[idx][-1] + n_nums[idx + 1][-1])
    return n_nums[0][-1]


def part2(n_nums):
    n_nums[-2].append(n_nums[-2][0])
    for idx in range(len(n_nums) - 3, -1, -1):
        n_nums[idx].insert(0, n_nums[idx][0] - n_nums[idx + 1][0])
    return n_nums[0][0]


def solve() -> None:
    input = stdin.read().splitlines()
    sum1, sum2 = 0, 0
    for x in [list(map(int, y.split())) for y in input]:
        n_nums = [x]
        while not all(map(lambda x: x == 0, n_nums[-1])):
            n_sum = []
            arr = n_nums[-1]
            for idx in range(len(arr) - 1):
                n_sum.append(arr[idx + 1] - arr[idx])
            n_nums.append(n_sum)
        n_nums1, n_nums2 = n_nums, deepcopy(n_nums)
        sum1 += part1(n_nums1)
        sum2 += part2(n_nums2)

    print(sum1)
    print(sum2)


if __name__ == '__main__':
    solve()
