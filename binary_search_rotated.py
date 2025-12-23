arr = list(map(int, input().split()))
target = int(input())

l, r = 0, len(arr) - 1

while l <= r:
    mid = (l + r) // 2

    if arr[mid] == target:
        print(mid)
        break

    if arr[l] <= arr[mid]:
        if arr[l] <= target < arr[mid]:
            r = mid - 1
        else:
            l = mid + 1
    else:
        if arr[mid] < target <= arr[r]:
            l = mid + 1
        else:
            r = mid - 1
else:
    print(-1)
