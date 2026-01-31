processed = set()

def write(req_id, data):
    if req_id in processed:
        return "IGNORED"
    processed.add(req_id)
    return "WRITTEN"

print(write("1","x"))
print(write("1","x"))
