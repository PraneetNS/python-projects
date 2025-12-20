arr = list(map(int, input("Enter numbers: ").split()))

largest = second = float('-inf')

for num in arr:
    if num > largest:
        second = largest
        largest = num
    elif num != largest and num > second:
        second = num

print("Second largest:", second)
