arr = list(map(int, input().split()))
n = len(arr) - 1

expected_sum = n * (n + 1) // 2
actual_sum = sum(arr)

print("Duplicate:", actual_sum - expected_sum)
