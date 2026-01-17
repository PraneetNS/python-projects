from collections import deque

def bfs(cap, parent, s, t):
    visited = [False]*len(cap)
    q = deque([s])
    visited[s] = True
    while q:
        u = q.popleft()
        for v in range(len(cap)):
            if not visited[v] and cap[u][v] > 0:
                parent[v] = u
                visited[v] = True
                if v == t:
                    return True
                q.append(v)
    return False


n = int(input())
cap = [list(map(int, input().split())) for _ in range(n)]
s, t = map(int, input().split())

parent = [-1]*n
max_flow = 0

while bfs(cap, parent, s, t):
    flow = float('inf')
    v = t
    while v != s:
        flow = min(flow, cap[parent[v]][v])
        v = parent[v]

    v = t
    while v != s:
        u = parent[v]
        cap[u][v] -= flow
        cap[v][u] += flow
        v = u

    max_flow += flow

print(max_flow)
