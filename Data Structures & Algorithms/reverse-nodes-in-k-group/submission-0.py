# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return None
        prev, next = None, None
        resHead = None
        curHead = head
        curTail = None
        while curHead:
            curTail = curHead
            for i in range(1, k):
                curTail = curTail.next
                if not curTail: break
            if not curTail:
                if prev: prev.next = curHead
                return resHead if resHead else head
            else:
                next = curTail.next
                curTail.next = None
                rev = self.reverseList(curHead)
                if not resHead: resHead = rev
                if prev: prev.next = rev
                prev = curHead
                curHead = next
        return resHead

    def reverseList(self, head: ListNode) -> ListNode:
        cur = head
        prev = None
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev

        