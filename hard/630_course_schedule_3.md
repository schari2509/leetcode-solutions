# 630. Course Schedule III

**Difficulty:** Hard  
**Topics:** Array, Greedy, Heap (Priority Queue), Sorting  

---

## Problem Statement

There are `n` different online courses numbered from `1` to `n`. You are given an array `courses` where `courses[i] = [durationi, lastDayi]` indicates that the $i^{\text{th}}$ course should be taken continuously for `durationi` days and must be finished before or on `lastDayi`.

You will start on the $1^{\text{st}}$ day and you cannot take two or more courses simultaneously.

Return the **maximum number of courses** that you can take.

---

## Examples

### Example 1

**Input:**
```text
courses = [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
```

**Output:**
```text
3
```

**Explanation:**  
There are totally 4 courses, but you can take 3 courses at most:
1. First, take the $1^{\text{st}}$ course: it costs 100 days so you will finish it on the $100^{\text{th}}$ day, and be ready to take the next course on the $101^{\text{st}}$ day.
2. Second, take the $3^{\text{rd}}$ course: it costs 1000 days so you will finish it on the $1100^{\text{th}}$ day, and be ready to take the next course on the $1101^{\text{st}}$ day.
3. Third, take the $2^{\text{nd}}$ course: it costs 200 days so you will finish it on the $1300^{\text{th}}$ day.
4. The $4^{\text{th}}$ course cannot be taken now, since you would finish it on the $3300^{\text{th}}$ day, which exceeds its deadline of 3200.

### Example 2

**Input:**
```text
courses = [[1, 2]]
```

**Output:**
```text
1
```

### Example 3

**Input:**
```text
courses = [[3, 2], [4, 3]]
```

**Output:**
```text
0
```

---

## Constraints

- `1 <= courses.length <= 10^4`
- `courses[i].length == 2`
- `1 <= durationi, lastDayi <= 10^4`
