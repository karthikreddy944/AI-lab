
def hill_climbing(start, goal, graph, heuristic):
    current = start
    path = [current]

    while current != goal:
        neighbors = graph[current]

        if not neighbors:
            break

        next_node = min(neighbors, key=lambda x: heuristic[x])

        if heuristic[next_node] >= heuristic[current]:
            break

        current = next_node
        path.append(current)

    print("Path:", path)

    if current == goal:
        print("Goal reached:", goal)
    else:
        print("Goal not reached")


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

heuristic = {
    'A': 7,
    'B': 5,
    'C': 6,
    'D': 4,
    'E': 2,
    'F': 3,
    'G': 0
}

start = input("Enter start node: ")
goal = input("Enter goal node: ")

hill_climbing(start, goal, graph, heuristic)
