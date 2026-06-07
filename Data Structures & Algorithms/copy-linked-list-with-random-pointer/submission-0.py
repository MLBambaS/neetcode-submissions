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
        hashMap = dict()
        node = head
        pos = 0
        while node:
            newNode = Node(node.val)
            hashMap[node] = newNode
            node = node.next
        node = head
        while node:
            hashMap[node].next = hashMap.get(node.next, None)
            hashMap[node].random = hashMap.get(node.random, None)
            node = node.next
        return hashMap[head]


        