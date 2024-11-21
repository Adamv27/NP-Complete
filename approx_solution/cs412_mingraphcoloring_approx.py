"""
    
name: Adam Vinch


DSATUR (Degree of Saturation)

Greedy approach which prioritizes vertices with the highest
saturation degree
    - Number of different colors already assigned to adjacent vertices
"""

from collections import defaultdict
from queue import PriorityQueue
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
    
    return max_vertex


def assign_color(graph, v, colors):
    neighbor_colors = set()
    for u in graph[v]:
        if u in colors:
            neighbor_colors.add(colors[u])

    #neighbor_colors = {colors[neighbor] for neighbor in graph[v] if neighbor in colors}
    
    color = 1
    while color in neighbor_colors:
        color += 1
    
    return color


def dsatur(graph):
    colors = {}
    
    while len(colors) != len(graph):
        v = highest_saturation(graph, colors)
        color = assign_color(graph, v, colors)
        print(f'assigning vertex: {v} color: {color}')
        colors[v] = color

    return set(colors.values()) 


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
    #min_colors = dsatur(graph)
    print(min_colors)
