arr = list(map(int, input().split()))

mp = {0: -1}
prefix = 0
best = 0

for i, x in enumerate(arr):
    prefix += -1 if x == 0 else 1
    if prefix in mp:
        best = max(best, i - mp[prefix])
    else:
        mp[prefix] = i

print(best)