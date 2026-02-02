# Linked List (Basic)

The Linked List pattern focuses on **pointer manipulation**, **edge-case handling**,
and maintaining correctness while modifying a mutable data structure.

Unlike arrays, linked lists do not allow random access, so correctness depends
entirely on how references (`next` pointers) are updated.

This pattern is tested to evaluate **clarity of thought**, not clever tricks.

---

## Core Idea

Every linked list problem reduces to:
- Knowing what each pointer represents
- Updating pointers in the correct order
- Handling `None` safely

Most bugs in linked list problems are **pointer bugs**, not algorithmic ones.

---

## What Interviewers Look For

- Clean pointer updates
- Correct handling of edge cases (head, tail, single node)
- Use of dummy nodes where appropriate
- Ability to explain pointer movement calmly

Recursion is optional; **iterative solutions are preferred** unless recursion is explicitly requested.

---

## Problems Covered

### 1. Reverse Linked List
- Fundamental pointer manipulation problem
- Reverses the list in-place
- Establishes basic pointer discipline

---

### 2. Merge Two Sorted Lists
- Iterative merge using a dummy node
- Reuses existing nodes (no extra allocation)
- Tests ordered traversal and pointer updates

---

### 3. Linked List Cycle
- Uses Floyd’s Tortoise and Hare algorithm
- Detects cycles using fast and slow pointers
- Avoids extra memory usage

---

### 4. Remove Nth Node From End of List
- Uses two pointers with a fixed gap
- Handles head removal safely using a dummy node
- Tests off-by-one and boundary awareness

---

## Pattern Summary

| Problem             | Key Technique             |
|---------------------|---------------------------|
| Reverse Linked List | Pointer reversal          |
| Merge Two Lists     | Dummy node + tail pointer |
| Cycle Detection     | Fast & slow pointers      |
| Remove Nth Node     | Two-pointer gap           |

---

## Interview Takeaway

Linked List problems test whether you can:
- Think clearly while mutating a structure
- Track multiple pointers without confusion
- Handle edge cases without special casing everywhere
---
