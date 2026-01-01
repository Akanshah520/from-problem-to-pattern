## Problem 1: Longest Subarray with Sum = K

### Problem Statement
Given an integer array `nums` and an integer `k`, find the **length of the longest contiguous subarray** whose sum equals `k`.

### Why this problem?
This question tests:
- Understanding of contiguous subarrays
- Ability to reason about negative numbers
- Recognition of when sliding window fails
- Use of prefix sums and hashing for optimization

It commonly appears in MLE and SDE interviews due to its strong overlap with:
- Time-series analysis
- Windowed feature aggregation
- Streaming data reasoning

---

### Brute Force Approach
A naive two-loop solution checks all subarrays and computes their sums.

- Time Complexity: `O(n²)`
- Space Complexity: `O(1)`

This approach is correct but inefficient for large inputs.

---

### Optimized Approach (Prefix Sum + HashMap)

**Key Insight:**
If `prefix_sum[j] - prefix_sum[i] = k`,  
then the subarray `(i+1 → j)` sums to `k`.

By storing the **first occurrence** of each prefix sum, we ensure the longest possible subarray.

Sliding window is not applicable here due to the presence of negative numbers, which breaks monotonicity.

