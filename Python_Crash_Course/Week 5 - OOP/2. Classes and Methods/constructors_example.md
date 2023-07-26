# Constructors and Other Special Methods

Want to see this in action?
 
In this code, there's a Person class that has an attribute name, which gets set when constructing the object. Fill in the blanks so that :

1. when an instance of the class is created, the attribute gets set correctly.
  
2. when the greeting() method is called, the greeting states the assigned name.

```python
class Person:
    def __init__(self, name):
        self.name = ___
    def greeting(self):
        # Should return "hi, my name is " followed by the name of the Person.
        return ___ 

# Create a new instance with a name of your choice
some_person = ___  
# Call the greeting method
print(some_person.___)
```

To complete the code, you can use the following:

```python
class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        return "Hi, my name is " + self.name

# Create a new instance with a name of your choice
some_person = Person("John")

# Call the greeting method
print(some_person.greeting())
```

    Hi, my name is John

This code defines a `Person` class with an `__init__` method that takes a `name` parameter and assigns it to the `self.name` attribute. The `greeting` method returns a string that includes the person's name. 

To create a new instance of the `Person` class, you can pass a name of your choice as an argument. In this example, the name "John" is used. Finally, you can call the `greeting` method on the `some_person` instance to print the greeting message.
