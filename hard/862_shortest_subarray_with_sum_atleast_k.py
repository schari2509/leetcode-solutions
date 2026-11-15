from collections import deque


class Solution:

    # Time Complexity: O(n) where n = len(nums); each prefix index is added and popped at most once.
    # Space Complexity: O(n) for the prefix sum array and monotonic deque.
    def shortestSubarray(self, nums: list[int], k: int) -> int:
        n = len(nums)
        # prefixSums[i] stores the sum of nums[:i]
        prefixSums = [0] * (n + 1)
        for i in range(n):
            prefixSums[i + 1] = prefixSums[i] + nums[i]

        minLen = float('inf')
        monoDeque: deque[int] = deque()  # Stores indices with strictly increasing prefixSums

        for j in range(n + 1):
            # 1. Pop from front: valid window found where prefixSums[j] - prefixSums[monoDeque[0]] >= k.
            # monoDeque[0] can never yield a shorter subarray for any subsequent index > j.
            while monoDeque and prefixSums[j] - prefixSums[monoDeque[0]] >= k:
                minLen = min(minLen, j - monoDeque.popleft())

            # 2. Pop from rear: if prefixSums[j] <= prefixSums[monoDeque[-1]],
            # index j dominates monoDeque[-1] because it is closer to future indices and has a smaller prefix sum.
            while monoDeque and prefixSums[j] <= prefixSums[monoDeque[-1]]:
                monoDeque.pop()

            monoDeque.append(j)

        return int(minLen) if minLen != float('inf') else -1
