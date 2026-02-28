matrix = eval(input())
if not matrix:
    print(0)
    exit()

m, n = len(matrix), len(matrix[0])
heights = [0]*n
max_area = 0

for row in matrix:
    for j in range(n):
        heights[j] = heights[j] + 1 if row[j] == "1" else 0

    stack = []
    for i in range(n+1):
        cur = heights[i] if i < n else 0
        while stack and heights[stack[-1]] > cur:
            h = heights[stack.pop()]
            w = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h * w)
        stack.append(i)

print(max_area)