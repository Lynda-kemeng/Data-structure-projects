import heapq
import math

def find_min(n, m, s, t, edges):
    graph = {i: [] for i in range(1, n + 1)}
    for u, v, ai in edges:
        graph[u].append((v, ai))
        graph[v].append((u, ai))

    pq = [(0, 0, s)]
    visited = set()

    while pq:
        current_hp, current_sp, current_node = heapq.heappop(pq)
        if current_node == t:
            return current_hp
        state = (current_node, current_sp)
        if state in visited:
            continue
        visited.add(state)

        for neighbor, ai in graph[current_node]:
            next_sp = current_sp + 1
            next_hp = current_hp + math.floor(ai / (current_sp + 1))
            heapq.heappush(pq, (next_hp, next_sp, neighbor))

    return -1

def main():
    n, m, t, s  = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v, ai = map(int, input().split())
        edges.append((u, v, ai))

    result = find_min(n, m, s, t, edges)
    print(result)

if __name__ == "__main__":
    main()
