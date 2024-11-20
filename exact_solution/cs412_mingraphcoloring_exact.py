"""
    name:  Lorenzo Ashurst

    Honor Code and Acknowledgments:

            This work complies with the JMU Honor Code.

           Comments here on your code and submission.
"""

import itertools


# All modules for CS 412 must include a main method that allows it
# to imported and invoked from other python scripts
def main():

    num_edges = int(input())
    graph = {}

    for _ in range(num_edges):
        parent, child = input().split()
        if parent not in graph:
            graph[parent] = (set(), -1)
        graph[parent][0].add(child)  # add tyhe verticies

    for index, parent in enumerate(graph):
        used_colors = set()

        # Check neighbors and mark their colors as used
        for index, child in enumerate(graph):
            if colors[index] != -1:
                used_colors.add(colors[index])

        # Find the smallest available color
        color = 0
        while True:
            if color not in used_colors:
                colors[index] = color
                break
            color += 1

    # Find the maximum color used (chromatic number)
    chromatic_number = max(colors) + 1
    print(chromatic_number)
    for index, item in enumerate(graph):
        print(f"{item} {colors[index]}")


if __name__ == "__main__":
    main()
