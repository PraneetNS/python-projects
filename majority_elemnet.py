arr = list(map(int, input("Enter array: ").split()))

candidate = None
count = 0

for num in arr:
    if count == 0:
        candidate = num
        count = 1
    elif num == candidate:
        count += 1
    else:
        count -= 1

print("Majority element:", candidate)
