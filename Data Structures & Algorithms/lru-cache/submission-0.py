class Node:

    def __init__(self, key:int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None




class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.left = Node(0,0) #LRU
        self.right = Node(0,0) #MRU
        self.cache = {}
        self.left.next = self.right #initially there are no elems
        self.right.prev = self.left # only two nodes left and right


    def remove(self, node: Node) :
        prev , nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
    
    def insert(self, node: Node):
        prev, nxt = self.right.prev, self.right
        node.prev = prev
        node.next = nxt
        prev.next = node
        nxt.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        node = Node(key,value)
        self.insert(node)
        self.cache[key] = node

        if len(self.cache) > self.capacity:
            lru = self.cache[self.left.next.key]
            self.remove(lru)
            del self.cache[lru.key]






        
