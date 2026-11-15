class Solution:

    # Time Complexity: O(n) where n is the length of nums; set creation is O(n), and each number is visited at most twice.
    # Space Complexity: O(n) to store numbers in numsSet.
    def longestConsecutive(self, nums: list[int]) -> int:
        numsSet = set(nums)
        longestSeq = 0

        # Important to use the set here instead of the list, otherwise
        # the time complexity will be O(n^2) instead of O(n)
        for num in numsSet:
            if (num - 1) not in numsSet:
                currentSeq = 1
                currentNum = num

                while (currentNum + 1) in numsSet:
                    currentSeq += 1
                    currentNum += 1

                if currentSeq > longestSeq:
                    longestSeq = currentSeq

        return longestSeq
