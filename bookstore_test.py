import unittest
import bookstore

class TestBookMethods(unittest.TestCase):
    
    def setUp(self):
        self.book = bookstore.Book("Python Programming", "John Doe", 29.99, 10)
        
    def test_book_initialization(self):
        self.assertEqual(self.book.title, "Python Programming")
    
    def test_update_book(self):
        self.book.update_book("new Title", "JJ", 0, 0)
        self.assertNotEqual(self.book.title, "Python Programming")

if __name__ == "__main__":
    unittest.main()