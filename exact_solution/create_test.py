import os

for i in range(6, 15):
    os.mkdir(f".\\test_cases\\test{i}complete")
    with open(
        f".\\test_cases\\test{i}complete\\testInput.txt",
        "w",
    ) as file:
        # 500 verts

        num_verts = i

        file.write(f"{num_verts * (num_verts - 1)}\n")

        for i in range(num_verts):

            for j in range(num_verts):

                if i != j:
                    file.write(f"{i} {j}\n")
