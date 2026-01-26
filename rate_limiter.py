import time

class RateLimiter:
    def __init__(self, rate, capacity):
        self.rate = rate
        self.capacity = capacity
        self.tokens = capacity
        self.last = time.time()

    def allow(self):
        now = time.time()
        elapsed = now - self.last
        self.last = now

        self.tokens = min(self.capacity, self.tokens + elapsed * self.rate)

        if self.tokens >= 1:
            self.tokens -= 1
            return True
        return False


rl = RateLimiter(rate=5, capacity=10)

for _ in range(15):
    print(rl.allow())
