s = input()
stack = []
mp = {')':'(', ']':'[', '}':'{'}

for c in s:
    if c in mp.values():
        stack.append(c)
    else:
        if not stack or stack[-1] != mp[c]:
            print(False)
            break
        stack.pop()
else:
    print(not stack)
