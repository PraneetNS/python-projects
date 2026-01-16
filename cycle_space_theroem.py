def dfs(node):
    visited[node] = True
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
components = 0

for i in range(n):
    if not visited[i]:
        dfs(i)
        components += 1

cycles = e - n + components
print("Number of cycles:", cycles)
