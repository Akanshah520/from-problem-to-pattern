def minimum_window_substring(s, t):
    if not s or not t:
        return ""

    from collections import Counter

    need = Counter(t)
    window = {}
    required = len(need)
    formed = 0

    left = 0
    min_len = float("inf")
    min_window = ""

    for right, char in enumerate(s):
        window[char] = window.get(char, 0) + 1

        if char in need and window[char] == need[char]:
            formed += 1

        while formed == required:
            window_len = right - left + 1
            if window_len < min_len:
                min_len = window_len
                min_window = s[left:right + 1]

            left_char = s[left]
            window[left_char] -= 1
            if left_char in need and window[left_char] < need[left_char]:
                formed -= 1
            left += 1

    return min_window
