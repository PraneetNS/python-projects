n = int(input())
reach = [list(map(int, input().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if reach[i][k] and reach[k][j]:
                reach[i][j] = 1

for row in reach:
    print(*row)
