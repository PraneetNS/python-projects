from collections import deque

v, e = map(int, input("Vertices Edges: ").split())
graph = [[] for _ in range(v)]
indegree = [0] * v

for _ in range(e):
    u, vtx = map(int, input().split())
    graph[u].append(vtx)
    indegree[vtx] += 1

q = deque()
for i in range(v):
    if indegree[i] == 0:
        q.append(i)

result = []

while q:
    node = q.popleft()
    result.append(node)
    for nei in graph[node]:
        indegree[nei] -= 1
        if indegree[nei] == 0:
            q.append(nei)

if len(result) == v:
    print("Topological Order:", result)
else:
    print("Cycle exists")
