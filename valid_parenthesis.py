s = input("Enter parentheses: ")
stack = []

pairs = {')': '(', '}': '{', ']': '['}
valid = True

for ch in s:
    if ch in '({[':
        stack.append(ch)
    elif ch in ')}]':
        if not stack or stack[-1] != pairs[ch]:
            valid = False
            break
        stack.pop()

if stack:
    valid = False

print("Valid" if valid else "Invalid")
