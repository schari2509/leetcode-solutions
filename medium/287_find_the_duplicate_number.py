class Solution:

    # Time Complexity: O(n) where n = len(nums) using Floyd's Tortoise and Hare algorithm.
    # Space Complexity: O(1) auxiliary space modifying no inputs.
    def findDuplicate(self, nums: list[int]) -> int:
        slow = nums[0]
        fast = nums[nums[0]]

        # Phase 1: Detect intersection point inside the cycle
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        # Phase 2: Locate the entrance to the cycle (the duplicate number)
        entry = 0
        while entry != slow:
            entry = nums[entry]
            slow = nums[slow]

        return entry
