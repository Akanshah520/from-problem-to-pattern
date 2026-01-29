# Arrays + Hashing

The Arrays + Hashing pattern focuses on using hash-based data structures
(`dict`, `set`) to eliminate redundant work and reduce time complexity.

This pattern is **foundational** and appears implicitly in many higher-level
patterns such as sliding window, prefix sum, and graph traversal.

If this layer is weak, everything built on top of it becomes fragile.

---

## Core Idea

When a problem involves:
- Repeated lookups
- Frequency counting
- Detecting duplicates
- Pairing or matching elements

Hashing can often reduce the time complexity from **O(n²)** to **O(n)**  
by trading extra space for speed.

---

## When to Use This Pattern

Use Arrays + Hashing when:
- You need constant-time lookup
- Order is not important
- You want to avoid nested loops
- You are asked about duplicates, counts, or complements

---

## Problems Covered

### 1. Two Sum
- Uses a hashmap for complement lookup
- Eliminates nested loops
- Canonical example of time–space tradeoff
- Tests fast lookup reasoning

---

### 2. Contains Duplicate
- Uses a set for existence checking
- Returns early on first duplicate
- Reinforces choosing the lightest data structure

---

### 3. Longest Consecutive Sequence
- Uses a set to enable O(1) lookups
- Expands sequences only from valid starting points
- Avoids sorting to maintain O(n) time complexity

---

## Pattern Summary

| Problem Type        | Data Structure | Key Insight                      |
|---------------------|----------------|----------------------------------|
| Pair matching       | HashMap        | Store complements                |
| Duplicate detection | Set            | Existence > counting             |
| Sequence detection  | Set            | Expand only from sequence starts |

---

## Interview Takeaway

Arrays + Hashing problems test whether you:
- Recognize repeated work
- Use memory intentionally
- Choose the simplest structure that solves the problem
- Handle duplicates and edge cases cleanly

Mastering this pattern is non-negotiable for
AI / ML Engineer interviews, as it directly maps to
feature preprocessing, frequency analysis, and fast lookups.

---
