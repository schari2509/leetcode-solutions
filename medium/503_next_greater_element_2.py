class Solution:

    # Time Complexity: O(n) where n = len(nums); 2n iterations, each index pushed and popped at most once.
    # Space Complexity: O(n) for the output array ans and monotonic stack.
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [-1] * n
        monoStack: list[int] = []  # Monotonic decreasing stack storing indices

        # Traverse twice (2 * n) to simulate circular array traversal using modulo
        for i in range(2 * n):
            currNum = nums[i % n]
            while monoStack and currNum > nums[monoStack[-1]]:
                prevIndex = monoStack.pop()
                ans[prevIndex] = currNum

            # Only push indices during the first pass
            if i < n:
                monoStack.append(i)

        return ans
