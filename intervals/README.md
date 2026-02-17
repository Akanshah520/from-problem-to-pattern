
# Intervals

The Intervals pattern focuses on problems involving overlapping
ranges and boundary comparisons.

Most interval problems follow a simple structure:
1. Sort intervals by start time
2. Traverse once
3. Merge or evaluate overlaps

This pattern tests greedy reasoning and clean boundary handling.

---

## Core Idea

After sorting by start time, overlapping intervals
will appear next to each other.

Two intervals overlap if:
start_current <= end_previous

---

## Problems Covered

### 1. Merge Intervals
- Sort + greedy merge
- Updates boundaries carefully
- Time complexity: O(n log n)

---

## Takeaway

Interval problems test whether you can:
- Handle boundaries correctly
- Avoid unnecessary nested comparisons
- Recognize greedy opportunities

Sorting first is often the key insight.
