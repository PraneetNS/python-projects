def is_valid(arr, students, max_pages):
    count = 1
    pages = 0

    for x in arr:
        if x > max_pages:
            return False
        if pages + x > max_pages:
            count += 1
            pages = x
        else:
            pages += x

    return count <= students


arr = list(map(int, input().split()))
students = int(input())

l, r = max(arr), sum(arr)
ans = r

while l <= r:
    mid = (l + r) // 2
    if is_valid(arr, students, mid):
        ans = mid
        r = mid - 1
    else:
        l = mid + 1

print(ans)
