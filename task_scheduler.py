from collections import Counter

tasks = input().split()
n = int(input())

freq = Counter(tasks)
maxf = max(freq.values())
count = list(freq.values()).count(maxf)

ans = max(len(tasks), (maxf - 1) * (n + 1) + count)
print(ans)
