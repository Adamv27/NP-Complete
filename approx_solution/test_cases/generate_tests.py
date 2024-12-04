from itertools import combinations


files_created = 0

def create_graph(num_vertices):
    vertices = list(range(0, num_vertices)) 
    
    edges = combinations(vertices, 2)
    num_edges = 0
    for _ in edges:
        num_edges += 1

    edges = combinations(vertices, 2)
    with open(f'input{files_created}.txt', 'w') as f:
        f.write(f'{num_edges}\n')

        for v,u in edges:
            f.write(f'{v} {u}\n')


for n in range(10, 1000, 50):
    create_graph(n)
    files_created += 1
