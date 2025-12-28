arr = list(map(int, input().split()))
dep = list(map(int, input().split()))

arr.sort()
dep.sort()

i = j = 0
platforms = max_platforms = 0

while i < len(arr):
    if arr[i] <= dep[j]:
        platforms += 1
        max_platforms = max(max_platforms, platforms)
        i += 1
    else:
        platforms -= 1
        j += 1

print(max_platforms)
