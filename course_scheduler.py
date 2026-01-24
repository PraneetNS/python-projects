from collections import defaultdict

n = int(input())
edges = eval(input())

graph = defaultdict(list)
for u, v in edges:
    graph[u].append(v)

vis = [0] * n

def dfs(u):
    if vis[u] == 1:
        return False
    if vis[u] == 2:
        return True

    vis[u] = 1
    for v in graph[u]:
        if not dfs(v):
            return False
    vis[u] = 2
    return True

print(all(dfs(i) for i in range(n)))
