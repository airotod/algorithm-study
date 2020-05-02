import heapq as hq

def dijkstra(graph, source):
    dist = {}
    prev = {}
    hqueue = []

    dist[source] = 0
    prev[source] = None

    for v in graph:
        if v != source:
            dist[v] = float('inf')
            prev[v] = None
        hq.heappush(hqueue, (dist[v], v))

    while hqueue:
        cost, u = hq.heappop(hqueue)
        for v in graph[u]:
            alt = dist[u] + graph[u][v]
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                hq.heappush(hqueue, (dist[v], v))

    return dist, prev

if __name__ == "__main__":
    test1_graph = {
        'A': {'B': 1, 'F': 2},
        'B': {'A': 1, 'C': 1},
        'C': {'B': 1, 'D': 1},
        'D': {'C': 1, 'E': 1},
        'E': {'D': 1, 'F': 1},
        'F': {'A': 2, 'E': 1}
    }
    test1_source = 'A'
    # return: ({'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 3, 'F': 2}, {'A': None, 'B': 'A', 'C': 'B', 'D': 'C', 'E': 'F', 'F': 'A'})
    print(f'graph: {test1_graph}, source: {test1_source}, return: {dijkstra(test1_graph, test1_source)}')
