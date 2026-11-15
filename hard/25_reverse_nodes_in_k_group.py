from __future__ import annotations


class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None = None):
        self.val = val
        self.next = next


class Solution:

    # Time Complexity: O(n) where n is the number of nodes in the linked list; each node is touched at most twice.
    # Space Complexity: O(1) auxiliary space (in-place node pointer updates).
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        dummy = ListNode(0, head)
        groupPrev = dummy

        def getKth(curr: ListNode | None, count: int) -> ListNode | None:
            while curr and count > 0:
                curr = curr.next
                count -= 1
            return curr

        while True:
            kth = getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next

            # Reverse the k nodes between groupPrev and groupNext
            prev = groupNext
            curr = groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            # Connect previous group to reversed group head and advance
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp

        return dummy.next
