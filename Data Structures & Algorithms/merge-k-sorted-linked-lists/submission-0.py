# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return None
        k = len(lists)
        res = lists[0]
        for i in range(1, k):
            arr = lists[i]
            cur = arr
            while cur: 
                next = cur.next
                if not res: res = cur
                else:
                    if cur.val < res.val:
                        cur.next = res
                        res = cur
                    prev = res
                    curRes = res.next 
                    while curRes:
                        if curRes.val < cur.val:
                            prev = curRes
                            curRes = curRes.next
                        else:
                            prev.next = cur
                            cur.next = curRes
                            break
                    if not curRes and prev.next!=cur:
                        prev.next = cur
                        cur.next = None
                cur = next
        return res
