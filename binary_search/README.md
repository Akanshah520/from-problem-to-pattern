# Binary Search

Binary Search is a pattern used to efficiently locate an element or
determine an optimal value by repeatedly halving the search space.

This pattern applies whenever:
- The search space is **sorted or monotonic**
- A decision can eliminate half the possibilities
- A brute-force approach is too slow

Binary Search is not limited to arrays. It can be applied to any problem
where the **answer space itself is monotonic**.

---

## Types of Binary Search

### Classic Binary Search (Index-Based)
Searches directly over indices in a sorted array.

Used when:
- The data itself is sorted
- Exact matches are required

---

### Boundary Binary Search
Used to find **positions or ranges**, not just exact matches.

Used when:
- Finding first or last occurrence
- Determining insertion index
- Handling duplicates correctly

---

### Binary Search on Answer
Searches over a **range of possible answers** rather than array indices.

Used when:
- The goal is to minimize or maximize a value
- A feasibility check can validate a candidate
- The feasibility condition is monotonic

---

## Problems Covered

### 1. Binary Search in a Sorted Array
- Classic index-based binary search
- Establishes loop invariant and termination correctness
- Foundation for all other variants

---

### 2. First and Last Position of Element in Sorted Array
- Boundary-based binary search
- Finds leftmost and rightmost occurrences
- Tests off-by-one and invariant control

---

### 3. Search Insert Position
- Boundary binary search variant
- Finds correct insertion index if target is not present
- Reinforces `left` pointer as the insertion boundary

---

### 4. Koko Eating Bananas
- Binary search on answer
- Uses feasibility checking
- Demonstrates monotonic decision space

---

### 5. Split Array Largest Sum
- Binary search on answer with partitioning
- Uses greedy feasibility check
- Canonical workload allocation problem

---

## Pattern Summary

| Problem Type    | What is Binary Searched       |
|-----------------|-------------------------------|
| Exact search    | Array indices                 |
| Boundary search | Index range / insertion point |
| Optimization    | Answer space                  |
| Feasibility     | Decision outcome (yes/no)     |

---

## Interview Takeaway

Binary Search problems test whether you can:
- Identify monotonicity
- Maintain strict invariants
- Handle boundaries without off-by-one errors
- Separate feasibility logic from optimization goals
---
