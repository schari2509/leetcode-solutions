class Solution:

    # Time Complexity: O(n) where n is the length of height; two-pointer traversal visits each element at most once.
    # Space Complexity: O(1) auxiliary space using constant extra variables.
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        maxWaterArea = 0

        while left < right:
            hLeft, hRight = height[left], height[right]
            width = right - left

            if hLeft <= hRight:
                area = width * hLeft
                while left < right and height[left] <= hLeft:
                    left += 1
            else:
                area = width * hRight
                while left < right and height[right] <= hRight:
                    right -= 1

            if area > maxWaterArea:
                maxWaterArea = area

        return maxWaterArea
