"""
    
name: Adam Vinch

"""

from collections import defaultdict
from queue import PriorityQueue


def assign_color(graph, v, colors):
    neighbor_colors = set()
    for u in graph[v]:
        if u in colors:
            neighbor_colors.add(colors[u])

    color = 1
    while color in neighbor_colors:
        color += 1
    
    return color


def color_highest_degree(graph):
    colors = {}

    pq = PriorityQueue() 
    for v in graph:
        degree = len(graph[v])
        pq.put((-degree, v))
    
    while not pq.empty():
        _, v = pq.get()

        color = assign_color(graph, v, colors)
        colors[v] = color

    return colors 


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
    min_colors = color_highest_degree(graph)
    print(len(set(min_colors.values())))
    for key in min_colors:
        print(f'{key} {min_colors[key]}')
