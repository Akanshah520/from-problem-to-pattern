# Heap / Priority Queue

The Heap (Priority Queue) pattern is used when you need to efficiently
maintain the smallest or largest element while processing data.

Heaps are commonly used in:
- Top-K problems
- Streaming data
- Scheduling tasks
- Ranking systems
- Merging sorted structures

This pattern tests whether you understand how to maintain
a dynamically ordered subset of elements.

---

## Core Idea

A heap allows:

- Insert in O(log n)
- Remove min/max in O(log n)
- Peek min/max in O(1)

The goal is not to sort everything,
but to maintain only what matters (often size k).

---

## When to Use a Heap

Use a heap when:
- You need the top k elements
- You need the kth smallest/largest
- You need repeated access to the smallest/largest
- You are merging multiple sorted streams

Avoid sorting the entire dataset when you only need partial order.

---

## Problems Covered

### 1. Top K Frequent Elements
- Uses frequency counting + min-heap of size k
- Maintains only the k most frequent elements
- Time complexity: O(n log k)

---

### 2. Kth Largest Element in an Array
- Maintains a min-heap of size k
- Heap root represents kth largest element
- Time complexity: O(n log k)

---

### 3. Merge K Sorted Lists
- Uses a min-heap to always extract the smallest current node
- Efficiently merges k sorted linked lists
- Time complexity: O(n log k)

---

## Pattern Summary

| Problem        | Heap Strategy                     |
|----------------|-----------------------------------|
| Top K Frequent | Min-heap of size k                |
| Kth Largest    | Min-heap of size k                |
| Merge K Lists  | Min-heap with structured elements |

---

## Takeaway

Heap problems test whether you can:

- Recognize partial ordering requirements
- Avoid unnecessary full sorting
- Maintain size constraints correctly
- Explain time complexity improvements clearly

---
