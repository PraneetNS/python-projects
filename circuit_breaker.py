failures = 0
OPEN = False

def call():
    global failures, OPEN
    if OPEN:
        return "BLOCKED"

    failures += 1
    if failures >= 3:
        OPEN = True
    return "FAIL"

for _ in range(5):
    print(call())
print("Circuit is now open:", OPEN)