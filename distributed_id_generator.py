import time

EPOCH = 1700000000
machine_id = 3
seq = 0

def generate_id():
    global seq
    ts = int(time.time()) - EPOCH
    seq = (seq + 1) & 4095
    return (ts << 22) | (machine_id << 12) | seq

print(generate_id())
print(generate_id())
