class DoubleLinkedNode:
    def __init__(self, key, val=0, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cur=0
        self.dico = {}
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        if key not in self.dico : return -1
        node = self.dico[key]
        self.moveToTail(node)
        return node.val
        


    def put(self, key: int, value: int) -> None:
        if key in self.dico:
            node = self.dico[key]
            node.val = value
            self.moveToTail(node)
        else:
            node = DoubleLinkedNode(key, value, self.tail, None)
            if self.tail: self.tail.next = node
            self.tail = node
            self.dico[key] = node
            if not self.head:
                self.head = node
            self.cur+=1
            if self.cur > self.capacity:
                self.head.next.prev = None
                del self.dico[self.head.key]
                self.head = self.head.next
                self.cur-=1

    def moveToTail(self, node:DoubleLinkedNode) -> None:
        if self.tail == node: return
        prev = node.prev
        next = node.next
        if prev: prev.next = next
        else:
            self.head = next
        if next: next.prev = prev
        node.prev = self.tail
        self.tail.next = node
        self.tail = node

        
