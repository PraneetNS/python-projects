arr = list(map(int, input("Enter array: ").split()))

slow = arr[0]
fast = arr[0]

while True:
    slow = arr[slow]
    fast = arr[arr[fast]]
    if slow == fast:
        break

slow = arr[0]
while slow != fast:
    slow = arr[slow]
    fast = arr[fast]

print("Duplicate:", slow)
