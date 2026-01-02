arr = list(map(int, input().split()))
res = 0

for x in arr:
    res ^= x

print("Unique element:", res)
