arr = list(map(int, input().split()))

candidate = None
count = 0

for x in arr:
    if count == 0:
        candidate = x
        count = 1
    elif x == candidate:
        count += 1
    else:
        count -= 1

# verify
freq = 0
for x in arr:
    if x == candidate:
        freq += 1

if freq > len(arr) // 2:
    print("Majority:", candidate)
else:
    print("No majority element")
