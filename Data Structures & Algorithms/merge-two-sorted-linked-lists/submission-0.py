# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and list2: return list2
        elif list1 and not list2: return list1
        elif not list1 and not list2: return None
        A_cur, B_cur = list1, list2
        res = None
        if A_cur.val < B_cur.val:
            res = A_cur
            A_cur = A_cur.next
        else : 
            res = B_cur
            B_cur = B_cur.next
        cur = res
        while A_cur and B_cur :
            if A_cur.val <= B_cur.val:
                cur.next = A_cur
                cur = A_cur
                A_cur = A_cur.next
            else:
                cur.next = B_cur
                cur = B_cur
                B_cur = B_cur.next
        if A_cur: cur.next = A_cur
        elif B_cur: cur.next = B_cur
        return res
        