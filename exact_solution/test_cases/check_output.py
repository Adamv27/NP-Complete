import pickle


def main():

    with open("graph_output", "rb") as file:
        graph = pickle.load(file)
        if solver(graph):
            print("correct")
        else:
            print("incorrect")


def solver(graph):
    for parent in graph:

        children, parent_color = graph[parent]

        for child in children:
            child_color = graph[child][1]
            if parent_color == child_color:
                return False
    return True


if __name__ == "__main__":
    main()
