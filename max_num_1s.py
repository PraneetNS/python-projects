arr = list(map(int, input().split()))

count = max_count = 0

for x in arr:
    if x == 1:
        count += 1
        max_count = max(max_count, count)
    else:
        count = 0

print(max_count)
