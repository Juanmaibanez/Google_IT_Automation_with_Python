# Instance Methods

Create a Dog class with dog_years based on the Piglet class shown before (one human year is about 7 dog years).

```python
class Dog:
  years = 0
  __
    
fido=Dog()
fido.years=3
print(fido.dog_years())
```

To make the code work and print the dog's age in dog years, you can add a method called `dog_years` to the `Dog` class. Here's the modified code:

```python
class Dog:
    years = 0
    
    def dog_years(self):
        return self.years * 7

fido = Dog()
fido.years = 3
print(fido.dog_years())  # Should print 21
```

In this code, the `Dog` class is defined with the `years` attribute. The `dog_years` method is added to the class, which multiplies the `years` attribute by 7 to calculate the dog's age in dog years. Finally, an instance of the `Dog` class named `fido` is created, and its `years` attribute is set to 3. The `dog_years` method is then called on the `fido` instance, and the result is printed, which should be 21.

    21

    Awesome! You've now learned about writing your own methods!