# 542. 01 Matrix

**Difficulty:** Medium  
**Topics:** Array, Dynamic Programming, Breadth-First Search, Matrix  

---

## Problem Statement

Given an `m x n` binary matrix `mat`, return *the distance of the nearest `0` for each cell*.

The distance between two adjacent cells sharing a common edge is `1`.

---

## Examples

### Example 1

**Input:**
```text
mat = [[0,0,0],[0,1,0],[0,0,0]]
```

**Output:**
```text
[[0,0,0],[0,1,0],[0,0,0]]
```

### Example 2

**Input:**
```text
mat = [[0,0,0],[0,1,0],[1,1,1]]
```

**Output:**
```text
[[0,0,0],[0,1,0],[1,2,1]]
```

---

## Constraints

- `m == mat.length`
- `n == mat[i].length`
- `1 <= m, n <= 10^4`
- `1 <= m * n <= 10^4`
- `mat[i][j]` is either `0` or `1`.
- There is at least one `0` in `mat`.
