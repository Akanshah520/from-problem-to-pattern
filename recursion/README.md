# Recursion / Backtracking (Light)

The Recursion / Backtracking pattern is used to explore all valid
configurations of a problem by making choices, exploring outcomes,
and undoing those choices safely.


## Core Idea

All backtracking problems follow the same structure:

1. Make a choice
2. Recurse with that choice
3. Undo the choice (backtrack)

A correct base case and clean rollback matter more than clever pruning.

---

## What Interviewers Look For

- Clear base cases
- Correct state updates and rollbacks
- No unnecessary global state
- Ability to explain recursion flow step by step

If you can explain *what the recursive function represents*, you are safe.

---

## Problems Covered

### 1. Subsets
- Canonical backtracking problem
- Explores include / exclude decisions
- Establishes the choose → recurse → undo pattern

---

### 2. Permutations
- Order-sensitive backtracking
- Uses a `used` structure to avoid reuse
- Tests precise state rollback

---

### 3. Combination Sum (Basic)
- Constraint-based backtracking
- Uses remaining sum to prune paths
- Allows reuse of elements while avoiding duplicates

---

### 4. Generate Parentheses
- Validity-constrained backtracking
- Prevents invalid states during recursion
- Tests reasoning about constraints, not brute force

---

## Pattern Summary

| Problem              | Key Technique        |
|----------------------|----------------------|
| Subsets              | Include / exclude    |
| Permutations         | Used tracking        |
| Combination Sum      | Remaining constraint |
| Generate Parentheses | Validity constraint  |

---

## Interview Takeaway

Recursion / Backtracking problems test whether you can:
- Define a correct recursive function
- Maintain valid state throughout recursion
- Backtrack cleanly without side effects
- Explain your approach calmly under observation

---
