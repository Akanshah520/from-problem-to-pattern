# Two Pointers

The Two Pointers pattern is used to optimize problems on arrays or strings
by traversing the input with **two indices** instead of relying on nested loops.

This pattern is especially effective when:
- The input is **sorted or ordered**
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
- Symmetry and palindrome checks
- Geometric optimization problems

---

## Problems Covered

### 1. Remove Duplicates from Sorted Array
- Slow–fast pointer technique
- In-place array modification
- Exploits sorted input to avoid extra space

---

### 2. Two Sum II (Sorted Array)
- Left–right pointer technique
- Uses sorted input to eliminate extra space
- Moves pointers deterministically based on sum comparison

---

### 3. Container With Most Water
- Left–right pointer optimization problem
- Moves the pointer with the smaller height
- Demonstrates mathematical reasoning behind pointer movement

---

### 4. Valid Palindrome
- Left–right pointer technique on strings
- Skips irrelevant characters in place
- Tests symmetry and boundary handling

---

## Interview Takeaway

Two pointer problems test whether you:
- Exploit input structure deliberately
- Move pointers with logical justification
- Maintain invariants without extra space

Mastering this pattern demonstrates strong control over
both time and space optimization in interviews.

---
