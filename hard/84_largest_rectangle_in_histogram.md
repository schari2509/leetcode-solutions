# 84. Largest Rectangle in Histogram

**Difficulty:** Hard  
**Topics:** Array, Stack, Monotonic Stack  

---

## Problem Statement

Given an array of integers `heights` representing the histogram's bar height where the width of each bar is `1`, return *the area of the largest rectangle in the histogram*.

---

## Examples

### Example 1

**Input:**
```text
heights = [2, 1, 5, 6, 2, 3]
```

**Output:**
```text
10
```

**Explanation:**  
The largest rectangle is formed by the bars of heights 5 and 6 (spanning width 2 at height 5), which has an area of `5 * 2 = 10` units.

### Example 2

**Input:**
```text
heights = [2, 4]
```

**Output:**
```text
4
```

---

## Constraints

- `1 <= heights.length <= 10^5`
- `0 <= heights[i] <= 10^4`
