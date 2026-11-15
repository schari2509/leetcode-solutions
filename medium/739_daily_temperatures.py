class Solution:

    # Time Complexity: O(n) where n = len(temperatures); each index is pushed and popped at most once.
    # Space Complexity: O(n) for the output array and monotonic stack.
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        answer = [0] * n
        monoStack: list[int] = []  # Monotonic decreasing stack storing indices

        for currIndex in range(n):
            currTemp = temperatures[currIndex]
            while monoStack and currTemp > temperatures[monoStack[-1]]:
                prevIndex = monoStack.pop()
                answer[prevIndex] = currIndex - prevIndex
            monoStack.append(currIndex)

        return answer
