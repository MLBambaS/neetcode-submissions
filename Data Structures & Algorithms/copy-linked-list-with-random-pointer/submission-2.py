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
        map = {}
        cur = head
        if not cur : return None
        while cur:
            new = Node(cur.val)
            map[cur] = new
            cur = cur.next
        cur = head
        while cur:
            if cur.next:
                map[cur].next = map[cur.next]
            if cur.random: 
                map[cur].random = map[cur.random]
            cur = cur.next
        return map[head]

        