from collections import defaultdict


# Time Complexity:
#   - push: O(1) to update frequency map, group map, and maxFreq.
#   - pop: O(1) to pop from group map list and decrement frequency.
# Space Complexity: O(n) where n is the total number of elements currently stored in FreqStack.
class FreqStack:

    def __init__(self):
        self.freq: dict[int, int] = defaultdict(int)
        self.group: dict[int, list[int]] = defaultdict(list)
        self.maxFreq: int = 0

    def push(self, val: int) -> None:
        f = self.freq[val] + 1
        self.freq[val] = f
        if f > self.maxFreq:
            self.maxFreq = f
        self.group[f].append(val)

    def pop(self) -> int:
        val = self.group[self.maxFreq].pop()
        self.freq[val] -= 1
        if not self.group[self.maxFreq]:
            self.maxFreq -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
