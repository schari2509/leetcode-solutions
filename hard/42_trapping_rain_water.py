class Solution:

    # Time Complexity: O(n) where n = len(height); each index is pushed and popped at most once.
    # Space Complexity: O(n) for the monotonic stack storing indices.
    def trap(self, height: list[int]) -> int:
        totalWater = 0
        monoStack: list[int] = []  # Monotonic decreasing stack storing indices

        for currIndex, currHeight in enumerate(height):
            # A taller bar acts as a right wall bounding a basin
            while monoStack and currHeight > height[monoStack[-1]]:
                bottomIndex = monoStack.pop()

                # If there is no left wall, water spills to the left
                if not monoStack:
                    break

                leftIndex = monoStack[-1]
                boundedHeight = min(height[leftIndex], currHeight) - height[bottomIndex]
                distance = currIndex - leftIndex - 1
                totalWater += boundedHeight * distance

            monoStack.append(currIndex)

        return totalWater
