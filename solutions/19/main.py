#!/usr/bin/env python3

from sys import stdin
import re

rules_dict = dict()
begin = 'in'


class Example():
    def __init__(self, line: str) -> None:
        self.x, self.m, self.a, self.s = re.findall('(\d+)', line)

    def value(self):
        return int(self.x) + int(self.m) + int(self.a) + int(self.s)

    def get(self, value: str):
        if value == 'x':
            return self.x
        if value == 'm':
            return self.m
        if value == 'a':
            return self.a
        if value == 's':
            return self.s
        raise Exception()


class Rule():
    def __init__(self, line: str):
        name, rest = line.split('{')
        self.name = name
        rules_dict[name] = self
        self.rules = rest[:-1].split(',')

    def fit_example(self, example: Example):
        for r in self.rules[:-1]:
            category, comp_sign, comp, go_to = re.findall(
                '(\w+)([<>])(\w+):(\w+)', r)[0]
            evl = eval(f"{example.get(category)}{comp_sign}{comp}")
            if evl:
                return go_to
        return self.rules[-1]


def is_accepted(example: Example, starting_rule: str = begin):
    rule = starting_rule
    while rule != 'A' and rule != 'R':
        rule = rules_dict[rule].fit_example(example)
    return rule == 'A'


def fit_range(example: Example, starting_rule: str = begin):
    pass


def solve() -> None:
    rules, examples = stdin.read().split('\n\n')
    rules = [Rule(x) for x in rules.splitlines()]
    examples = [Example(x) for x in examples.splitlines()]
    print(sum([example.value()
          for example in examples if is_accepted(example)]))
    print(sum(map(fit_range, examples)))


if __name__ == '__main__':
    solve()
