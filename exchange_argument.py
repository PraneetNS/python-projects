intervals = eval(input())  # [[start, end], ...]

intervals.sort(key=lambda x: x[1])
count = 1
last_end = intervals[0][1]

for s, e in intervals[1:]:
    if s >= last_end:
        count += 1
        last_end = e

print(count)
# The code reads a list of intervals, sorts them by their end times,
# and counts the maximum number of non-overlapping intervals using a greedy approach.