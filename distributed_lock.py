import time

lock = {"owner": None, "expires": 0}

def acquire(node, ttl=5):
    now = time.time()
    if now > lock["expires"]:
        lock["owner"] = node
        lock["expires"] = now + ttl
        return True
    return False

print(acquire("A"))
print(acquire("B"))
time.sleep(6)
print(acquire("B"))
def release(node):
    if lock["owner"] == node:
        lock["owner"] = None
        lock["expires"] = 0
        return True
    return False