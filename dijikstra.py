class Graph:
    def __init__(self):
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def dijkstras_algorithm(self, vertices, src):
        dist = [float('inf')] * vertices
        dist[src] = 0
        visited = [False] * vertices

        for _ in range(vertices):
            u = self.min_dist(dist, visited)
            visited[u] = True

            for v, w in self.get_neighbours(u):
                if not visited[v] and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        return dist

    def min_dist(self, dist, visited):
        min_val = float('inf')
        min_index = -1
        for v in range(len(dist)):
            if not visited[v] and dist[v] < min_val:
                min_val = dist[v]
                min_index = v
        return min_index

    def get_neighbours(self, u):
        neighbours = []
        for edge in self.graph:
            if edge[0] == u:
                neighbours.append((edge[1], edge[2]))
            elif edge[1] == u:
                neighbours.append((edge[0], edge[2]))
        return neighbours

def main():
    graph = Graph()

    while True:
        try:
            input_str = input("Enter the source, destination, and weight, or enter -1 to finish: ")
            if input_str == "-1":
                break
            u, v, w = [int(x) for x in input_str.split()]
            graph.add_edge(u, v, w)
        except ValueError:
            print("Invalid input")

    src = int(input("Enter the source vertex: "))
    vertices = max(max(edge[0], edge[1]) for edge in graph.graph) + 1
    dist = graph.dijkstras_algorithm(vertices, src)
    print("Shortest Distances (Dijkstra's Algorithm):")
    for v in range(vertices):
        print(f"Distance from {src} to {v}: {dist[v]}")

if __name__ == "__main__":
    main()
