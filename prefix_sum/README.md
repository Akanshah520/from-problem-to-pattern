# Prefix Sum + HashMap

Prefix Sum is a fundamental pattern used to efficiently compute information over **contiguous subarrays**.

This pattern is especially useful when:
- Subarray constraints are involved
- Negative numbers are present
- Sliding window techniques are not applicable

The core idea is to convert a subarray problem into a relationship between two prefix sums.

---

## Key Insight

If:
prefix_sum[j] - prefix_sum[i] = k

Then:
the subarray (i+1 → j) sums to k

By storing previously seen prefix sums in a hashmap, we can solve subarray problems in linear time.

---

## Problems Covered

### 1. Longest Subarray with Sum = K
**Objective:** Find the maximum length of a contiguous subarray whose sum equals `k`.

- Strategy: Store the **first occurrence** of each prefix sum
- Rationale: Earlier index gives a longer subarray
- Time Complexity: `O(n)`
- Space Complexity: `O(n)`

---

### 2. Subarray Sum Equals K (Count)
**Objective:** Count the total number of contiguous subarrays whose sum equals `k`.

- Strategy: Store the **frequency** of each prefix sum
- Rationale: Multiple valid starting points may exist for the same ending index
- Time Complexity: `O(n)`
- Space Complexity: `O(n)`

---

## Pattern Variations

| Problem Type | HashMap Stores |
|-------------|----------------|
| Longest subarray | First index |
| Count subarrays | Frequency |

This highlights how the **same mathematical invariant** leads to different implementations based on the problem requirement.

---

## Interview Takeaway

Prefix Sum problems are not about memorization.  
They are about identifying invariants and choosing the right auxiliary data structure.

Understanding *what to store* in the hashmap is the key differentiator.

---
