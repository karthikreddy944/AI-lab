
def astar(graph, start, goal, heuristic):
    open_list = [(heuristic[start], 0, start)]
    visited = set()
    parent = {}

    while open_list:
        open_list.sort()
        f, g, node = open_list.pop(0)

        if node == goal:
            path = []
            while node in parent:
                path.append(node)
                node = parent[node]
            path.append(start)
            path.reverse()
            print("Path:", path)
            print("Total cost:", g)
            return

        if node in visited:
            continue

        visited.add(node)

        for child, cost in graph[node]:
            if child not in visited:
                new_g = g + cost
                new_f = new_g + heuristic[child]
                parent[child] = node
                open_list.append((new_f, new_g, child))

    print("Goal not found")


graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5)],
    'D': [],
    'E': [('G', 2)],
    'F': [('G', 2)],
    'G': []
}

heuristic = {
    'A': 5,
    'B': 4,
    'C': 4,
    'D': 3,
    'E': 2,
    'F': 1,
    'G': 0
}

start = input("Enter start node: ")
goal = input("Enter goal node: ")

astar(graph, start, goal, heuristic)
