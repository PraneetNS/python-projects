import time
from collections import defaultdict

class FixedWindowLimiter:
    def __init__(self, limit):
        self.limit = limit
        self.window = defaultdict(int)

    def allow(self, user):
        now = int(time.time())
        key = (user, now)
        self.window[key] += 1
        return self.window[key] <= self.limit


rl = FixedWindowLimiter(3)
for _ in range(5):
    print(rl.allow("u1"))
