arr = list(map(int, input("Enter sorted array: ").split()))
target = int(input("Enter target: "))

l, r = 0, len(arr) - 1

while l <= r:
    mid = (l + r) // 2
    if arr[mid] == target:
        print("Found at index:", mid)
        break
    elif arr[mid] < target:
        l = mid + 1
    else:
        r = mid - 1
else:
    print("Not found")
