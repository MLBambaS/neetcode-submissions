# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow
        second = mid.next
        mid.next = None
        # reverse second part
        prev = None
        cur = second
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        first, second = head, prev
        while second:
            tmp = first.next
            first.next = second
            tmp2 = second.next
            second.next = tmp
            first = tmp
            second = tmp2
        
