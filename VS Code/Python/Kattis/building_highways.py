import heapq

def prim_mst(cities, difficulties):
    if cities == 1:
        return 0
    min_heap = [(0, 0)]
    total_cost = 0
    visited = [False] * cities
    min_cost = [float('inf')] * cities
    min_cost[0] = 0

    while min_heap:
        cost, u = heapq.heappop(min_heap)

        if visited[u]:
            continue

        visited[u] = True
        total_cost += cost

        for v in range(cities):
            if not visited[v]:
                new_cost = difficulties[u] + difficulties[v]
                if new_cost < min_cost[v]:
                    min_cost[v] = new_cost
                    heapq.heappush(min_heap, (new_cost, v))
    return total_cost

cities = int(input())
difficulties = [int(x) for x in input().split()]

min_cost = prim_mst(cities, difficulties)
print(min_cost)
