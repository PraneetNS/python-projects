import heapq
from collections import Counter

posts = input().split()
k = int(input())

freq = Counter(posts)
heap = []

for post, score in freq.items():
    heapq.heappush(heap, (-score, post))

res = []
for _ in range(k):
    res.append(heapq.heappop(heap)[1])

print(res)
