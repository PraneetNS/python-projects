arr = list(map(int, input().split()))
target = int(input())

mid = len(arr) // 2
left = arr[:mid]
right = arr[mid:]

def gen(nums):
    res = [0]
    for x in nums:
        res += [s + x for s in res]
    return res

L = gen(left)
R = gen(right)
R.sort()

found = False
for s in L:
    import bisect
    idx = bisect.bisect_left(R, target - s)
    if idx < len(R) and R[idx] == target - s:
        found = True
        break

print(found)
