# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        beg = head
        tail = prev
        while tail:
            for i in range (k):
                tail = tail.next
                if not tail : return dummy.next
            self.reverse(beg, tail)
            prev.next = tail
            prev = beg
            beg = beg.next
            tail = prev
        return dummy.next
        
        
    def reverse(self, beg: ListNode, end: ListNode):
        cur = beg
        prev = end.next
        stop = end.next
        while cur!=stop:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp        
            

        