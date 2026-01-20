arr = list(map(int, input().split()))
x = int(input())

arr.sort(key=lambda v: abs(v - x))
print(arr)
