import heapq

low, high = [], []

nums = list(map(int, input().split()))
for x in nums:
    heapq.heappush(low, -x)
    heapq.heappush(high, -heapq.heappop(low))

    if len(high) > len(low):
        heapq.heappush(low, -heapq.heappop(high))

    if len(low) == len(high):
        print((-low[0] + high[0]) / 2)
    else:
        print(-low[0])
