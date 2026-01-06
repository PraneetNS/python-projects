import heapq

n, e = map(int, input("Nodes Edges: ").split())
graph = [[] for _ in range(n)]

for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

src = int(input("Source: "))
dist = [float('inf')] * n
dist[src] = 0

pq = [(0, src)]

while pq:
    d, node = heapq.heappop(pq)
    if d > dist[node]:
        continue

    for nei, w in graph[node]:
        if dist[nei] > d + w:
            dist[nei] = d + w
            heapq.heappush(pq, (dist[nei], nei))

print("Distances:", dist)
