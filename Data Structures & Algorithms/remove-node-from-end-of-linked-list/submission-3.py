# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        first, second = dummy, dummy
        for i in range(n+1):
            second = second.next
        while second:
            second = second.next
            first = first.next
        tmp = first.next.next
        first.next = tmp
        return dummy.next

        