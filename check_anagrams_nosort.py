s1 = input()
s2 = input()

if len(s1) != len(s2):
    print(False)
else:
    count = {}

    for ch in s1:
        count[ch] = count.get(ch, 0) + 1

    for ch in s2:
        if ch not in count:
            print(False)
            break
        count[ch] -= 1
        if count[ch] == 0:
            del count[ch]
    else:
        print(True)
