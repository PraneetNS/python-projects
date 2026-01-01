arr = list(map(int, input().split()))
l, r = 0, len(arr) - 1
max_area = 0

while l < r:
    area = min(arr[l], arr[r]) * (r - l)
    max_area = max(max_area, area)

    if arr[l] < arr[r]:
        l += 1
    else:
        r -= 1

print("Max area:", max_area)
