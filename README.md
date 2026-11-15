# LeetCode Solutions

A structured repository of solutions and notes for LeetCode algorithmic problems.

---

## Repository Structure

Problems are categorized by their LeetCode difficulty level:

```text
LeetCode/
├── easy/
│   ├── 496_next_greater_element_1.md
│   ├── 496_next_greater_element_1.py
│   ├── 706_design_hashmap.md
│   └── 706_design_hashmap.py
├── medium/
│   ├── 11_container_with_most_water.md
│   ├── 11_container_with_most_water.py
│   ├── 128_longest_consecutive_sequence.md
│   ├── 128_longest_consecutive_sequence.py
│   ├── 142_linked_list_cycle_2.md
│   ├── 142_linked_list_cycle_2.py
│   ├── 143_reorder_list.md
│   ├── 143_reorder_list.py
│   ├── 146_lru_cache.md
│   ├── 146_lru_cache.py
│   ├── 155_min_stack.md
│   ├── 155_min_stack.py
│   ├── 207_course_schedule.md
│   ├── 207_course_schedule.py
│   ├── 238_product_of_array_except_self.md
│   ├── 238_product_of_array_except_self.py
│   ├── 287_find_the_duplicate_number.md
│   ├── 287_find_the_duplicate_number.py
│   ├── 503_next_greater_element_2.md
│   ├── 503_next_greater_element_2.py
│   ├── 525_contiguous_array.md
│   ├── 525_contiguous_array.py
│   ├── 542_01_matrix.md
│   ├── 542_01_matrix.py
│   ├── 560_subarray_sum_equals_k.md
│   ├── 560_subarray_sum_equals_k.py
│   ├── 739_daily_temperatures.md
│   ├── 739_daily_temperatures.py
│   ├── 994_rotting_oranges.md
│   └── 994_rotting_oranges.py
├── hard/
│   ├── 25_reverse_nodes_in_k_group.md
│   ├── 25_reverse_nodes_in_k_group.py
│   ├── 30_substring_with_concatenation_of_all_words.md
│   ├── 30_substring_with_concatenation_of_all_words.py
│   ├── 42_trapping_rain_water.md
│   ├── 42_trapping_rain_water.py
│   ├── 76_minimum_window_substring.md
│   ├── 76_minimum_window_substring.py
│   ├── 84_largest_rectangle_in_histogram.md
│   ├── 84_largest_rectangle_in_histogram.py
│   ├── 149_max_points_on_a_line.md
│   ├── 149_max_points_on_a_line.py
│   ├── 224_basic_calculator.md
│   ├── 224_basic_calculator.py
│   ├── 239_sliding_window_maximum.md
│   ├── 239_sliding_window_maximum.py
│   ├── 381_insert_delete_getrandom_o1.md
│   ├── 381_insert_delete_getrandom_o1.py
│   ├── 630_course_schedule_3.md
│   ├── 862_shortest_subarray_with_sum_atleast_k.md
│   ├── 862_shortest_subarray_with_sum_atleast_k.py
│   ├── 895_maximum_frequency_stack.md
│   └── 895_maximum_frequency_stack.py
└── README.md
```

- **Markdown files (`<id>_<title>.md`)**: Problem statement, difficulty, topic tags, formatted examples, and constraints.
- **Python files (`<id>_<title>.py`)**: Clean, optimal solutions.

---

## Guidelines & Coding Standards

1. **Casing Convention:**
   - Always follow **`camelCase`** for variable, helper function, and method names throughout the codebase, even in Python and regardless of linter/PEP 8 warnings.
2. **Indentation & Formatting:**
   - Use **4 spaces** for indentation. Avoid mixing tabs and spaces to prevent Python `TabError` exceptions.
   - Maintain clean type hints (`list[int]`, `bool`, etc.) on solution methods.
3. **File Naming:**
   - Format: `<problem_number>_<snake_case_title>.py` and `<problem_number>_<snake_case_title>.md`
   - Example: `11_container_with_most_water.py`, `238_product_of_array_except_self.md`
4. **Markdown Documentation:**
   - Maintain the standard section headers: `# <Number>. <Title>`, `**Difficulty:**`, `**Topics:**`, `## Problem Statement`, `## Examples`, and `## Constraints`.
5. **Complexity Analysis Comments:**
   - All Python solutions should have time and space complexity mentioned for the solution code as comments.

---

## Problem Index

