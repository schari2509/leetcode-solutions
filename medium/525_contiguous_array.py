class Solution:

    # Time Complexity: O(n) where n = len(nums); single pass with O(1) hash map operations.
    # Space Complexity: O(n) to store prefix sums in prefixIndices hash map in the worst case.
    def findMaxLength(self, nums: list[int]) -> int:
        prefixIndices = {0: -1}
        currentSum = 0
        maxLength = 0

        for i, num in enumerate(nums):
            currentSum += 1 if num == 1 else -1

            if currentSum in prefixIndices:
                maxLength = max(maxLength, i - prefixIndices[currentSum])
            else:
                prefixIndices[currentSum] = i

        return maxLength
