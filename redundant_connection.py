edges = eval(input())

parent = {}

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    px,py = find(x),find(y)
    if px==py:
        return False
    parent[px] = py
    return True

for u,v in edges:
    parent.setdefault(u,u)
    parent.setdefault(v,v)
    if not union(u,v):
        print([u,v])
        break