from __future__ import annotations


class ListNode:
    def __init__(self, x: int):
        self.val = x
        self.next: ListNode | None = None


class Solution:

    # Time Complexity: O(n) where n is the number of nodes in the linked list (Floyd's cycle-finding algorithm).
    # Space Complexity: O(1) auxiliary space using pointers slow, fast, and entry.
    def detectCycle(self, head: ListNode | None) -> ListNode | None:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                # Cycle detected; find the cycle entrance
                break
        else:
            return None

        entry = head
        while entry != slow:
            entry = entry.next
            slow = slow.next

        return entry
