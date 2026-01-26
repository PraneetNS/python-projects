class LRUCache:
    def __init__(self, cap):
        self.cap = cap
        self.cache = {}
        self.order = []

    def get(self, key):
        if key not in self.cache:
            return -1
        self.order.remove(key)
        self.order.append(key)
        return self.cache[key]

    def put(self, key, val):
        if key in self.cache:
            self.order.remove(key)
        elif len(self.cache) == self.cap:
            old = self.order.pop(0)
            del self.cache[old]

        self.cache[key] = val
        self.order.append(key)


c = LRUCache(2)
c.put(1, 10)
c.put(2, 20)
c.get(1)
c.put(3, 30)
print(c.cache)
