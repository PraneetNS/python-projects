path = input().split('/')
stack = []

for p in path:
    if p == "" or p == ".":
        continue
    elif p == "..":
        if stack:
            stack.pop()
    else:
        stack.append(p)

print("/" + "/".join(stack))
