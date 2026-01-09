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
Used when the problem asks for an aggregate over a fixed range.

### Variable-Size Window
The window size changes dynamically based on a condition.
Used when the goal is to maximize or minimize window length
while maintaining a constraint.

---

## Problems Covered

### 1. Maximum Sum Subarray of Size K
**Objective:**  
Find the maximum sum of any contiguous subarray of size `k`.

- Window Type: Fixed-size
- Strategy: Maintain window sum by adding the entering element and
  removing the exiting element
- Time Complexity: `O(n)`
- Space Complexity: `O(1)`

---

### 2. Longest Subarray with Sum ≤ K
**Objective:**  
Find the length of the longest contiguous subarray whose sum is
less than or equal to `k`.

- Window Type: Variable-size
- Constraint: All elements must be non-negative
- Strategy: Expand the window greedily and shrink it when the
  sum constraint is violated
- Time Complexity: `O(n)`
- Space Complexity: `O(1)`
-
### 3. Longest Substring with At Most K Distinct Characters
- Variable-size sliding window on strings
- Uses character frequency map
- Demonstrates window validity based on distinct count


