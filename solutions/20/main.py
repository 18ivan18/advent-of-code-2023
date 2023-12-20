#!/usr/bin/env python3

from sys import stdin
from math import lcm


modules = dict()

state = dict()

lows = 0
highs = 0
button_presses = 0

cycles = dict()


def visit(modules_to_signal: list, to_visit: list, signal: str, f: str):
    global lows, highs, button_presses
    for module in modules_to_signal:
        if signal == 'low':
            lows += 1
        else:
            highs += 1
        # ultra input sensitive
        if signal == 'high' and module == 'lb':
            print(module, signal, f, button_presses)
            cycles[f] = button_presses
        if module not in modules:
            return
        to_visit.append((module, signal))
        if modules[module][0] == '&':
            state[module][f] = signal


def send_signal(name: str, signal: str, to_visit: list):
    module_type, next = modules[name]
    if module_type == '%':
        if signal == 'high':
            return
        if state[name] == 'off':
            state[name] = 'on'
            return visit(next, to_visit, 'high', name)
        if state[name] == 'on':
            state[name] = 'off'
            return visit(next, to_visit, 'low', name)
    if module_type == '&':
        only_highs = True
        for x in state[name]:
            if state[name][x] == 'low':
                only_highs = False
                break
        if only_highs:
            return visit(next, to_visit, 'low', name)
        else:
            return visit(next, to_visit, 'high', name)

    # broadcaster sends low
    return visit(next, to_visit, 'low', name)


def solve() -> None:
    input = stdin.read().splitlines()
    for x in input:
        name, targets = x.split(' -> ')
        all_targets = targets.split(', ')
        if name.startswith('%') or name.startswith('&'):
            modules[name[1:]] = (name[0], all_targets)
            if name.startswith('%'):
                state[name[1:]] = 'off'
            if name.startswith('&'):
                state[name[1:]] = dict()
            continue
        modules[name] = (name, all_targets)
    for x in input:
        name, targets = x.split(' -> ')
        all_targets = targets.split(', ')
        for target in all_targets:
            if target in modules and modules[target][0] == '&':
                state[target][name[1:]] = 'low'
    modules['button'] = ('button', ['broadcaster'])

    global button_presses
    while True:
        if button_presses == 1000:
            print(lows, highs, lows*highs)
        button_presses += 1
        to_visit = [('button', 'low')]
        while to_visit:
            name, signal = to_visit.pop(0)
            send_signal(name, signal, to_visit)
        # very input sensitive
        if len(cycles) == 4:
            print(lcm(*cycles.values()))
            break


if __name__ == '__main__':
    solve()
