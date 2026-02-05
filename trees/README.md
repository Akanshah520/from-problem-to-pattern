# Trees (Shallow but Common)

Tree problems test whether you can reason recursively and handle
hierarchical data structures with clarity.

For AI / ML Engineer interviews, the focus is **not** on advanced tree
algorithms, but on:
- Correct traversal
- Clear base cases
- Knowing when to use DFS vs BFS

This pattern is about **structural thinking**, not optimization tricks.

---

## Core Idea

Most tree problems can be solved by:
1. Defining a clear base case
2. Solving the problem for the left and right subtrees
3. Combining the results

If you understand this recursive structure, tree problems become predictable.

---

## Traversal Types

### Depth-First Search (DFS)
Used when:
- The problem is naturally recursive
- You want to process subtrees independently

Common DFS orders:
- Inorder (Left → Root → Right)
- Preorder (Root → Left → Right)
- Postorder (Left → Right → Root)

---

### Breadth-First Search (BFS)
Used when:
- Processing nodes level by level
- Distance or level information matters

Implemented using a queue.

---

## Problems Covered

### 1. Binary Tree Inorder Traversal
- Basic DFS traversal
- Establishes recursion structure
- Foundation for all tree problems

---

### 2. Maximum Depth of Binary Tree
- Recursive depth computation
- Reinforces base case discipline
- Tests subtree result combination

---

### 3. Same Tree
- Structural and value comparison
- Pure recursive definition
- Tests correctness of base cases

---

### 4. Invert Binary Tree
- Structural transformation problem
- Swaps left and right subtrees
- Reinforces recursive mutation

---

### 5. Binary Tree Level Order Traversal
- Breadth-first traversal (BFS)
- Processes nodes level by level
- Uses a queue to manage traversal state

---

## Pattern Summary

| Problem               | Technique |
|-----------------------|-----------|
| Inorder Traversal     | DFS       |
| Maximum Depth         | DFS       |
| Same Tree             | DFS       |
| Invert Tree           | DFS       |
| Level Order Traversal | BFS       |

---

## Interview Takeaway

Tree problems test whether you can:
- Think recursively without confusion
- Handle base cases correctly
- Choose between DFS and BFS deliberately
- Explain your approach calmly and clearly

---
