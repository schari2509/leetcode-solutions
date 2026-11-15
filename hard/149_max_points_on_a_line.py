from collections import defaultdict


class Solution:

    def calculateSlope(self, a, b) -> float:
        delY = b[1] - a[1]
        delX = b[0] - a[0]

        if delX == 0:
            return float('inf')

        return delY / delX

    # Time Complexity: O(n^2) where n = len(points); nested loops evaluate slopes between all point pairs.
    # Space Complexity: O(n) to store slopes relative to each anchor point in slopeCounts.
    def maxPoints(self, points: list[list[int]]) -> int:
        globalSlopeCount = 0
        if len(points) == 1:
            return 1

        for i in range(len(points) - 1):
            anchor = points[i]
            slopeCounts = defaultdict(float)

            for j in range(i + 1, len(points)):
                slope = self.calculateSlope(anchor, points[j])
                slopeCounts[slope] += 1

            maxSlope = max(slopeCounts.values()) + 1
            if maxSlope > globalSlopeCount:
                globalSlopeCount = maxSlope

        return int(globalSlopeCount)
