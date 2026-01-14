def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    px, py = find(x), find(y)
    if px != py:
        parent[py] = px


n, e = map(int, input().split())
edges = []

for _ in range(e):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))

edges.sort()
parent = list(range(n))
mst_cost = 0

for w, u, v in edges:
    if find(u) != find(v):
        union(u, v)
        mst_cost += w

print("MST cost:", mst_cost)
