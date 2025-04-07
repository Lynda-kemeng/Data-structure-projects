import heapq

def dijkstra(n, edges, start, end, required_edges):
    graph = {i: [] for i in range(1, n + 1)}
    edge_map = {}
    for idx, (u, v, w) in enumerate(edges, start=1):
        graph[u].append((v, w, idx))
        graph[v].append((u, w, idx))
        edge_map[(u, v)] = edge_map[(v, u)] = idx

    required_edge_set = set(required_edges)

    pq = [(0, start, frozenset())]
    visited = set()
    while pq:
        cost, node, covered_edges = heapq.heappop(pq)

        if node == end and required_edge_set.issubset(covered_edges):
            return cost

        state = (node, covered_edges)
        if state in visited:
            continue
        visited.add(state)

        for neighbor, weight, edge_idx in graph[node]:
            new_cost = cost + weight
            new_covered_edges = covered_edges | ({edge_idx} if edge_idx in required_edge_set else frozenset())
            heapq.heappush(pq, (new_cost, neighbor, new_covered_edges))

    return -1

def main():
    n, m, q = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))

    queries = []
    for _ in range(q):
        k = int(input())
        required_edges = list(map(int, input().split()))
        queries.append(required_edges)

    paths = []
    for _ in range(q):
        s, t = map(int, input().split())
        paths.append((s, t))

    results = []
    for required_edges, (start, end) in zip(queries, paths):
        result = dijkstra(n, edges, start, end, required_edges)
        results.append(result)

    for result in results:
        print(result)

if __name__ == "__main__":
    main()
