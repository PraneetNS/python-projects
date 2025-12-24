arr = list(map(int, input().split()))
n = len(arr)
res = [0] * n
stack = []

for i in range(n):
    while stack and arr[i] > arr[stack[-1]]:
        idx = stack.pop()
        res[idx] = i - idx
    stack.append(i)

print(res)
