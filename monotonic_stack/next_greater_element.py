def next_greater_element(nums):
    n = len(nums)
    result = [-1] * n
    stack = []  # will store indices

    for i in range(n):
        while stack and nums[i] > nums[stack[-1]]:
            idx = stack.pop()
            result[idx] = nums[i]
        stack.append(i)

    return result
