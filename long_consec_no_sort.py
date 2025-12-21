arr = list(map(int, input("Enter array: ").split()))
longest = 0

for num in arr:
    if num - 1 not in arr:
        current = num
        count = 1

        while current + 1 in arr:
            current += 1
            count += 1

        longest = max(longest, count)

print("Longest sequence length:", longest)
