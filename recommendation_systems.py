users = {
    "A": {"x", "y", "z"},
    "B": {"x", "y"},
    "C": {"y", "z"}
}

target = "B"
scores = {}

for u, items in users.items():
    if u != target:
        scores[u] = len(users[target] & items)

print(max(scores, key=scores.get))
