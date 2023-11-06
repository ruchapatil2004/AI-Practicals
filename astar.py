def astaralgo(start_node, stop_node):
    open_set = {start_node}
    closed_set = set()
    g = {}
    parents = {}
    g[start_node] = 0
    parents[start_node] = start_node
    while open_set:
        n = None
        for v in open_set:
            if n is None or (g[v] + heuristic(v) < g[n] + heuristic(n)):
                n = v
        if n is None:
            print("Path does not exist...")
            return None
        if n == stop_node:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()
            print("Path found: {}".format(path))
            return path
        open_set.remove(n)
        closed_set.add(n)
        for (m, weight) in get_neighbours(n):
            if m in closed_set:
                continue
            tentative_g = g[n] + weight 
            if m not in open_set or tentative_g < g[m]:
                open_set.add(m)
                g[m] = tentative_g
                parents[m] = n
    print("Path does not exist...")
    return None
def get_neighbours(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None
def heuristic(n):
    H_dist = {
        'A': 1,
        'B': 3,
        'C': 6,
        'D': 2,
        'E': 8,
        'F': 4
    }
    return H_dist[n]
Graph_nodes = {
    'A': [('B', 10), ('C', 5)],
    'B': [('D', 7)],
    'C': [('D', 1), ('E', 3)],
    'D': [('E', 6), ('F', 2)],
    'E': [('F', 9)]
}
astaralgo('A', 'F')