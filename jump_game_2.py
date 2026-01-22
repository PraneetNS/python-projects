nums = list(map(int, input().split()))
jumps = far = end = 0

for i in range(len(nums) - 1):
    far = max(far, i + nums[i])
    if i == end:
        jumps += 1
        end = far

print(jumps)
