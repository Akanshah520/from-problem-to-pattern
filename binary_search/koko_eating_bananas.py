import math

def min_eating_speed(piles, h):
    left = 1
    right = max(piles)

    while left <= right:
        mid = left + (right - left) // 2

        hours = 0
        for pile in piles:
            hours += math.ceil(pile / mid)

        if hours <= h:
            right = mid - 1
        else:
            left = mid + 1

    return left
