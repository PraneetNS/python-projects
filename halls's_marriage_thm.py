def bpm(u, seen, matchR):
    for v in graph[u]:
        if not seen[v]:
            seen[v] = True
            if matchR[v] == -1 or bpm(matchR[v], seen, matchR):
                matchR[v] = u
                return True
    return False


n_left, n_right = map(int, input().split())
graph = [[] for _ in range(n_left)]

edges = int(input())
for _ in range(edges):
    u, v = map(int, input().split())
    graph[u].append(v)

matchR = [-1] * n_right
result = 0

for i in range(n_left):
    seen = [False] * n_right
    if bpm(i, seen, matchR):
        result += 1

print("Maximum matching:", result)
