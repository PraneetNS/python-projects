mat = eval(input())
m, n = len(mat), len(mat[0])

row0 = any(mat[0][j] == 0 for j in range(n))
col0 = any(mat[i][0] == 0 for i in range(m))

for i in range(1, m):
    for j in range(1, n):
        if mat[i][j] == 0:
            mat[i][0] = mat[0][j] = 0

for i in range(1, m):
    for j in range(1, n):
        if mat[i][0] == 0 or mat[0][j] == 0:
            mat[i][j] = 0

if row0:
    for j in range(n):
        mat[0][j] = 0
if col0:
    for i in range(m):
        mat[i][0] = 0

print(mat)
