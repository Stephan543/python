class Users:
    def __init__(self, name, age, street,  city) -> None:
        self.name = name
        self.age = age
        self.address = Address(street, city)

    def __str__(self) -> str:
        return f"Users(name={self.name}, age={self.age})"
    
    def of_age(self) -> bool:
        return self.age >= 21

class Address:
    def __init__(self, street, city) -> None:
        self.street = street
        self.city = city

    def __str__(self) -> str:
        return f"Address(street={self.street}, city={self.city})"