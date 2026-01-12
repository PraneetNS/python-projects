def dfs(node):
    visited[node] = True
    print(node, end=" ")
    for nei in graph[node]:
        if not visited[nei]:
            dfs(nei)


n, e = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(e):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * n
dfs(0)
