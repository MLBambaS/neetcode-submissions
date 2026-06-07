# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        prev = dummy
        while l1 and l2:
            val = l1.val+l2.val+carry
            carry = val//10
            val%=10
            node = ListNode(val, None)
            prev.next = node
            prev = node
            l1=l1.next
            l2=l2.next
        while l1:
            val = l1.val+carry
            carry = val//10
            val%=10
            node = ListNode(val, None)
            prev.next = node
            prev = node
            l1=l1.next
        while l2:
            val = l2.val+carry
            carry = val//10
            val%=10
            node = ListNode(val, None)
            prev.next = node
            prev = node
            l2=l2.next
        if carry == 1:
            node = ListNode(1)
            prev.next = node
        return dummy.next


        