def split_array(nums, m):
    left = max(nums)
    right = sum(nums)

    while left < right:
        mid = left + (right - left) // 2

        subarrays = 1
        current_sum = 0

        for num in nums:
            if current_sum + num <= mid:
                current_sum += num
            else:
                subarrays += 1
                current_sum = num

        if subarrays <= m:
            right = mid
        else:
            left = mid + 1

    return left
