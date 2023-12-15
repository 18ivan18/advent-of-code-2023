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

    boxes = []
    for _ in range(256):
        boxes.append(dict())

    for x in input:
        if '=' in x:
            label, lens = x.split('=')
            index = hash(label)
            box = boxes[index]
            box[label] = int(lens)
            continue
        if '-' in x:
            label = x[:-1]
            index = hash(label)
            box = boxes[index]
            if label in box:
                box.pop(label)

    s = 0
    for idx, x in enumerate(boxes):
        if len(x) == 0:
            continue
        focus = 0
        for slot, y in enumerate(x.values()):
            focus += (idx+1)*y*(slot+1)
        s += focus
    print(s)


if __name__ == '__main__':
    solve()
    # test()
