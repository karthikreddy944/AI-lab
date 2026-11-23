
def dls(graph, node, goal, depth, visited):
    if node == goal:
        return True

    if depth <= 0:
        return False

    visited.append(node)

    for child in graph[node]:
        if child not in visited:
            if dls(graph, child, goal, depth - 1, visited):
                return True

    return False


def ids(graph, start, goal, max_depth):
    for depth in range(max_depth + 1):
        visited = []
        print("Depth:", depth)

        if dls(graph, start, goal, depth, visited):
            print("Goal found:", goal)
            print("Path:", visited)
            return

    print("Goal not found")


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

start = input("Enter start node: ")
goal = input("Enter goal node: ")
max_depth = int(input("Enter maximum depth: "))

ids(graph, start, goal, max_depth)
