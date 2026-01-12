# Two Pointers

The Two Pointers pattern is used to optimize problems on arrays or strings
by traversing the input with **two indices** instead of relying on nested loops.

This pattern is especially effective when:
- The input is **sorted**
- In-place modification is allowed
- Space optimization is required

By carefully controlling pointer movement, many problems can be solved
in linear time with constant extra space.

---

## Core Idea

Instead of fixing one index and searching for the other, two pointers are
moved strategically to maintain an invariant that guarantees correctness.

---

## Types of Two Pointer Techniques

### Same Direction (Slow–Fast)
Both pointers move forward, but at different speeds.

Used when:
- Removing duplicates
- Filtering elements in-place
- Compressing arrays

### Opposite Direction (Left–Right)
Pointers start at opposite ends and move toward each other.

Used when:
- Working with sorted arrays
- Pair-sum problems
- Palindrome checks

---

## Problems Covered

### 1. Remove Duplicates from Sorted Array
- Slow–fast pointer technique
- In-place array modification
- Exploits sorted input to avoid extra space

---
