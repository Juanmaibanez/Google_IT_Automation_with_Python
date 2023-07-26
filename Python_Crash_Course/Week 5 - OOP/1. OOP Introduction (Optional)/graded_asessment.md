# Graded Assessment

**1.** Let's test your knowledge of using dot notation to access methods in an object. Let's say we have a class called Birds. Birds has two attributes: color and number. Birds also has a method called count() that counts the number of birds (adds a value to number). which of the following lines of code will correctly print the number of birds) Heep in mind, the number os birds is 0 until they are counted!

~~~~python
    bluejay.number = 0
    print(bluejay.number()

    print(bluejay.nuber()

    bluejay.count()
    print(bluejay.number)

    print(bluejay.number)
~~~~

Based on the information provided, none of the given lines of code will correctly print the number of birds. Here's the corrected version:

```python
class Birds:
    def __init__(self):
        self.color = 'unknown'
        self.number = 0

    def count(self):
        self.number += 1

bluejay = Birds()
bluejay.count()
print(bluejay.number)
```

In this code, we create an instance of the Birds class called `bluejay`. We then call the `count()` method on the `bluejay` object to increment the number of birds. Finally, we print the `number` attribute of the `bluejay` object, which will correctly display the number of birds (in this case, 1).

**2.** Creating new instances of a class objects can be great way to keep track of values using attributes associated with the object. The values of these attributes can be easily changed at the object level. The following code illustrates a famous quote by George Bernard Shaw, using objects to represent people. Fill in the blanks to make the code satisfy the behavior described in the quote.

```python
# “If you have an apple and I have an apple and we exchange these apples then
# you and I will still each have one apple. But if you have an idea and I have
# an idea and we exchange these ideas, then each of us will have two ideas.”
# George Bernard Shaw

class Person:
    apples = 0
    ideas = 0

johanna = Person()
johanna.apples = 1
johanna.ideas = 1

martin = Person()
martin.apples = 2
martin.ideas = 1

def exchange_apples(you, me):
#Here, despite G.B. Shaw's quote, our characters have started with       #different amounts of apples so we can better observe the results. 
#We're going to have Martin and Johanna exchange ALL their apples with #one another.
#Hint: how would you switch values of variables, 
#so that "you" and "me" will exchange ALL their apples with one another?
#Do you need a temporary variable to store one of the values?
#You may need more than one line of code to do that, which is OK. 
    	___
    	return you.apples, me.apples
    
def exchange_ideas(you, me):
#"you" and "me" will share our ideas with one another.
#What operations need to be performed, so that each object receives
#the shared number of ideas?
#Hint: how would you assign the total number of ideas to 
#each idea attribute? Do you need a temporary variable to store 
#the sum of ideas, or can you find another way? 
#Use as many lines of code as you need here.
    you.ideas ___
    me.ideas ___
    return you.ideas, me.ideas

exchange_apples(johanna, martin)
print("Johanna has {} apples and Martin has {} apples".format(johanna.apples, martin.apples))
exchange_ideas(johanna, martin)
print("Johanna has {} ideas and Martin has {} ideas".format(johanna.ideas, martin.ideas))
```

Here's the code with the blanks filled in to satisfy the behavior described in the quote:

```python
class Person:
    apples = 0
    ideas = 0

johanna = Person()
johanna.apples = 1
johanna.ideas = 1

martin = Person()
martin.apples = 2
martin.ideas = 1

def exchange_apples(you, me):
    temp = you.apples
    you.apples = me.apples
    me.apples = temp
    return you.apples, me.apples

def exchange_ideas(you, me):
    total_ideas = you.ideas + me.ideas
    you.ideas = total_ideas
    me.ideas = total_ideas
    return you.ideas, me.ideas

exchange_apples(johanna, martin)
print("Johanna has {} apples and Martin has {} apples".format(johanna.apples, martin.apples))
exchange_ideas(johanna, martin)
print("Johanna has {} ideas and Martin has {} ideas".format(johanna.ideas, martin.ideas))
```

This code will correctly exchange the values of `apples` between Johanna and Martin, and also share the total number of `ideas` between them, as described in the quote by George Bernard Shaw.

**3.** The City class has the following attributes: name, country (where the city is located), elevation (measured in meters), and population approximate, according to recent statistics). Fill in the blanks of the max_elevation_city function to return the name of the city and its country (separated by comma), when comparing the 3 defined instances for a specified minimal population. For example, calling the function for a minimum population of 1 million: max_elevation_city(1000000) should return "Sofia, Bulgaria".

```python
# define a basic city class
class City:
	name = ""
	country = ""
	elevation = 0 
	population = 0

# create a new instance of the City class and
# define each attribute
city1 = City()
city1.name = "Cusco"
city1.country = "Peru"
city1.elevation = 3399
city1.population = 358052

# create a new instance of the City class and
# define each attribute
city2 = City()
city2.name = "Sofia"
city2.country = "Bulgaria"
city2.elevation = 2290
city2.population = 1241675

# create a new instance of the City class and
# define each attribute
city3 = City()
city3.name = "Seoul"
city3.country = "South Korea"
city3.elevation = 38
city3.population = 9733509

def max_elevation_city(min_population):
	# Initialize the variable that will hold 
# the information of the city with 
# the highest elevation 
	return_city = City()

	# Evaluate the 1st instance to meet the requirements:
	# does city #1 have at least min_population and
	# is its elevation the highest evaluated so far?
	if ___
		return_city = ___
	# Evaluate the 2nd instance to meet the requirements:
	# does city #2 have at least min_population and
	# is its elevation the highest evaluated so far?
	if ___
		return_city = ___
	# Evaluate the 3rd instance to meet the requirements:
	# does city #3 have at least min_population and
	# is its elevation the highest evaluated so far?
	if ___
		return_city = ___

	#Format the return string
	if return_city.name:
		return ___
	else:
		return ""

print(max_elevation_city(100000)) # Should print "Cusco, Peru"
print(max_elevation_city(1000000)) # Should print "Sofia, Bulgaria"
print(max_elevation_city(10000000)) # Should print ""
```
To fill in the blanks in the `max_elevation_city` function, you can use the following code:

```python
# define a basic city class
class City:
	name = ""
	country = ""
	elevation = 0 
	population = 0

# create a new instance of the City class and
# define each attribute
city1 = City()
city1.name = "Cusco"
city1.country = "Peru"
city1.elevation = 3399
city1.population = 358052

# create a new instance of the City class and
# define each attribute
city2 = City()
city2.name = "Sofia"
city2.country = "Bulgaria"
city2.elevation = 2290
city2.population = 1241675

# create a new instance of the City class and
# define each attribute
city3 = City()
city3.name = "Seoul"
city3.country = "South Korea"
city3.elevation = 38
city3.population = 9733509

def max_elevation_city(min_population):
	# Initialize the variable that will hold 
# the information of the city with 
# the highest elevation 
	return_city = City()

	# Evaluate the 1st instance to meet the requirements:
	# does city #1 have at least min_population and
	# is its elevation the highest evaluated so far?
	if city1.population >= min_population and city1.elevation > return_city.elevation:
		return_city = city1
	# Evaluate the 2nd instance to meet the requirements:
	# does city #2 have at least min_population and
	# is its elevation the highest evaluated so far?
	if city2.population >= min_population and city2.elevation > return_city.elevation:
		return_city = city2
	# Evaluate the 3rd instance to meet the requirements:
	# does city #3 have at least min_population and
	# is its elevation the highest evaluated so far?
	if city1.population >= min_population and city2.elevation > return_city.elevation:
		return_city = city3

	#Format the return string
	if return_city.name:
		return f"{return_city.name}, {return_city.country}"
	else:
		return ""

print(max_elevation_city(100000)) # Should print "Cusco, Peru"
print(max_elevation_city(1000000)) # Should print "Sofia, Bulgaria"
print(max_elevation_city(10000000)) # Should print ""
```

In this code, the `max_elevation_city` function takes a `min_population` parameter and initializes the `return_city` variable to an instance of the City class. It then evaluates each city instance (`city1`, `city2`, `city3`) to check if it meets the requirements of having a population greater than or equal to `min_population` and having a higher elevation than the current `return_city`. If a city meets these requirements, it becomes the new `return_city`. Finally, the function formats and returns the name and country of the `return_city` if it exists, or an empty string otherwise.

**4.** What makes an object different from class?

1. An object represents and defines a concept

2. An object is a specific instance of a class

3. An object is a template for a class

4. Objects don't have accesible variables

The correct answer is:

2. An object is a specific instance of a class

An object is a specific instance of a class. A class is a blueprint or template that defines the properties (attributes) and behaviors (methods) that objects of that class will have. When you create an object, you are creating a specific instance of that class with its own unique set of attribute values. Objects have their own state (attribute values) and can perform actions (methods) defined by the class. Objects can also have accessible variables, which are the attributes defined in the class.

**5.** We have two pieces of furniture: a brown wood table and a red leather couch. Fill in the blanks following the creation of each Furniture class instance. so that the describe_furniture function can format a sentence that describes these pieces as follow:"This piece of furniture is made of {color}{material}"

```python
class Furniture:
	color = ""
	material = ""

table = Furniture()
___
___

couch = Furniture()
___
___

def describe_furniture(piece):
	return ("This piece of furniture is made of {} {}".format(piece.color, piece.material))

print(describe_furniture(table)) 
# Should be "This piece of furniture is made of brown wood"
print(describe_furniture(couch)) 
# Should be "This piece of furniture is made of red leather"
```

To fill in the blanks and achieve the desired output, you can use the following code:

```python
class Furniture:
    color = ""
    material = ""

table = Furniture()
table.color = "brown"
table.material = "wood"

couch = Furniture()
couch.color = "red"
couch.material = "leather"

def describe_furniture(piece):
    return "This piece of furniture is made of {} {}".format(piece.color, piece.material)

print(describe_furniture(table))  # Should be "This piece of furniture is made of brown wood"
print(describe_furniture(couch))  # Should be "This piece of furniture is made of red leather"
```

In this code, the `Furniture` class is defined with the `color` and `material` attributes. Two instances of the `Furniture` class, `table` and `couch`, are created and their attributes are set accordingly. The `describe_furniture` function takes a `piece` parameter, which is an instance of the `Furniture` class. It returns a formatted string that describes the piece of furniture using the `color` and `material` attributes of the `piece` object. The `print` statements at the end demonstrate the expected output.