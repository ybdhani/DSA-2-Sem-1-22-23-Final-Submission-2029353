def find_shortest_path(graph, start, end):
    visited = set()
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            for neighbor in graph[vertex]:
                if neighbor == end:
                    return path + [end]
                queue.append((neighbor, path + [neighbor]))
    return None

# Example graph
graph = {'A': ['B', 'C'],
         'B': ['D', 'E'],
         'C': ['F'],
         'D': [],
         'E': ['F'],
         'F': []}

start = 'A'
end = 'F'

shortest_path = find_shortest_path(graph, start, end)

if shortest_path:
    print("The shortest path from", start, "to", end, "is:", shortest_path)
else:
    print("No path from", start, "to", end, "exists.")
