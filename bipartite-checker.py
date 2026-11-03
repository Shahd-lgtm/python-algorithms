
from collections import deque

def is_bipartite(graph):
    color = {}

    for node in graph:
        if node not in color:
            color[node] = 0
            queue = deque([node])

            while queue:
                current = queue.popleft()

                for neighbor in graph[current]:
                    if neighbor not in color:
                        color[neighbor] = 1 - color[current]
                        queue.append(neighbor)

                    elif color[neighbor] == color[current]:
                        return False

    return True


# Example Graph
graph = {
    0: [1, 3],
    1: [0, 2],
    2: [1, 3],
    3: [0, 2]
}

if is_bipartite(graph):
    print("The graph is Bipartite")
else:
    print("The graph is NOT Bipartite")
