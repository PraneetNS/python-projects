items = [
    ("post1", 0.9, 100),
    ("post2", 0.7, 200),
    ("post3", 0.9, 50)
]

items.sort(key=lambda x: (-x[1], -x[2]))

print(items)
