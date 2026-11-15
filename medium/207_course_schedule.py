from collections import defaultdict, deque


class Solution:

    # Time Complexity: O(V + E) where V = numCourses and E = len(prerequisites) (Kahn's algorithm).
    # Space Complexity: O(V + E) to store the adjacency list graph, in-degree array, and BFS queue.
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = defaultdict(list)
        inDegree = [0] * numCourses

        # Build the graph adjacency list & compute in-degree
        for u, v in prerequisites:
            graph[v].append(u)
            inDegree[u] += 1

        visited = 0
        queue = deque([u for u in range(numCourses) if inDegree[u] == 0])

        while queue:
            course = queue.popleft()
            visited += 1

            for v in graph[course]:
                inDegree[v] -= 1
                if inDegree[v] == 0:
                    queue.append(v)

        return visited == numCourses
