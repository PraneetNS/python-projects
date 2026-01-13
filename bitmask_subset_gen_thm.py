arr = input().split()
n = len(arr)

for mask in range(1 << n):
    subset = []
    for i in range(n):
        if mask & (1 << i):
            subset.append(arr[i])
    print(subset)
# Example usage:
# Input: a b c