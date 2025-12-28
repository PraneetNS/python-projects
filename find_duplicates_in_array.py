arr = list(map(int, input().split()))
res = []

for i in range(len(arr)):
    idx = abs(arr[i]) - 1
    if arr[idx] < 0:
        res.append(abs(arr[i]))
    else:
        arr[idx] = -arr[idx]

print(res)
