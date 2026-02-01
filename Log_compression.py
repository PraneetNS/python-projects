s = input()
res = []

i = 0
while i < len(s):
    j = i
    while j < len(s) and s[j] == s[i]:
        j += 1
    res.append(s[i] + str(j - i))
    i = j

print("".join(res))
