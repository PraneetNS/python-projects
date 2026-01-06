parent = []
rank = []

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    px = find(x)
    py = find(y)

    if px != py:
        if rank[px] < rank[py]:
            parent[px] = py
        elif rank[px] > rank[py]:
            parent[py] = px
        else:
            parent[py] = px
            rank[px] += 1


n = int(input("Number of nodes: "))
parent = list(range(n))
rank = [0] * n

edges = int(input("Edges: "))
for _ in range(edges):
    u, v = map(int, input().split())
    union(u, v)

print("Parents:", parent)
