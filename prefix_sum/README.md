# Prefix Sum + HashMap

Prefix Sum is a fundamental pattern used to efficiently compute information over
**contiguous subarrays**.

This pattern is especially useful when:
- Subarray constraints are involved
- Negative numbers are present
- Sliding window techniques are not applicable

The key idea is to convert a subarray problem into a relationship between
**two prefix sums**, enabling linear-time solutions.

---

## Core Insight

If:

prefix_sum[j] - prefix_sum[i] = k

Then:

the subarray (i + 1 → j) has sum = k

By storing previously seen prefix sums in a hashmap, we can avoid redundant
recomputation and optimize brute-force solutions.

---

## Problems Covered

### 1. Longest Subarray with Sum = K
**Objective:**  
Find the maximum length of a contiguous subarray whose sum equals `k`.

- Strategy: Store the **first occurrence** of each prefix sum
- Reason: An earlier index yields a longer subarray
- Time Complexity: `O(n)`
- Space Complexity: `O(n)`

---

### 2. Subarray Sum Equals K (Count)
**Objective:**  
Count the total number of contiguous subarrays whose sum equals `k`.

- Strategy: Store the **frequency** of each prefix sum
- Reason: Multiple valid starting points may exist for the same ending index
- Time Complexity: `O(n)`
- Space Complexity: `O(n)`

---

### 3. Longest Subarray with Equal 0s and 1s
**Objective:**  
Given a binary array, find the length of the longest contiguous subarray
containing an equal number of `0`s and `1`s.

- Transformation:
  - Treat `1` as `+1`
  - Treat `0` as `-1`
- Reduction: Becomes a **longest subarray with sum = 0** problem
- Strategy: Prefix sum with **first occurrence** tracking
- Time Complexity: `O(n)`
- Space Complexity: `O(n)`

---

## Pattern Variations Summary

| Problem Goal | HashMap Stores |
|-------------|----------------|
| Longest length | First index |
| Count of subarrays | Frequency |
| Balance condition | First index after value transformation |

This demonstrates how the **same mathematical invariant** leads to different
implementations depending on what the problem asks for.

---
