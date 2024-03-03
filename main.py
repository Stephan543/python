from some_script import HelloWorld
from users import Users, Address
from dataclasses import dataclass

import unittest

# HelloWorld()

user1 = Users("Stephan", 27, "Elm", "Mississauga")
print(user1.address)
print(user1)
print("city: " + user1.address.city)

# Table Driven tests

class TestUsersofAge(unittest.TestCase):
    def test_ofAge(self):
        # TestCase = [
        #     {
        #         "name": "person_of_age_should_be_true",
        #         "age": 27,
        #         "expected": True
        #     },
        #     {
        #         "name": "person_not_of_age_should_be_false",
        #         "age": 20,
        #         "expected": True
        #     }
        #     ]

        @dataclass
        class TestCase:
            name: str
            age: int
            expected: bool

        test_cases = [
            TestCase(name="person_of_age_should_be_true", age=27, expected=True),
            TestCase(name="person_of_age_should_be_true", age=20, expected=False),

        ]

        for t in test_cases:
            user = Users("test", t.age, "testStreet", "testCity")
            result = user.of_age()
            self.assertEqual(
                result, 
                t.expected,
                "Test: {}, Expected: {}, Actual: {}".format(
                    t.name,
                    t.expected,
                    result
                ))

if __name__ == "__main__":
    unittest.main()