#!/usr/bin/env python3

from collections import defaultdict
from copy import deepcopy
from sys import stdin


class Index():
    name = 'A'

    def __init__(self) -> None:
        self.name = Index.name
        Index.name = Index._increment_name(Index.name)

    @staticmethod
    def _increment_name(name):
        # Helper method to increment the name
        if not name or not name.isalpha():
            raise ValueError("Invalid name format")

        # Convert the string to a list of characters for easier manipulation
        name_list = list(name)

        # Start from the rightmost character and move towards the left
        i = len(name_list) - 1
        while i >= 0:
            if name_list[i] != 'Z':
                # If the character is not 'Z', simply increment it
                name_list[i] = chr(ord(name_list[i]) + 1)
                break
            else:
                # If the character is 'Z', set it to 'A' and move to the previous character
                name_list[i] = 'A'
                i -= 1

        # If all characters were 'Z', add a new 'A' to the left
        if i < 0:
            name_list.insert(0, 'A')

        # Convert the list back to a string
        return ''.join(name_list)


class Brick():
    def __init__(self, str: str) -> None:
        start, end = str.split('~')
        s_x, s_y, s_z = start.split(',')
        e_x, e_y, e_z = end.split(',')
        self.s_x = int(s_x)
        self.s_y = int(s_y)
        self.e_x = int(e_x)
        self.e_y = int(e_y)
        self.s_z = int(s_z)
        self.e_z = int(e_z)
        self.index = Index()

    def __str__(self) -> str:
        return f"{self.s_x},{self.s_y},{self.s_z}~{self.e_x},{self.e_y},{self.e_z}<-{self.index.name}"


def move_down(brick: Brick, placed: set, tile_to_brick: dict):
    for x in range(brick.s_x, brick.e_x + 1):
        for y in range(brick.s_y, brick.e_y + 1):
            for z in range(brick.s_z, brick.e_z + 1):
                placed.remove((x, y, z))
                placed.add((x, y, z-1))
                del tile_to_brick[((x, y, z))]
                tile_to_brick[((x, y, z-1))] = brick.index.name
    brick.s_z -= 1
    brick.e_z -= 1


def settle_bricks(bricks: list[Brick], placed: set, tile_to_brick: dict):
    finished = False
    fallen = set()
    while not finished:
        finished = True
        for brick in bricks:
            if brick.s_z == 1:
                continue
            if brick.s_x != brick.e_x:
                for x in range(brick.s_x, brick.e_x+1):
                    if (x, brick.s_y, brick.s_z - 1) in placed:
                        break
                else:
                    move_down(brick, placed, tile_to_brick)
                    fallen.add(brick.index.name)
                    finished = False
                continue

            if brick.s_y != brick.e_y:
                for y in range(brick.s_y, brick.e_y+1):
                    if (brick.s_x, y, brick.s_z - 1) in placed:
                        break
                else:
                    move_down(brick, placed, tile_to_brick)
                    fallen.add(brick.index.name)
                    finished = False
                continue
            if (brick.s_x, brick.s_y, brick.s_z - 1) not in placed:
                move_down(brick, placed, tile_to_brick)
                fallen.add(brick.index.name)
                finished = False
    return len(fallen)


def solve() -> None:
    input = stdin.read().splitlines()
    bricks = [Brick(x) for x in input]
    bricks.sort(key=lambda x: x.s_z)
    placed = set()
    tile_to_brick = dict()
    for brick in bricks:
        for x in range(brick.s_x, brick.e_x + 1):
            for y in range(brick.s_y, brick.e_y + 1):
                for z in range(brick.s_z, brick.e_z + 1):
                    placed.add((x, y, z))
                    tile_to_brick[(x, y, z)] = brick.index.name

    settle_bricks(bricks, placed, tile_to_brick)

    supported_by = defaultdict(set)
    for brick in bricks:
        if brick.s_z == 1:
            # supported_by[brick.index.name].add('Ground')
            continue
        if brick.s_x != brick.e_x:
            for x in range(brick.s_x, brick.e_x+1):
                if (x, brick.s_y, brick.s_z - 1) in placed:
                    supported_by[brick.index.name].add(
                        tile_to_brick[(x, brick.s_y, brick.s_z - 1)])

            continue
        if brick.s_y != brick.e_y:
            for y in range(brick.s_y, brick.e_y+1):
                if (brick.s_x, y, brick.s_z - 1) in placed:
                    supported_by[brick.index.name].add(
                        tile_to_brick[(brick.s_x, y, brick.s_z - 1)])
            continue
        if (brick.s_x, brick.s_y, brick.s_z - 1) in placed:
            supported_by[brick.index.name].add(
                tile_to_brick[(brick.s_x, brick.s_y, brick.s_z - 1)])

    can_be_removed = set(map(lambda brick: brick.index.name, bricks))
    for brick_name in supported_by:
        if len(supported_by[brick_name]) == 1:
            for name in supported_by[brick_name]:
                if name in can_be_removed:
                    can_be_removed.remove(name)
    print(len(can_be_removed))

    total_score = 0
    for brick in bricks:
        if brick.index.name not in can_be_removed:
            # print(brick.index.name)
            bricks.remove(brick)
            b = deepcopy(bricks)
            p = deepcopy(placed)
            t = deepcopy(tile_to_brick)
            for x in range(brick.s_x, brick.e_x + 1):
                for y in range(brick.s_y, brick.e_y + 1):
                    for z in range(brick.s_z, brick.e_z + 1):
                        p.remove((x, y, z))
                        del t[(x, y, z)]

            total_score += settle_bricks(b, p, t)
            bricks.insert(0, brick)
            # print(total_score)
    print(total_score)


if __name__ == '__main__':
    solve()
