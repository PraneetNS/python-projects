s = input().strip()
count = 0

for ch in reversed(s):
    if ch == ' ':
        break
    count += 1

print(count)
