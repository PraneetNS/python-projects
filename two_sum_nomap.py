arr = list(map(int, input("Enter array: ").split()))
target = int(input("Target: "))

found = False

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] == target:
            print(i, j)
            found = True
            break
    if found:
        break
