**List Comprehension Examples**

You can create a list from a sequence using a **for** loop, but there’s a more streamlined way to do this by using a list comprehension. List comprehensions allow you to create a new list from a sequence or a range in a single line.


**Simple List Comprehension**

For example, **[ x*2 for x in range(1,11) ]** is a simple list comprehension. This single line of code iterates over a range from 1 to 10, multiplies each element in the range by 2, and creates a new list from all multiples of 2 from 2 to 20.

```python
### Simple List Comprehension
print("List comprehension result:")

# The following list comprehension compacts several lines 
# of code into one line:
print([x*2 for x in range(1,11)]) 



### Long form for loop
print("Long form code result:")

# The list comprehension above accomplishes the same result as
# the long form version of the code:
my_list = []
for x in range(1,11):
   my_list.append(x*2)
print(my_list)
```

**List Comprehension with Conditional Statement**

You can also use conditionals with list comprehensions to build even more complex and powerful statements. You can do this by appending an if statement to the end of the list comprehension. For example, **[ x for x in range(1,101) if x % 10 == 0 ]** generates a new list containing all the integers divisible by 10 from 1 to 100. The if statement evaluates each value in the range from 1 to 100 to check if it’s evenly divisible by 10. If it is, the number is added to a new list.

```python
### List Comprehension with Conditional Statement
print("List comprehension result:")

# The following list comprehension compacts multiple lines 
# of code into one line:
print([ x for x in range(1,101) if x % 10 == 0 ])

### Long form for loop with nested if-statement
print("Long form code result:")

# The list comprehension above accomplishes the same result as
# the long form version of the code:
my_list = []
for x in range(1,101):
  if x % 10 == 0:
    my_list.append(x)
print(my_list)
```

List comprehensions can be really powerful, but they can also be complex, resulting in code that’s hard to read. Be careful when using them, since it might make it more difficult for someone else looking at your code to easily understand what the code is doing. It is a best practice to add descriptive comments about any list comprehensions used in your code. This helps to communicate the purpose of list comprehensions to other coders. Comments will also help you remember the goal of the code when performing future code additions and maintenance.   

