# Monotonic Stack

The Monotonic Stack pattern is used to solve problems where the relationship
between elements depends on their **relative order** rather than absolute position.

A stack is maintained such that its elements are always in a specific order
(either increasing or decreasing). This allows certain comparisons to be resolved
efficiently in linear time, avoiding nested loops.

---

## Core Idea

Each element is:
- Pushed onto the stack once
- Popped from the stack at most once

This guarantees an overall **O(n)** time complexity.

The stack maintains a strict invariant:
- Either **monotonically increasing**, or
- **Monotonically decreasing**

depending on what kind of dependency we want to resolve.

---

## Types of Monotonic Stacks

### Monotonically Increasing Stack
Used when finding:
- Next smaller element
- Previous smaller element
- Width-based or area-based boundaries

Typical use cases:
- Histogram problems
- Range expansion problems

---

### Monotonically Decreasing Stack
Used when finding:
- Next greater element
- Previous greater element
- Dependency resolution based on larger values

Typical use cases:
- Stock prices
- Temperature problems
- Span-based queries

---

## Problems Covered

### 1. Next Greater Element
- Monotonically decreasing stack
- Resolves future dependencies to the right
- Value-based result
- Each element waits until a greater element appears

---

### 2. Daily Temperatures
- Monotonically decreasing stack of indices
- Computes distance to the next greater element
- Index-based extension of Next Greater Element

---

### 3. Largest Rectangle in Histogram
- Monotonically increasing stack
- Computes left and right boundaries using nearest smaller elements
- Capstone problem for monotonic stack reasoning
- Combines width and height calculations

---

### 4. Stock Span Problem
- Monotonically decreasing stack
- Uses previous greater element logic
- Reinforces left-side dependency handling
- Computes consecutive span efficiently

---

## Pattern Summary

| Problem Type         | Stack Order | Dependency Direction |
|----------------------|-------------|----------------------|
| Next Greater Element | Decreasing  | Right                |
| Daily Temperatures   | Decreasing  | Right                |
| Largest Rectangle    | Increasing  | Both                 |
| Stock Span           | Decreasing  | Left                 |

---

## Interview Takeaway

Monotonic Stack problems test whether you can:
- Maintain strict stack invariants
- Resolve dependencies without redundant comparisons
- Convert nested-loop logic into linear-time solutions
- Reason clearly about **order, boundaries, and blocking elements**

If you can explain *why* the stack is monotonic and *when* elements are popped,
you are already ahead of most candidates.

Mastering this pattern unlocks a wide class of
order-dependent interview problems.

---
