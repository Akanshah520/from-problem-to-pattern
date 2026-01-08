def longest_substring_k_distinct(s, k):
    left = 0
    freq = {}
    max_len = 0

    for right in range(len(s)):
        char = s[right]
        freq[char] = freq.get(char, 0) + 1

        while len(freq) > k:
            left_char = s[left]
            freq[left_char] -= 1
            if freq[left_char] == 0:
                del freq[left_char]
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len
