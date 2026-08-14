class node:
    def __init__(self, key, val):
        self.key,self.val = key,val
        self.next = None
        self.prev = None
    
class LRUCache:

    def __init__(self, capacity: int):
        self.m = {}
        self.c = capacity

        self.left = node(0,0)
        self.right = node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        p = node.prev
        n = node.next
        p.next ,n.prev = n,p


    def insert(self, node):
        prev = self.right.prev
        prev.next = node
        self.right.prev = node

        node.next = self.right
        node.prev = prev

    def get(self, key: int) -> int:
        if key in self.m:
            self.remove(self.m[key])
            self.insert(self.m[key])
            return self.m[key].val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:

        if key in self.m:
            self.remove(self.m[key])
        self.m[key] = node(key,value)
        self.insert(self.m[key])

        if len(self.m)>self.c:
            lru = self.left.next
            del self.m[lru.key]
            self.remove(lru)
        

        
