"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None
        current = head
        # insert new nodes inside others
        while current:
            newNode = Node(current.val, current.next)
            current.next = newNode
            current = newNode.next
        # set random for new nodes
        current = head
        currentNew = head.next
        while current:
            if current.random:
                currentNew.random = current.random.next
            current = currentNew.next
            if currentNew.next:
                currentNew = current.next
        # detache
        current = head
        newHead = head.next
        currentNew = newHead
        while current:
            current.next = currentNew.next
            if currentNew.next:
                currentNew.next = currentNew.next.next
            current = current.next
            currentNew = currentNew.next
        return newHead
        