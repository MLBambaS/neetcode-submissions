# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next:
            return
    
        # 1. Trouver le milieu de la liste
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
    
        # 2. Inverser la seconde moitié
        second = slow.next
        slow.next = None  # Couper la liste en deux
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        second = prev  # Nouvelle tête de la seconde moitié inversée
    
        # 3. Fusionner les deux moitiés de manière alternée
        first = head
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
