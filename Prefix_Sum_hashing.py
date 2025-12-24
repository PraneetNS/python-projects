arr = list(map(int, input().split()))
k = int(input())

prefix = 0
mp = {0: 1}
count = 0

for x in arr:
    prefix = (prefix + x) % k
    if prefix < 0:
        prefix += k

    count += mp.get(prefix, 0)
    mp[prefix] = mp.get(prefix, 0) + 1

print(count)
