def longest_equal_zeros_ones(nums):
    prefix_sum = 0
    max_len = 0
    seen = {0: -1}

    for i, num in enumerate(nums):
        if num == 0:
            prefix_sum -= 1
        else:
            prefix_sum += 1

        if prefix_sum in seen:
            max_len = max(max_len, i - seen[prefix_sum])
        else:
            seen[prefix_sum] = i

    return max_len
