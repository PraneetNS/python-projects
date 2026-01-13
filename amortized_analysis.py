arr = list(map(int, input().split()))
stack = []
res = [-1] * len(arr)

for i in range(len(arr)):
    while stack and arr[i] > arr[stack[-1]]:
        res[stack.pop()] = arr[i]
    stack.append(i)

print(res)
# Example usage:
# Input: 2 1 2 4 3