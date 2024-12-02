with open("testInput.txt", "w") as file:
    # 500 verts

    file.write("249500\n")

    for i in range(500):

        for j in range(500):

            if i != j:
                file.write(f"{i} {j}\n")
