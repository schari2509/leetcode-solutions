# Time Complexity: O(1) for all operations (push, pop, top, getMin).
# Space Complexity: O(n) where n is the total number of elements currently stored across the stacks.
class MinStack:

    def __init__(self):
        self.stack: list[int] = []
        self.minStack: list[int] = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)

    def pop(self) -> None:
        if self.stack.pop() == self.minStack[-1]:
            self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
