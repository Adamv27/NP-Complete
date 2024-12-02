"""
    name:  Lorenzo Ashurst

    Honor Code and Acknowledgments:

            This work complies with the JMU Honor Code.

           Comments here on your code and submission.
"""


# All modules for CS 412 must include a main method that allows it
# to imported and invoked from other python scripts
def main():

    num_edges = int(input())
    graph = {}

    for _ in range(num_edges):
        parent, child = input().split()
        if parent not in graph:
            graph[parent] = [set(), -1]  # each verticies have an initial -1 color
        if child not in graph:
            graph[child] = [set(), -1]  # each verticies have an initial -1 color

        graph[child][0].add(parent)  # add the verticies

        graph[parent][0].add(child)  # add the verticies

    min_cols = 2
    marked = set()

    def determine_color_reccur(graph):

        nonlocal min_cols, marked

        if len(marked) == len(graph):
            return True

        for node in graph:
            if node not in marked:
                for color in range(min_cols):
                    if can_use(color, node, graph):
                        graph[node][1] = color
                        marked.add(node)

                        valid = determine_color_reccur(graph)

                        if valid:
                            return True

                        marked.remove(node)
                        graph[node][1] = -1
                        continue
                return False
        return False

    while True:
        if not determine_color_reccur(graph) or min_cols != len(graph):
            min_cols += 1
        else:
            break

    for key in graph:
        print(f"{key} {graph[key][1]}")


def can_use(color, node, graph):

    for neighbor in graph[node][0]:
        if color == graph[neighbor][1]:
            return False

    return True


if __name__ == "__main__":
    main()
