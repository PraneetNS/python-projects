from collections import defaultdict, deque

words = input().split()
graph = defaultdict(set)
indegree = {}

for w in words:
    for c in w:
        indegree[c] = 0

for i in range(len(words)-1):
    w1, w2 = words[i], words[i+1]
    for c1, c2 in zip(w1, w2):
        if c1 != c2:
            if c2 not in graph[c1]:
                graph[c1].add(c2)
                indegree[c2] += 1
            break

q = deque([c for c in indegree if indegree[c]==0])
res = []

while q:
    c = q.popleft()
    res.append(c)
    for nei in graph[c]:
        indegree[nei] -= 1
        if indegree[nei]==0:
            q.append(nei)

print("".join(res) if len(res)==len(indegree) else "")