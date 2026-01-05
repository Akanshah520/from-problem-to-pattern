# Prefix Sum + HashMap

Prefix Sum is a core algorithmic pattern used to efficiently reason about
**contiguous subarrays** by converting repeated range computations into
constant-time lookups.

This pattern becomes essential when:
- Subarray constraints are involved
- Negative numbers are present
- Sliding window techniques are not applicable
- The optimization goal is length, count, or balance

---

## Core Insight

If:

prefix_sum[j] - prefix_sum[i] = k

Then:

the subarray (i + 1 → j) satisfies the required condition.

By storing previously seen prefix sums (or their transformed representations)
in a hashmap, we can reduce brute-force solutions to linear time.

---

## Problems Covered

### 1. Longest Subarray with Sum = K
**Objective:**  
Find the maximum length of a contiguous subarray whose sum equals `k`.

- Strategy: Store the **first occurrence** of each prefix sum
- Reason: Earlier indices yield longer subarrays
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
  - `1` → `+1`
  - `0` → `-1`
- Reduction: Becomes a **longest subarray with sum = 0** problem
- Strategy: Prefix sum with **first occurrence** tracking
- Time Complexity: `O(n)`
- Space Complexity: `O(n)`

---

### 4. Subarray Sums Divisible by K
**Objective:**  
Count the number of contiguous subarrays whose sum is divisible by `k`.

- Key Insight:
  - If two prefix sums have the same remainder modulo `k`,
    the subarray between them is divisible by `k`
- Strategy: Store **remainder frequencies**
- Special Handling: Normalize negative remainders
- Time Complexity: `O(n)`
- Space Complexity: `O(k)`

---

## Pattern Variations Summary

| Problem Requirement | HashMap Stores |
|---------------------|----------------|
| Longest subarray | First index |
| Count subarrays | Frequency |
| Balance condition | First index after transformation |
| Modulo constraint | Remainder frequency |

This demonstrates how the **same invariant** leads to different implementations
based on what the problem asks for.

---
