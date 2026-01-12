import heapq

arr = list(map(int, input().split()))
k = int(input())

heap = []

for x in arr:
    heapq.heappush(heap, x)
    if len(heap) > k:
        heapq.heappop(heap)

print("Top K largest:", heap)
