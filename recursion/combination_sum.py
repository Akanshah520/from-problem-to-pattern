def combination_sum(candidates, target):
    result = []
    path = []

    def backtrack(start, remaining):
        if remaining == 0:
            result.append(path[:])
            return

        if remaining < 0:
            return

        for i in range(start, len(candidates)):
            path.append(candidates[i])                 # choose
            backtrack(i, remaining - candidates[i])    # explore (reuse allowed)
            path.pop()                                 # undo

    backtrack(0, target)
    return result
