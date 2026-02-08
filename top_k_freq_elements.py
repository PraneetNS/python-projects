import heapq
from collections import Counter
def top_k_frequent(nums, k):
    count = Counter(nums)
    heap = []

    for key, value in count.items():
        if len(heap) < k:
            heapq.heappush(heap, (value, key))
        else:
            heapq.heappushpop(heap, (value, key))
    return [key for value, key in heap]
        