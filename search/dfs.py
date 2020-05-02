def dfs(graph, start):
    '''
    graph: dictionary
    start: string or number
    '''
    visited = [start]
    stack = [start]
    while stack:
        v = stack.pop()
        for w in graph[v]:
            if w not in visited:
                visited.append(w)
                stack.append(w)
    return visited

if __name__ == "__main__":
    test1_graph = {
        'A': ['B', 'C'],
        'B': ['C'],
        'C': ['A', 'D'],
        'D': ['D']
    }
    print(f'graph: {test1_graph}, dfs: {dfs(test1_graph, "A")}')