import unittest
class Node:
    def __init__(self, key, value):
        self.prev = None
        self.next = None
        self.value = value
        self.key = key
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {} # will be a map of hashedkeys
        
        # Init left, right nodes; where left is the most recently used ref and right is the least recently used ref
        self.left = Node(-1, 0)
        self.right = Node(-2, 0)
        self.left.next = self.right
        self.right.prev = self.left
        
        
    def add(self, node):
        prev,  next = self.left, self.left.next
        
        node.prev, node.next = prev, next
        next.prev, prev.next = node, node
        
    def remove(self, node):
        prev = node.prev
        next = node.next
        
        prev.next = next
        next.prev = prev
        

    def get(self, key: int) -> int:
        if key in self.map:
            self.remove(self.map[key])
            self.add(self.map[key])
            return self.map[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        
        # update record if key already exists, add the node to MRU
        if key in self.map:
            self.map[key].value = value
            self.remove(self.map[key])
            self.add(self.map[key])
            return
        
        newNode = Node(key, value)

        
        # If hash table not at capacity, and add the newNode to MRU ref
        if len(self.map) < self.capacity:
            self.map[key] = newNode
            self.add(newNode)
            return         
                    
        # if hash table is at capacity
        del self.map[self.right.prev.key]
        self.remove(self.right.prev)
        
        self.add(newNode)
        self.map[key] = newNode


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


class TestLRUCache(unittest.TestCase):

    def test_initialization(self):
        cache = LRUCache(2)
        self.assertEqual(cache.capacity, 2)

    def test_put_operation(self):
        cache = LRUCache(2)
        cache.put(1, 1)
        self.assertEqual(cache.get(1), 1)

    def test_get_operation(self):
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        self.assertEqual(cache.get(1), 1)
        self.assertEqual(cache.get(2), 2)
        self.assertEqual(cache.get(3), -1)

    def test_capacity_limit(self):
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        cache.put(3, 3)
        self.assertEqual(cache.get(1), -1)
        self.assertEqual(cache.get(2), 2)
        self.assertEqual(cache.get(3), 3)

    def test_update_value(self):
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        cache.put(1, 10)
        self.assertEqual(cache.get(1), 10)
        cache.put(3, 3)
        self.assertEqual(cache.get(2), -1)

    def test_recently_used_order(self):
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        cache.get(1)
        cache.put(3, 3)
        self.assertEqual(cache.get(1), 1)
        self.assertEqual(cache.get(2), -1)
        self.assertEqual(cache.get(3), 3)

if __name__ == '__main__':
    unittest.main()