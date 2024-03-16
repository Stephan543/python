# Create a word counter that takes input text and outputs the number of words.

class Text:
    def __init__(self, txt) -> None:
        self.txt = txt.split()
    
    def count_string(self) -> int:        
        return len(self.txt)
        
    
user_input = input("Enter your text: ")

text_object = Text(user_input)

count = text_object.count_string()

print(f"There are {count} words")