class LinkNode:
    def __init__(self, key, val, prev, next):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.currentCapacity = 0
        self.leftDummy = LinkNode(0,0,None,None)
        self.rightDummy = LinkNode(0,0,self.leftDummy,None)
        self.leftDummy.right = self.rightDummy

    def add(self, node: LinkNode):
        prev = self.rightDummy.prev
        node.next = self.rightDummy
        node.prev = prev
        prev.next = node
        self.rightDummy.prev = node
        self.cache[node.key] = node
    
    def remove(self, node: LinkNode):
        self.cache.pop(node.key)
        self.leftDummy.next = node.next
        node.next.prev = self.leftDummy

    def moveToLast(self, node: LinkNode):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.rightDummy.prev.next = node
        node.prev = self.rightDummy.prev
        node.next = self.rightDummy
        self.rightDummy.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.moveToLast(self.cache[key])
        return self.cache[key].val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self.moveToLast(self.cache[key])
        else:
            if self.currentCapacity == self.capacity:
                self.remove(self.leftDummy.next)
            else: 
                self.currentCapacity += 1
            self.add(LinkNode(key, value, None, None))
        
