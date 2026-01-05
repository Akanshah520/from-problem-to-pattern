def subarrays_divisible_by_k(nums, k):
    prefix_sum = 0
    count = 0
    seen = {0: 1}

    for num in nums:
        prefix_sum += num
        remainder = prefix_sum % k

        # handle negative remainders
        if remainder < 0:
            remainder += k

        count += seen.get(remainder, 0)
        seen[remainder] = seen.get(remainder, 0) + 1

    return count
