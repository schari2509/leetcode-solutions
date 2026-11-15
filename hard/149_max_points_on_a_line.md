# 149. Max Points on a Line

**Difficulty:** Hard  
**Topics:** Array, Hash Table, Math, Geometry  

---

## Problem Statement

Given an array of `points` where `points[i] = [xi, yi]` represents a point on the X-Y plane, return the **maximum number of points that lie on the same straight line**.

---

## Examples

### Example 1

**Input:**
```text
points = [[1,1],[2,2],[3,3]]
```

**Output:**
```text
3
```

### Example 2

**Input:**
```text
points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
```

**Output:**
```text
4
```

---

## Constraints

- `1 <= points.length <= 300`
- `points[i].length == 2`
- `-10^4 <= xi, yi <= 10^4`
- All the points are **unique**.
