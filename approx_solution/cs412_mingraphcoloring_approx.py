"""
    
name: Adam Vinch

"""

from collections import defaultdict
from queue import PriorityQueue
import random


def assign_color(graph, v, colors):
    neighbor_colors = set()
    for u in graph[v]:
        if u in colors:
            neighbor_colors.add(colors[u])

    color = 1
    while color in neighbor_colors:
        color += 1
    
    return color


def color_lowest_degree(graph):
    colors = {}

    pq = PriorityQueue() 
    for v in graph:
        degree = len(graph[v])
        pq.put((-degree, v))
    
    while not pq.empty():
        _, v = pq.get()

        color = assign_color(graph, v, colors)
        print(f'assigning vertex: {v} color: {color}')
        colors[v] = color

    
    return set(colors.values()) 


def color_highest_degree(graph):
    colors = {}

    pq = PriorityQueue() 
    for v in graph:
        degree = len(graph[v])
        pq.put((-degree, v))
    
    while not pq.empty():
        _, v = pq.get()

        color = assign_color(graph, v, colors)
        print(f'assigning vertex: {v} color: {color}')
        colors[v] = color

    
    return set(colors.values()) 


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
    min_colors = color_highest_degree(graph)
    print(min_colors)
