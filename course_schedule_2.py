from collections import defaultdict, deque

n = int(input())
edges = eval(input())

graph = defaultdict(list)
indegree = [0]*n

for u,v in edges:
    graph[u].append(v)
    indegree[v] += 1

q = deque([i for i in range(n) if indegree[i] == 0])
res = []

while q:
    node = q.popleft()
    res.append(node)
    for nei in graph[node]:
        indegree[nei] -= 1
        if indegree[nei] == 0:
            q.append(nei)

print(res if len(res) == n else [])
