n, q = map(int, input().split())
arr = [0] * (n + 1)

for _ in range(q):
    a, b, k = map(int, input().split())
    arr[a-1] += k
    arr[b] -= k

max_val = curr = 0
for x in arr:
    curr += x
    max_val = max(max_val, curr)

print(max_val)
