def permutations(nums):
    result = []
    path = []
    used = [False] * len(nums)

    def backtrack():
        if len(path) == len(nums):
            result.append(path[:])
            return

        for i in range(len(nums)):
            if used[i]:
                continue

            used[i] = True           # choose
            path.append(nums[i])
            backtrack()              # explore
            path.pop()               # undo
            used[i] = False

    backtrack()
    return result
