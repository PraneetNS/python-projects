def can_ship(weights, days, cap):
    curr = 0
    d = 1
    for w in weights:
        if w > cap:
            return False
        if curr + w > cap:
            d += 1
            curr = w
        else:
            curr += w
    return d <= days


weights = list(map(int, input().split()))
days = int(input())

l, r = max(weights), sum(weights)
ans = r

while l <= r:
    mid = (l + r) // 2
    if can_ship(weights, days, mid):
        ans = mid
        r = mid - 1
    else:
        l = mid + 1

print(ans)
