def bfs(graph, start):
    '''
    graph: dictionary
    start: string or number
    '''
    visited = [start]
    queue = [start]
    while queue:
        v = queue.pop(0)
        for w in graph[v]:
            if w not in visited:
                visited.append(w)
                queue.append(w)
    return visited

if __name__ == "__main__":
    test1_graph = {
        'A': ['B', 'C'],
        'B': ['C'],
        'C': ['A', 'D'],
        'D': ['D']
    }
    print(f'graph: {test1_graph}, bfs: {bfs(test1_graph, "A")}')