import random

def trial():
    seen = set()
    for _ in range(23):
        b = random.randint(1, 365)
        if b in seen:
            return True
        seen.add(b)
    return False

count = 0
for _ in range(10000):
    if trial():
        count += 1

print("Probability:", count / 10000)
