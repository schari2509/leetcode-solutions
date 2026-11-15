class Solution:

    # Time Complexity: O(m + n) where m = len(nums1) and n = len(nums2).
    # Space Complexity: O(n) to store the monotonic stack and nextGreaterMap.
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nextGreaterMap: dict[int, int] = {}
        monoStack: list[int] = []

        # Traverse nums2 once to precompute the next greater element for each number
        for num in nums2:
            while monoStack and num > monoStack[-1]:
                prevNum = monoStack.pop()
                nextGreaterMap[prevNum] = num
            monoStack.append(num)

        # Look up precomputed next greater values for elements of nums1
        return [nextGreaterMap.get(x, -1) for x in nums1]
