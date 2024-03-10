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

    
book1 = bookstore.Book("book1", "steph", 10, 2)
book2 = bookstore.Book("book2", "steph", 10, 2)
book3 = bookstore.Book("book3", "steph", 10, 2)

class TestCustomerMethods(unittest.TestCase):

    
    def setUp(self) -> None:

        self.customer = bookstore.Customer()
        
        self.customer.add_book_to_cart(book1)
        self.customer.add_book_to_cart(book2)
        self.customer.add_book_to_cart(book3)
        
    def test_remove_book_from_cart(self):
        self.customer.remove_book_from_cart(book2)
        self.assertEqual(self.customer.shoppingCart, [book1, book3])
        self.customer.remove_book_from_cart(book3)
        self.assertEqual(self.customer.shoppingCart, [book1])
        
        
if __name__ == "__main__":
    unittest.main()