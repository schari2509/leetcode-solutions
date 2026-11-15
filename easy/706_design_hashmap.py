# Time Complexity:
#   - put: O(1) amortized average, O(N) worst case during resize or high collisions.
#   - get: O(1) average, O(N) worst case.
#   - remove: O(1) average, O(N) worst case.
# Space Complexity: O(N + C) where N is the number of active keys and C is the capacity (O(N) overall).
class MyHashMap:
    _EMPTY = object()
    _DELETED = object()

    def __init__(self, capacity: int = 1009):
        self.capacity = capacity
        self.size = 0
        self.occupied = 0  # Tracks both active keys and tombstones
        self.keys = [self._EMPTY] * self.capacity
        self.values = [None] * self.capacity

    def _probe(self, key: int) -> tuple[int, bool]:
        idx = hash(key) % self.capacity
        firstDeleted = None

        while self.keys[idx] is not self._EMPTY:
            if self.keys[idx] is self._DELETED:
                if firstDeleted is None:
                    firstDeleted = idx
            elif self.keys[idx] == key:
                return idx, True
            idx = (idx + 1) % self.capacity

        return (firstDeleted if firstDeleted is not None else idx), False

    def put(self, key: int, value: int) -> None:
        # Resize when occupied slots exceed 66% capacity to prevent clustering and probe loops
        if self.size * 3 >= self.capacity * 2:  # Load factor >= 2/3
            self._resize(self.capacity * 2)

        idx, found = self._probe(key)
        if not found:
            self.size += 1
            if self.keys[idx] is self._EMPTY:
                self.occupied += 1

        self.keys[idx] = key
        self.values[idx] = value

    def get(self, key: int) -> int:
        idx, found = self._probe(key)
        if found:
            return self.values[idx]
        return -1

    def remove(self, key: int) -> None:
        idx, found = self._probe(key)
        if found:
            self.keys[idx] = self._DELETED
            self.values[idx] = None
            self.size -= 1

    def _resize(self, new_capacity: int) -> None:
        old_keys, old_values = self.keys, self.values
        self.capacity = new_capacity
        self.size = 0
        self.occupied = 0
        self.keys = [self._EMPTY] * self.capacity
        self.values = [None] * self.capacity

        # Rehash all active keys; tombstones are cleared
        for k, v in zip(old_keys, old_values):
            if k is not self._EMPTY and k is not self._DELETED:
                self.put(k, v)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
