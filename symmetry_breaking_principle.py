arr = sorted(input().split())
res = [[]]

for x in arr:
    res += [r + [x] for r in res if not r or r[-1] <= x]

print(res)
from collections import deque