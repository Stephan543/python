import unittest

# Implement a hashmap.

class Node():
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        self.next = None

class MyHashMap():
    def __init__(self) -> None:
        self.size = 10
        self.map = [Node(-1, -1) for i in range(self.size)]
    
    # How to set hash value from key? mod? 
    def _hash_(self, key) -> int:
        return key % self.size
    
    def put(self, key, value):
        hKey = self._hash_(key)
        current = self.map[hKey]
        
        newNode = Node(key, value)
        
        while current.next:
            # Handle if the key already exists
            if current.next.key == key:
                current.next.value = value
                return
            current = current.next
        current.next = newNode
        
    def get(self, key) -> int:
        hKey = self._hash_(key)
        current = self.map[hKey].next
        
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return -1
    
    def remove(self, key):
        hKey = self._hash_(key)
        current = self.map[hKey]
        
        while current.next:
            # remove the key
            if current.next.key == key:
                current.next = current.next.next
                return
            current = current.next
               
               
               
# Unit testing
class TestMyHashMap(unittest.TestCase):
    def setUp(self):
        self.m = MyHashMap()
        self.m.put(1, 1)
        self.m.put(21,3)
        self.m.put(11,5)


    def test_get(self):
        self.assertEqual(self.m.get(1), 1)
        self.assertEqual(self.m.get(21), 3)
        self.assertEqual(self.m.get(11), 5)
        
    def test_put(self):
        self.m.put(11, 400)
        self.assertEqual(self.m.get(11), 400)
        
    def test_remove(self):
        self.m.remove(11)
        self.assertEqual(self.m.get(11), -1)


if __name__ == "__main__":
    unittest.main()
