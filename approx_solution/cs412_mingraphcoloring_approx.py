"""
    
name: Adam Vinch


DSATUR (Degree of Saturation)

Greedy approach which prioritizes vertices with the highest
saturation degree
    - Number of different colors already assigned to adjacent vertices
"""

from collections import defaultdict
import random


def highest_saturation(graph, colors):
    max_saturation = 0
    max_vertex = random.choice(list(graph.keys()))

    for v in graph:
        num_adjacent_colored = 0
        for u in graph[v]:
            if u in colors:
                num_adjacent_colored += 1

        if num_adjacent_colored > max_saturation:
            max_saturation = num_adjacent_colored
            max_vertex = v
    
    return v


def dsatur(graph):
    colors = {}

    return 0 


def build_graph():
    n = int(input())
    
    graph = defaultdict(set)
    for _ in range(n):
        edges = input().split()                                                                                          
        v = edges.pop(0)
        for u in edges:
            graph[v].add(u)
            graph[u].add(v)

    return graph


if __name__ == "__main__":
    graph = build_graph()
    print(graph)
    min_colors = dsatur(graph)
    print(min_colors)
