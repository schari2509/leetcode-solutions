from collections import deque


class Solution:

    # Time Complexity: O(n) where n = len(nums); each index is pushed to and popped from monoDeque at most once.
    # Space Complexity: O(k) auxiliary space for monoDeque holding at most k indices (excluding output array).
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        monoDeque: deque[int] = deque()
        ans: list[int] = []

        for currIndex, currNum in enumerate(nums):
            # 1. Pop indices that have slid out of the active window [currIndex - k + 1, currIndex]
            while monoDeque and monoDeque[0] < currIndex - k + 1:
                monoDeque.popleft()

            # 2. Maintain monotonic decreasing order by popping smaller elements from the rear
            while monoDeque and currNum > nums[monoDeque[-1]]:
                monoDeque.pop()

            monoDeque.append(currIndex)

            # 3. Once the first window of size k is formed, record the maximum at the front of the deque
            if currIndex >= k - 1:
                ans.append(nums[monoDeque[0]])

        return ans
