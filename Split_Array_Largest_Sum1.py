nums = list(map(int, input().split()))
m = int(input())

def can(mid):
    count = 1
    total = 0
    for n in nums:
        total += n
        if total > mid:
            count += 1
            total = n
    return count <= m

l, r = max(nums), sum(nums)

while l < r:
    mid = (l+r)//2
    if can(mid):
        r = mid
    else:
        l = mid+1

print(l)