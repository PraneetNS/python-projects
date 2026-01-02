arr = list(map(int, input().split()))
n = len(arr)
res = [-1] * n
stack = []

for i in range(n):
    while stack and arr[i] > arr[stack[-1]]:
        idx = stack.pop()
        res[idx] = arr[i]
    stack.append(i)

print("Next greater:", res)
