class SessionStore:
    def __init__(self, cap):
        self.cap = cap
        self.data = {}
        self.order = []

    def access(self, sid):
        if sid in self.data:
            self.order.remove(sid)
        else:
            if len(self.data) == self.cap:
                old = self.order.pop(0)
                del self.data[old]
            self.data[sid] = True
        self.order.append(sid)

    def get_active(self):
        return list(self.order)


s = SessionStore(3)
s.access("A")
s.access("B")
s.access("C")
s.access("A")
s.access("D")
print(s.get_active())
