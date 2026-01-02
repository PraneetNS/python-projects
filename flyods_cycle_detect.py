arr = list(map(int, input().split()))

slow = fast = arr[0]

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
