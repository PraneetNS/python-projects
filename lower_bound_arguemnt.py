def merge_sort(a):
    if len(a) <= 1:
        return a
    mid = len(a)//2
    return sorted(merge_sort(a[:mid]) + merge_sort(a[mid:]))

print(merge_sort(list(map(int, input().split()))))
