from collections import defaultdict

shards = [defaultdict(int) for _ in range(3)]

def increment(key):
    shard = hash(key) % len(shards)
    shards[shard][key] += 1

def total(key):
    return sum(shard[key] for shard in shards)

increment("click")
increment("click")
increment("click")

print(total("click"))
