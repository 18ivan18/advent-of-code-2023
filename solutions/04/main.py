#!/usr/bin/env python3

from collections import defaultdict
from sys import stdin


class Card():
    def __init__(self, input: str) -> None:
        _, numbers = input.split(": ")
        winning, my = numbers.split('|')
        self.winning_numbers = set([int(x) for x in winning.split()])
        self.my_numbers = [int(x) for x in my.split()]


def process_cards(cards: Card):
    instances = defaultdict(lambda: 1)
    for i, card in enumerate(cards):
        matching = 0
        for x in card.my_numbers:
            if x in card.winning_numbers:
                matching += 1
        for j in range(matching):
            instances[i+1+j] += instances[i]
        card.score = 0 if matching == 0 else 2 ** (matching - 1)
        card.instances = instances[i]


def solve() -> None:
    input = stdin.read().splitlines()
    cards = [Card(x) for x in input]
    process_cards(cards)
    print(sum([card.score for card in cards]))
    print(sum([card.instances for card in cards]))


if __name__ == '__main__':
    solve()
