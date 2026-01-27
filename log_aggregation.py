from collections import Counter
import heapq

logs = input().split()
k = int(input())

freq = Counter(logs)
heap = []

for err, c in freq.items():
    heapq.heappush(heap, (-c, err))

print([heapq.heappop(heap)[1] for _ in range(k)])
