class ListNode:
    def __init__(self, key: int = 0, val: int = 0):
        self.key = key
        self.val = val
        self.prev: ListNode | None = None
        self.next: ListNode | None = None


# Time Complexity:
#   - get: O(1) hash map lookup and doubly-linked list node repositioning.
#   - put: O(1) hash map update/insertion and doubly-linked list node insertion/eviction.
# Space Complexity: O(C) where C is the capacity of the LRU cache (hash map and node instances).
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache: dict[int, ListNode] = {}
        # Sentinel dummy nodes to eliminate edge-case boundary checks
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def removeNode(self, node: ListNode) -> None:
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode

    def addToHead(self, node: ListNode) -> None:
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def moveToHead(self, node: ListNode) -> None:
        self.removeNode(node)
        self.addToHead(node)

    def popTail(self) -> ListNode:
        res = self.tail.prev
        self.removeNode(res)
        return res

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.moveToHead(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.moveToHead(node)
        else:
            newNode = ListNode(key, value)
            self.cache[key] = newNode
            self.addToHead(newNode)
            if len(self.cache) > self.capacity:
                tailNode = self.popTail()
                del self.cache[tailNode.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
