class Animal:
    name = ""
    category = ""
    
    def __init__(self, name):
        self.name = name
    
    def set_category(self, category):
        self.category = category
    
class Turtle(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.set_category("reptile")
        
print(Turtle.category)