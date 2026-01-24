from collections import deque

begin = input()
end = input()
words = set(input().split())

q = deque([(begin, 1)])
visited = set([begin])

while q:
    word, steps = q.popleft()
    if word == end:
        print(steps)
        break
    for i in range(len(word)):
        for c in "abcdefghijklmnopqrstuvwxyz":
            nxt = word[:i] + c + word[i+1:]
            if nxt in words and nxt not in visited:
                visited.add(nxt)
                q.append((nxt, steps + 1))
else:
    print(0)
