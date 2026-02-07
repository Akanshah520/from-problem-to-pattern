def subsets(nums):
    result = []
    path = []

    def backtrack(start):
        # record the current subset
        result.append(path[:])

        for i in range(start, len(nums)):
            path.append(nums[i])        # choose
            backtrack(i + 1)            # explore
            path.pop()                  # undo (backtrack)

    backtrack(0)
    return result
