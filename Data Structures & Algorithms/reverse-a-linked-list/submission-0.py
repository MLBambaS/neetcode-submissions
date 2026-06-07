# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == []: return []
        node = head
        nextNode = None
        while node:
            n = ListNode(node.val, nextNode)
            node = node.next
            nextNode = n
        return nextNode




        
        