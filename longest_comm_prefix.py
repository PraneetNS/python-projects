arr = input().split()

prefix = arr[0]

for word in arr[1:]:
    i = 0
    while i < len(prefix) and i < len(word) and prefix[i] == word[i]:
        i += 1
    prefix = prefix[:i]

print(prefix)
