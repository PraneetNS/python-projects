nums = list(map(int, input().split()))
res = []

def backtrack(i, path):
    if i == len(nums):
        res.append(path[:])
        return
    backtrack(i+1, path)
    backtrack(i+1, path+[nums[i]])

backtrack(0, [])
print(res)
