arr = list(map(int, input().split()))
k = int(input())

prefix = 0
count = 0
mp = {0: 1}

for x in arr:
    prefix += x
    if prefix - k in mp:
        count += mp[prefix - k]
    mp[prefix] = mp.get(prefix, 0) + 1

print(count)
