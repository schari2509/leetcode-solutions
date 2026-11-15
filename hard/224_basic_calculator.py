class Solution:

    # Time Complexity: O(n) where n = len(s); single pass character-by-character scan.
    # Space Complexity: O(n) for the stack storing intermediate sums and signs across parentheses levels.
    def calculate(self, s: str) -> int:
        runningSum = 0
        currNum = 0
        currSign = 1
        stack = []

        for ch in s:
            if ch.isdigit():
                currNum = currNum * 10 + int(ch)
            elif ch == '+':
                runningSum += currSign * currNum
                currNum = 0
                currSign = 1
            elif ch == '-':
                runningSum += currSign * currNum
                currNum = 0
                currSign = -1
            elif ch == '(':
                # Push the running sum and current sign before '(' onto the stack
                stack.append(runningSum)
                stack.append(currSign)
                # Reset for the new expression inside parentheses
                runningSum = 0
                currSign = 1
            elif ch == ')':
                # Add the last number within the parentheses
                runningSum += currSign * currNum
                currNum = 0
                # Combine with sign and sum before '('
                prevSign = stack.pop()
                prevSum = stack.pop()
                runningSum = prevSum + prevSign * runningSum

        runningSum += currSign * currNum
        return runningSum
