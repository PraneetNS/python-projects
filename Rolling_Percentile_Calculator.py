import bisect

data = []

def add(val):
    bisect.insort(data, val)

def percentile(p):
    idx = int(len(data) * p)
    return data[min(idx, len(data)-1)]

for x in [100,200,150,400,120]:
    add(x)

print("P95:", percentile(0.95))
