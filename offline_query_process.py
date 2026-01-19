arr = list(map(int, input().split()))
queries = eval(input())  # [(l,r),...]

queries.sort()
res = []

for l, r in queries:
    res.append(sum(arr[l:r+1]))

print(res)
