arr = list(map(int, input().split()))
reach = 0

for i in range(len(arr)):
    if i > reach:
        print(False)
        break
    reach = max(reach, i + arr[i])
else:
    print(True)
