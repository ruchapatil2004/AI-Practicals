V = int(input("Enter the number of vertices: "))

G = []
for _ in range(V):
    row = [int(x) for x in input(f"Enter {V} space-separated values for the {V} edges connected to this vertex: ").split()]
    G.append(row)

selected = [False] * V
no_edge = 0
selected[0] = True

print("Edge : Weight\n")
while no_edge < V - 1:
    minimum = float('inf')
    x = 0
    y = 0
    for i in range(V):
        if selected[i]:
            for j in range(V):
                if not selected[j] and G[i][j] > 0:
                    if minimum > G[i][j]:
                        minimum = G[i][j]
                        x = i
                        y = j
    print(f"{x}-{y}:{G[x][y]}")
    selected[y] = True
    no_edge += 1
