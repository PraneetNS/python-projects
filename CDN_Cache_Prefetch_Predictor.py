from collections import defaultdict

pairs = input().split()  # sequence: A B C A B
trans = defaultdict(lambda: defaultdict(int))

for i in range(len(pairs)-1):
    trans[pairs[i]][pairs[i+1]] += 1

# Predict next page after "A"
cur = input()
next_page = max(trans[cur], key=trans[cur].get) if trans[cur] else None
print(next_page)
