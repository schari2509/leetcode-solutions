class Solution:

    # Time Complexity: O(n) where n = len(nums); single linear pass updating prefixes and suffixes.
    # Space Complexity: O(1) auxiliary space (excluding the output array ans of size n).
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [1] * n
        prefix, suffix = 1, 1

        for i in range(n):
            ans[i] *= prefix
            prefix *= nums[i]

            suffixIdx = n - 1 - i
            ans[suffixIdx] *= suffix
            suffix *= nums[suffixIdx]

        return ans
