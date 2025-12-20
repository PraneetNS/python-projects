s = input("Enter string: ")
visited = ""

for ch in s:
    if ch not in visited:
        count = 0
        for c in s:
            if c == ch:
                count += 1
        print(ch, "=", count)
        visited += ch
