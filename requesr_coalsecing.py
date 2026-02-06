from collections import defaultdict

inflight = defaultdict(list)

def request(key, cb):
    if key in inflight:
        inflight[key].append(cb)
        return

    inflight[key].append(cb)
    result = f"result_for_{key}"

    for f in inflight[key]:
        f(result)
    del inflight[key]


def callback(res):
    print("Got:", res)

request("A", callback)
request("A", callback)
request("B", callback)
request("B", callback)