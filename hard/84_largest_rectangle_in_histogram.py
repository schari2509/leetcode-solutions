class Solution:

    # Time Complexity: O(n) where n = len(heights); each index is pushed and popped at most once.
    # Space Complexity: O(n) for the monotonic stack storing indices.
    def largestRectangleArea(self, heights: list[int]) -> int:
        monoStack: list[int] = []  # Monotonic increasing stack storing indices
        maxArea = 0
        n = len(heights)

        # Iterate up to n + 1 using a sentinel height of 0 at index n
        for currIndex in range(n + 1):
            currHeight = heights[currIndex] if currIndex < n else 0

            # When the current bar is shorter than the bar on top of the stack,
            # the bar at the top of the stack cannot extend further right.
            while monoStack and currHeight < heights[monoStack[-1]]:
                barIndex = monoStack.pop()
                barHeight = heights[barIndex]

                # Width is bounded by currIndex on the right and monoStack[-1] on the left
                width = currIndex if not monoStack else currIndex - monoStack[-1] - 1
                maxArea = max(maxArea, barHeight * width)

            monoStack.append(currIndex)

        return maxArea
