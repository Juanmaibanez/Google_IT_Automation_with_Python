Let’s create a new class together and inherit from it. Below we have a base class called Clothing. Together, let’s create a second class, called Shirt, that inherits methods from the Clothing class. Fill in the blanks to make it work properly.

```python
class Clothing:
  material = ""
  def __init__(self,name):
    self.name = name
  def checkmaterial(self):
	  print("This {} is made of {}".format(self.___,self.___))
			
class Shirt(___):
  material="Cotton"

polo = Shirt("Polo")
polo.checkmaterial()
```

To create the `Shirt` class that inherits from the `Clothing` class, you can modify the code as follows:

```python
class Clothing:
    material = ""

    def __init__(self, name):
        self.name = name

    def checkmaterial(self):
        print("This {} is made of {}".format(self.name, self.material))


class Shirt(Clothing):
    material = "Cotton"

polo = Shirt("Polo")
polo.checkmaterial()
```
    This Polo is made of Cotton

In the updated code, the `Shirt` class is defined with `Clothing` as its base class by specifying `Clothing` in parentheses after the class name. This indicates that `Shirt` inherits from `Clothing` and can access its methods and attributes.

The `material` attribute is set to "Cotton" in the `Shirt` class, overriding the `material` attribute inherited from the `Clothing` class.

The `polo` object is created as an instance of the `Shirt` class, passing "Polo" as the name argument to the `__init__` method inherited from the `Clothing` class.

Finally, the `polo.checkmaterial()` method is called, which invokes the `checkmaterial` method defined in the `Clothing` class. This method prints the name of the clothing object (in this case, "Polo") and the material attribute of the object's class (in this case, "Cotton").