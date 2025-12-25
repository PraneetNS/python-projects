arr = list(map(int, input().split()))
n = len(arr)

res = 0
for i in range(n + 1):
    res ^= i

for x in arr:
    res ^= x

print(res)
