def longest_subarray_sum_k(nums, k):
    prefix_sum = 0
    max_len = 0
    seen = {0: -1}  # prefix_sum : index

    for i, num in enumerate(nums):
        prefix_sum += num

        if (prefix_sum - k) in seen:
            length = i - seen[prefix_sum - k]
            max_len = max(max_len, length)

        if prefix_sum not in seen:
            seen[prefix_sum] = i  # store earliest occurrence only

    return max_len