| # | Title | Difficulty | Topics | Solution | Notes |
|---|---|---|---|---|---|
| 11 | Container With Most Water | Medium | Array, Two Pointers, Greedy | [Python](medium/11_container_with_most_water.py) | [Notes](medium/11_container_with_most_water.md) |
| 25 | Reverse Nodes in k-Group | Hard | Linked List, Recursion | [Python](hard/25_reverse_nodes_in_k_group.py) | [Notes](hard/25_reverse_nodes_in_k_group.md) |
| 30 | Substring with Concatenation of All Words | Hard | Hash Table, String, Sliding Window | [Python](hard/30_substring_with_concatenation_of_all_words.py) | [Notes](hard/30_substring_with_concatenation_of_all_words.md) |
| 42 | Trapping Rain Water | Hard | Array, Two Pointers, Dynamic Programming, Stack, Monotonic Stack | [Python](hard/42_trapping_rain_water.py) | [Notes](hard/42_trapping_rain_water.md) |
| 76 | Minimum Window Substring | Hard | Hash Table, String, Sliding Window | [Python](hard/76_minimum_window_substring.py) | [Notes](hard/76_minimum_window_substring.md) |
| 84 | Largest Rectangle in Histogram | Hard | Array, Stack, Monotonic Stack | [Python](hard/84_largest_rectangle_in_histogram.py) | [Notes](hard/84_largest_rectangle_in_histogram.md) |
| 128 | Longest Consecutive Sequence | Medium | Array, Hash Table, Union Find | [Python](medium/128_longest_consecutive_sequence.py) | [Notes](medium/128_longest_consecutive_sequence.md) |
| 142 | Linked List Cycle II | Medium | Hash Table, Linked List, Two Pointers | [Python](medium/142_linked_list_cycle_2.py) | [Notes](medium/142_linked_list_cycle_2.md) |
| 143 | Reorder List | Medium | Linked List, Two Pointers, Stack, Recursion | [Python](medium/143_reorder_list.py) | [Notes](medium/143_reorder_list.md) |
| 146 | LRU Cache | Medium | Hash Table, Linked List, Design, Doubly-Linked List | [Python](medium/146_lru_cache.py) | [Notes](medium/146_lru_cache.md) |
| 149 | Max Points on a Line | Hard | Array, Hash Table, Math, Geometry | [Python](hard/149_max_points_on_a_line.py) | [Notes](hard/149_max_points_on_a_line.md) |
| 155 | Min Stack | Medium | Stack, Design | [Python](medium/155_min_stack.py) | [Notes](medium/155_min_stack.md) |
| 207 | Course Schedule | Medium | DFS, BFS, Graph, Topological Sort | [Python](medium/207_course_schedule.py) | [Notes](medium/207_course_schedule.md) |
| 224 | Basic Calculator | Hard | Math, String, Stack, Recursion | [Python](hard/224_basic_calculator.py) | [Notes](hard/224_basic_calculator.md) |
| 238 | Product of Array Except Self | Medium | Array, Prefix Sum | [Python](medium/238_product_of_array_except_self.py) | [Notes](medium/238_product_of_array_except_self.md) |
| 239 | Sliding Window Maximum | Hard | Array, Queue, Sliding Window, Heap (Priority Queue), Monotonic Queue | [Python](hard/239_sliding_window_maximum.py) | [Notes](hard/239_sliding_window_maximum.md) |
| 287 | Find the Duplicate Number | Medium | Array, Two Pointers, Binary Search, Bit Manipulation | [Python](medium/287_find_the_duplicate_number.py) | [Notes](medium/287_find_the_duplicate_number.md) |
| 381 | Insert Delete GetRandom O(1) - Duplicates allowed | Hard | Array, Hash Table, Math, Design, Randomized | [Python](hard/381_insert_delete_getrandom_o1.py) | [Notes](hard/381_insert_delete_getrandom_o1.md) |
| 496 | Next Greater Element I | Easy | Array, Hash Table, Stack, Monotonic Stack | [Python](easy/496_next_greater_element_1.py) | [Notes](easy/496_next_greater_element_1.md) |
| 503 | Next Greater Element II | Medium | Array, Stack, Monotonic Stack | [Python](medium/503_next_greater_element_2.py) | [Notes](medium/503_next_greater_element_2.md) |
| 525 | Contiguous Array | Medium | Array, Hash Table, Prefix Sum | [Python](medium/525_contiguous_array.py) | [Notes](medium/525_contiguous_array.md) |
| 542 | 01 Matrix | Medium | Array, Dynamic Programming, Breadth-First Search, Matrix | [Python](medium/542_01_matrix.py) | [Notes](medium/542_01_matrix.md) |
| 560 | Subarray Sum Equals K | Medium | Array, Hash Table, Prefix Sum | [Python](medium/560_subarray_sum_equals_k.py) | [Notes](medium/560_subarray_sum_equals_k.md) |
| 630 | Course Schedule III | Hard | Array, Greedy, Heap (Priority Queue), Sorting | — | [Notes](hard/630_course_schedule_3.md) |
| 706 | Design HashMap | Easy | Array, Hash Table, Linked List, Design, Hash Function | [Python](easy/706_design_hashmap.py) | [Notes](easy/706_design_hashmap.md) |
| 739 | Daily Temperatures | Medium | Array, Stack, Monotonic Stack | [Python](medium/739_daily_temperatures.py) | [Notes](medium/739_daily_temperatures.md) |
| 862 | Shortest Subarray with Sum at Least K | Hard | Array, Binary Search, Queue, Sliding Window, Heap (Priority Queue), Prefix Sum, Monotonic Queue | [Python](hard/862_shortest_subarray_with_sum_atleast_k.py) | [Notes](hard/862_shortest_subarray_with_sum_atleast_k.md) |
| 895 | Maximum Frequency Stack | Hard | Hash Table, Stack, Design, Ordered Set | [Python](hard/895_maximum_frequency_stack.py) | [Notes](hard/895_maximum_frequency_stack.md) |
| 994 | Rotting Oranges | Medium | Array, Breadth-First Search, Matrix | [Python](medium/994_rotting_oranges.py) | [Notes](medium/994_rotting_oranges.md) |
