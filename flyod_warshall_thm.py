n = int(input())
dist = []

for _ in range(n):
    dist.append(list(map(int, input().split())))

for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

for row in dist:
    print(*row)
