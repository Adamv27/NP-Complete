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

        # if we have reached marked all edges that means we have covered all edges and therefore we are done
        if len(marked) == len(graph):
            return True

        # Go through every node in the graph as long as it hasnt been marked and attempt to assign it a color
        for node in graph:
            if node not in marked:
                for color in range(min_cols):
                    if can_use(color, node, graph):
                        graph[node][1] = color
                        marked.add(node)

                        valid = determine_color_reccur(graph)

                        # if we found a valid coloring get out
                        if valid:
                            return True

                        # otherwise remove the curr node from marked and set its color to -1 to try and color it again
                        marked.remove(node)
                        graph[node][1] = -1
                        continue
                return False
        return False

    for color in range(
        2, len(graph) + 1
    ):  # start at two colors and work up to the worst case of e colors
        min_cols = color
        if determine_color_reccur(graph):
            break

    print(min_cols)

    for key in graph:
        print(f"{key} {graph[key][1]}")

    # This is the code for the verifier

    # for parent in graph:

    #     children, parent_color = graph[parent]

    #     for child in children:
    #         child_color = graph[child][1]
    #         if parent_color == child_color:
    #             print("false")
    # print("true")

def can_use(color, node, graph):
    for neighbor in graph[node][0]:
        if color == graph[neighbor][1]:
            return False
    return True


if __name__ == "__main__":
    main()
