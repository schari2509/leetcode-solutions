# 525. Contiguous Array

**Difficulty:** Medium  
**Topics:** Array, Hash Table, Prefix Sum  

---

## Problem Statement

Given a binary array `nums`, return the maximum length of a contiguous subarray with an equal number of `0` and `1`.

---

## Examples

### Example 1

**Input:**
```text
nums = [0, 1]
```

**Output:**
```text
2
```

**Explanation:**  
`[0, 1]` is the longest contiguous subarray with an equal number of `0` and `1`.

### Example 2

**Input:**
```text
nums = [0, 1, 0]
```

**Output:**
```text
2
```

**Explanation:**  
`[0, 1]` (or `[1, 0]`) is a longest contiguous subarray with equal number of `0` and `1`.

### Example 3

**Input:**
```text
nums = [0, 1, 1, 1, 1, 1, 0, 0, 0]
```

**Output:**
```text
6
```

**Explanation:**  
`[1, 1, 1, 0, 0, 0]` is the longest contiguous subarray with equal number of `0` and `1`.

---

## Constraints

- `1 <= nums.length <= 10^5`
- `nums[i]` is either `0` or `1`.
