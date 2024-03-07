class Book: 
    def __init__(self, title, author, price, quantity) -> None:
        self.title = title
        self.author = author
        self.price = price
        self.quantity = quantity        
        
    def update_book(self, title, author, price, quantity):
        self.title = title
        self.author = author
        self.price = price
        self.quantity = quantity        
        

class Customer:
    def __init__(self) -> None:
        self.shoppingCart = []
        self.orderHistory = []
    
    # add_book_to_cart assume each book is unique
    def add_book_to_cart(self, book):
        self.shoppingCart.append(book)
    
    
    def remove_book_from_cart(self, book):
        self.shoppingCart.remove(book)
        
    def place_order(self):
        placedOrder = Order(self, self.shoppingCart)
        self.orderHistory.append(placedOrder)
        self.shoppingCart = []
        
    
class Order:
    def __init__(self, customer, books) -> None:
        self.customer = customer
        self.books = books
        
        
class Catalog:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def remove_book(self, book):
        self.books.remove(book)
        
    

    
    
book1 = Book("book1", "steph", 10, 2)
book2 = Book("book2", "steph", 10, 2)
book3 = Book("book3", "steph", 10, 2)

customer1 = Customer()
customer1.add_book_to_cart(book1)
customer1.add_book_to_cart(book2)
customer1.add_book_to_cart(book3)

customer1.remove_book_from_cart(book2)
book3.update_book("book4", "cat", 1, 1)
customer2 = Customer()

