def permute(nums):
    res = []

    def backtrack(path):
        if len(path) == len(nums):
            res.append(path.copy())
            return
        for n in nums:
            if n not in path:
                path.append(n)
                backtrack(path)
                path.pop()

    backtrack([])
    return res