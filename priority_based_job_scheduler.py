import heapq

pq = []

def submit(job, priority):
    heapq.heappush(pq, (-priority, job))

def execute():
    if pq:
        return heapq.heappop(pq)[1]

submit("job1", 1)
submit("job2", 5)
submit("job3", 3)

print(execute())
print(execute())
