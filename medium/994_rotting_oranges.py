from collections import deque


class Solution:

    # Time Complexity: O(m * n) where m = len(grid) and n = len(grid[0]); every cell is processed at most once.
    # Space Complexity: O(m * n) in the worst case for the BFS queue.
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        queue: deque[tuple[int, int]] = deque()
        freshOranges = 0

        # Step 1: Enqueue all initially rotten oranges and count fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    freshOranges += 1

        # Edge case: No fresh oranges initially
        if freshOranges == 0:
            return 0

        minutes = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Step 2: Multi-source BFS (level by level, where 1 level = 1 minute)
        while queue and freshOranges > 0:
            minutes += 1
            for _ in range(len(queue)):
                currR, currC = queue.popleft()
                for dr, dc in directions:
                    newR = currR + dr
                    newC = currC + dc
                    if 0 <= newR < rows and 0 <= newC < cols and grid[newR][newC] == 1:
                        grid[newR][newC] = 2
                        freshOranges -= 1
                        queue.append((newR, newC))

        return minutes if freshOranges == 0 else -1
