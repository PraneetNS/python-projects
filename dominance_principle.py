pairs = eval(input())  # [(cost, time)]

pairs.sort()
best_time = float('inf')
res = []

for c, t in pairs:
    if t < best_time:
        res.append((c, t))
        best_time = t

print(res)
