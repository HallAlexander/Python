import heapq

def alg(n, edges, start, end):
    graph = {i: [] for i in range(1, n+1)}

    for u, v, length, c in edges:
        graph[u].append((v, length, c))
        graph[v].append((u, length, c))
    
    pq = [(0, 0, 0, start)]

    best = {i: (float('inf'), float('inf'), float('inf')) for i in graph}
    best[start] = (0, 0, 0)

    while pq:
        t, s, dist, node = heapq.heappop(pq)

        if node == end:
            return f"{dist} {s} {t}"
        if (t, s, dist) > best[node]:
            continue
        for neighbour, length, c in graph[node]:
            nt = t + (c == 2)
            ns = s + (c == 1)
            nd = dist + length
            new_cost = (nt, ns, nd)

            if new_cost < best[neighbour]:
                best[neighbour] = new_cost
                heapq.heappush(pq, (nt, ns, nd, neighbour))
    return 'IMPOSSIBLE'

n, m, st, en = map(int, input().split())
edges = []
for _ in range(int(m)):
    edges.append(tuple(map(int, input().split())))
print(alg(n, edges, st, en))