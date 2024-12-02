"""
    
name: Thomas Cantrell


Welsh-Powell Implementation

Greedy approach which prioritizes neighboring verticies and
selects accepting color option

"""


def greedyColoring(adj, V):
    result = [-1] * V
    result[0] = 0
    
    available = [False] * V
    for u in range(1, V):
        for i in adj[u]:
            if (result[i] != -1):
                available[result[i]] = True

        color = 0
        while color < V:
            if (available[color] == False):
                break
            color += 1
        result[u] = color

        for i in adj[u]:
            if (result[i] != -1):
                available[result[i]] = False
                
    num_colors = max(result) + 1
    print(num_colors)
    for u in range(V):
        print(f"{u} {result[u]}")

def main():
    vertex, e = map(int, input().split())
    adj = [[] for i in range(vertex)]
    for i in range(e):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
        
    greedyColoring(adj, vertex)

if __name__ == "__main__":
    main()