# Binary Search

Binary Search is a pattern used to efficiently locate an element or
determine an optimal value by repeatedly halving the search space.

This pattern is applicable when:
- The search space is **sorted or monotonic**
- A decision can be made to discard half the possibilities
- A brute-force solution is too slow

Binary Search is not limited to arrays. It can be applied to
any problem where the answer space has a monotonic property.

---

## Types of Binary Search

### Classic Binary Search (Index-Based)
Searches directly over indices in a sorted array.

Used when:
- The data itself is sorted
- Exact or boundary positions are required

### Binary Search on Answer
Searches over a range of possible answers.

Used when:
- The goal is to minimize or maximize a value
- A feasibility check can validate a candidate answer
- The feasibility condition is monotonic

### 1. Binary Search in a Sorted Array
- Classic index-based binary search
- Establishes loop invariant and boundary correctness
- Foundation for all advanced binary search problems

---

## Problems Covered
- Binary Search (Basic)
