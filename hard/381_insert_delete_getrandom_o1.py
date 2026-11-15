from collections import defaultdict
import random


# Time Complexity:
#   - insert: O(1) average time to append to list and add index to set.
#   - remove: O(1) average time using swap-with-last element technique.
#   - getRandom: O(1) time using random.choice on the underlying list pool.
# Space Complexity: O(n) where n is the total number of inserted elements across pool and index sets.
class RandomizedCollection:

    def __init__(self):
        self.indices = defaultdict(set)
        self.pool = []

    def insert(self, val: int) -> bool:
        indicesSet = self.indices[val]
        hasVal = bool(indicesSet)
        indicesSet.add(len(self.pool))
        self.pool.append(val)
        return not hasVal

    def remove(self, val: int) -> bool:
        indicesSet = self.indices.get(val)
        if not indicesSet:
            return False

        removeIdx = indicesSet.pop()
        lastIdx = len(self.pool) - 1

        if removeIdx != lastIdx:
            lastVal = self.pool[-1]
            self.pool[removeIdx] = lastVal
            lastValIndices = self.indices[lastVal]
            lastValIndices.remove(lastIdx)
            lastValIndices.add(removeIdx)

        self.pool.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.pool)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
