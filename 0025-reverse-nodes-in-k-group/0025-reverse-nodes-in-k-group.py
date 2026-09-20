# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:

        new = ListNode(0)
        new.next = head

        group_prev = new

        while True:
            kth = group_prev

            for i in range(k):
                kth = kth.next

                if kth is None:
                    return new.next

            group_next = kth.next

            prev = group_next
            curr = group_prev.next

            while curr != group_next:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node

            old_group_start = group_prev.next
            group_prev.next = kth

            group_prev = old_group_start