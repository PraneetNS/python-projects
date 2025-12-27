n = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]

# transpose
for i in range(n):
    for j in range(i, n):
        mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

# reverse rows
for i in range(n):
    mat[i].reverse()

for row in mat:
    print(*row)
