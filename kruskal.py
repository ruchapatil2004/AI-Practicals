class Graph:
    def __init__(self):
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def kruskals_algorithm(self, vertices):
        self.graph.sort(key=lambda edge: edge[2])
        parent = [i for i in range(vertices)]
        result = []
        for edge in self.graph:
            u, v, w = edge
            parent_u = self.find(parent, u)
            parent_v = self.find(parent, v)
            if parent_u != parent_v:
                result.append(edge)
                self.union(parent, parent_u, parent_v)
        return result

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, x, y):
        x_set = self.find(parent, x)
        y_set = self.find(parent, y)
        parent[x_set] = y_set

def main():
    graph = Graph()

    while True:
        print("\nMenu:")
        print("1. Add Edge")
        print("2. Kruskal's Algorithm")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            u, v, w = map(int, input("Enter the source, destination, and weight (space-separated): ").split())
            graph.add_edge(u, v, w)
        elif choice == '2':
            vertices = max(max(edge[0], edge[1]) for edge in graph.graph) + 1
            mst = graph.kruskals_algorithm(vertices)
            print("Minimum Spanning Tree (Kruskal's Algorithm):")
            for u, v, w in mst:
                print(f"{u} -- {v} : {w}")
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
