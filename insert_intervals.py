intervals = eval(input())
newInterval = eval(input())

res = []

for i in range(len(intervals)):
    if newInterval[1] < intervals[i][0]:
        res.append(newInterval)
        res.extend(intervals[i:])
        break
    elif newInterval[0] > intervals[i][1]:
        res.append(intervals[i])
    else:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
else:
    res.append(newInterval)

print(res)
