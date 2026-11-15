class Solution:

    # Time Complexity: O(n) where n = len(nums); single pass with O(1) hash map operations.
    # Space Complexity: O(n) in the worst case to store prefix sums in prefixCounts.
    def subarraySum(self, nums: list[int], k: int) -> int:
        prefixCounts = {0: 1}
        currentSum = 0
        total = 0

        for num in nums:
            currentSum += num
            if prefixCounts.get(currentSum - k) is not None:
                total += prefixCounts.get(currentSum - k)
            prefixCounts[currentSum] = prefixCounts.get(currentSum, 0) + 1

        return total
