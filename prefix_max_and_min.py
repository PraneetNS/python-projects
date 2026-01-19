arr = list(map(int, input().split()))

min_so_far = arr[0]
ans = 0

for x in arr[1:]:
    ans = max(ans, x - min_so_far)
    min_so_far = min(min_so_far, x)

print(ans)
