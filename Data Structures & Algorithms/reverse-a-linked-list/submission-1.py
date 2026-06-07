# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == []: return []
        cur = head
        prevNode = None
        node = head
        while node:
            n = node.next
            node.next = prevNode
            prevNode = node
            node = n
        return prevNode




        
        