# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1: return l2
        if not l2: return l1
        carry = False
        tmp = l1.val+l2.val
        if tmp>=10:
            carry = True
            tmp %= 10
        res = ListNode(tmp)
        A, B = l1.next, l2.next
        prev = res 
        while A and B:
            tmp = A.val + B.val
            if carry: tmp+=1
            if tmp >= 10: 
                carry = True
                tmp = tmp%10
            else: carry = False
            current = ListNode(tmp)
            prev.next = current
            prev = current
            A = A.next
            B = B.next
        while A:
            tmp = A.val
            if carry: tmp+=1
            if tmp == 10: 
                carry = True
                tmp = 0
            else: carry = False
            current = ListNode(tmp)
            prev.next = current
            prev = current
            A = A.next
        while B:
            tmp = B.val
            if carry: tmp+=1
            if tmp == 10: 
                carry = True
                tmp = 0
            else: carry = False
            current = ListNode(tmp)
            prev.next = current
            prev = current
            B = B.next
        if carry:
            current = ListNode(1)
            prev.next = current
            prev = current
        return res

            

        