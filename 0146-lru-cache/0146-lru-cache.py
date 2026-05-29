#LRU Cache is a Doubly Linked List of Cache Entries

class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node): #helper to remove any node from Doubly Linked List
        prev , nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right #Insert MRU on right node
        prev.next = node
        node.prev = prev 

        node.next = nxt
        nxt.prev = node

        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1 

        node = self.cache[key]
        self.remove(node)
        self.insert(node)

        return node.val
        

    def put(self, key: int, value: int) -> None:
        
        if key in self.cache: #if key exists
            self.remove(self.cache[key])
        
        new_node = Node(key,value)

        self.cache[key] = new_node
        self.insert(new_node)

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)