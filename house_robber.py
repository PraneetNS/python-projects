nums = list(map(int, input().split()))
rob1 = rob2 = 0

for n in nums:
    new = max(rob1 + n, rob2)
    rob1 = rob2
    rob2 = new

print(rob2)
