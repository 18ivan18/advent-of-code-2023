#!/usr/bin/env python3

from sys import stdin
import networkx as nx
from itertools import combinations


def solve() -> None:
    input = stdin.read().splitlines()
    G = nx.Graph()
    for x in input:
        f, t = x.split(': ')
        rest = t.split(' ')
        for vertex in rest:
            G.add_edge(f, vertex, capacity=1)
    for source, sink in combinations(G.nodes, 2):
        cut_value, partition = nx.minimum_cut(G, source, sink)
        reachable, non_reachable = partition
        if cut_value == 3:
            print(len(reachable) * len(non_reachable))
            # print(cut_value, partition, reachable, non_reachable)
            break


if __name__ == '__main__':
    solve()
