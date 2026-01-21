s = input()
p = input()

from collections import Counter

p_count = Counter(p)
window = Counter()
res = []
k = len(p)

for i in range(len(s)):
    window[s[i]] += 1

    if i >= k:
        if window[s[i-k]] == 1:
            del window[s[i-k]]
        else:
            window[s[i-k]] -= 1

    if window == p_count:
        res.append(i - k + 1)

print(res)
