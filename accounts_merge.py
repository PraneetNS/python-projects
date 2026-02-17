parent = {}

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    parent[find(x)] = find(y)

accounts = eval(input())
email_to_name = {}

for acc in accounts:
    name = acc[0]
    for email in acc[1:]:
        parent.setdefault(email, email)
        email_to_name[email] = name
        union(acc[1], email)

from collections import defaultdict
groups = defaultdict(list)

for email in parent:
    groups[find(email)].append(email)

res = []
for root, emails in groups.items():
    res.append([email_to_name[root]] + sorted(emails))

print(res)
