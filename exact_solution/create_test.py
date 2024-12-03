with open("testInput.txt", "w") as file:
    # 500 verts

    num_verts = 10

    file.write(f"{num_verts * (num_verts - 1)}\n")

    for i in range(num_verts):

        for j in range(num_verts):

            if i != j:
                file.write(f"{i} {j}\n")
