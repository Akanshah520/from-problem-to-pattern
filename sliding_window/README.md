# Sliding Window

The Sliding Window pattern is used to optimize problems involving
**contiguous subarrays or substrings** by maintaining a window that
moves through the input without recomputing values from scratch.

This pattern is applicable when:
- The data structure is linear (array or string)
- The window represents a valid subproblem
- Expanding or shrinking the window preserves a clear invariant

---

## Types of Sliding Window

### Fixed-Size Window
The window size is constant and known in advance.
The goal is usually to compute an aggregate (sum, average, max, min).

### Variable-Size Window
The window size changes dynamically based on a condition.
The goal is usually to maximize or minimize window length.

---

## Problems Covered
### 1. Maximum Sum Subarray of Size K
- Fixed-size sliding window
- Maintains window sum incrementally
- Avoids recomputation of overlapping subarrays

### 2. Longest Subarray with Sum ≤ K
- Variable-size sliding window
- Works only for non-negative numbers
- Demonstrates dynamic window contraction


