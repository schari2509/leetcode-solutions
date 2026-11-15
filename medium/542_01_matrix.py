from collections import deque


class Solution:

    # Time Complexity: O(m * n) where m = len(mat) and n = len(mat[0]); each cell is enqueued and dequeued once.
    # Space Complexity: O(m * n) for the dist matrix and BFS queue.
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        rows = len(mat)
        cols = len(mat[0])
        dist: list[list[int]] = [[-1] * cols for _ in range(rows)]
        queue: deque[tuple[int, int]] = deque()

        # Step 1: Add all 0s to the queue as starting sources with distance 0
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    dist[r][c] = 0
                    queue.append((r, c))

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Step 2: Multi-source BFS outward from all 0s simultaneously
        while queue:
            currR, currC = queue.popleft()
            for dr, dc in directions:
                newR = currR + dr
                newC = currC + dc
                if 0 <= newR < rows and 0 <= newC < cols and dist[newR][newC] == -1:
                    dist[newR][newC] = dist[currR][currC] + 1
                    queue.append((newR, newC))

        return dist
