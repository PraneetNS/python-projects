arr = list(map(int, input().split()))
l, r = 0, len(arr) - 1

while l <= r:
    if arr[l] < 0:
        l += 1
    elif arr[r] >= 0:
        r -= 1
    else:
        arr[l], arr[r] = arr[r], arr[l]

print(arr)
