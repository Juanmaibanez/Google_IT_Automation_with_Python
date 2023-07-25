# Graded Assessment

**1.** Fill in the blanks to complete the "first_character" function. This function should return the first character of any string passed in. Complete the string operation needed in this function so that input like "Hello, World!" will produce the output "H".

```python
def first_character(string):
    # Complete the return statement using a string operation.
    return ___ 


print(first_character("Hello, World")) # Should print H
print(first_character("Python is awesome")) # Should print P
print(first_character("Keep going")) # Should print K
```

The code you provided is already correct. The `first_character` function correctly returns the first character of the input string by accessing the character at index 0 using the string indexing operation `string[0]`. Here's the code with the example outputs:

```python
def first_character(string):
    # Complete the return statement using a string operation.
    return string[0]


print(first_character("Hello, World"))  # Should print H
print(first_character("Python is awesome"))  # Should print P
print(first_character("Keep going"))  # Should print K
```

When you run this code, it will correctly print the first character of each input string as expected.

~~~~
    H
    P
    K
~~~~

**2.** Fill in the blanks to complete the "string_worlds" function. This function should split up the words in the given "string" and return the number of words in the "string". Complete the string operation and method needed in ths function so that a function call like "string_words("Hello, World)!" will return the output "2".

```python
def string_words(string):
    # Complete the return statement using both a string operation and 
    # a string method in a single line.
    return ___


print(string_words("Hello, World")) # Should print 2
print(string_words("Python is awesome")) # Should print 3
print(string_words("Keep going")) # Should print 2
print(string_words("Have a nice day")) # Should print 4
```

To split up the words in the given string and return the number of words, you can use the `split()` method to split the string into a list of words, and then use the `len()` function to get the length of the list. Here's the updated code:

```python
def string_words(string):
    # Complete the return statement using both a string operation and 
    # a string method in a single line.
    return len(string.split())


print(string_words("Hello, World"))  # Should print 2
print(string_words("Python is awesome"))  # Should print 3
print(string_words("Keep going"))  # Should print 2
print(string_words("Have a nice day"))  # Should print 4
```

This code will split the input string into a list of words using the `split()` method, and then return the length of the list using the `len()` function.

**3.** Consider the following scenario about using Python list:

A professor gave his two assistants, Jaime and Drew, the task of keeping an attendance list of students in the order they arrive in the classroom. Drew was the first one to note which students arrived, and then Jaime took over. After the class, they each entered their lists into the computer and emailed them to the professor. The professor wants to combine the two lists into one, in the order of each student's arrival. Jaime emailed a follow-up, saying that her list is in reverse order.

Complete the code to combine the two lists into one in the order of: the contents of Drew's list, followed by Jaime's list in reverse order, to produce an accurate list of students as they arrived: This function should:

   1. accept two list through the function's parameters;

   2. reverse the order os "list1";

   3. combine the two lists so that "list2" comes firstm, followed b y "list1";

   4. return  the new list.

```python
def combine_lists(list1, list2):


  combined_list = ___ # Initialize an empty list variable
  ___ # Reverse the order of "list1"
  ___ # Combine the two lists 
  combined_list = list2
  return combined_list  
  
Jaimes_list = ["Alma", "Chika", "Benjamin", "Jocelyn", "Oakley"]
Drews_list = ["Minna", "Carol", "Gunnar", "Malena"]


print(combine_lists(Jaimes_list, Drews_list))
# Should print ['Minna', 'Carol', 'Gunnar', 'Malena', 'Oakley', 'Jocelyn', 'Benjamin', 'Chika', 'Alma']
```

Here's the code:

```python
def combine_lists(list1, list2):
    combined_list = []  # Initialize an empty list variable
    list1.reverse()  # Reverse the order of "list1"
    combined_list = list2 + list1  # Combine the two lists
    return combined_list

Jaimes_list = ["Alma", "Chika", "Benjamin", "Jocelyn", "Oakley"]
Drews_list = ["Minna", "Carol", "Gunnar", "Malena"]

print(combine_lists(Jaimes_list, Drews_list))
# Should print ['Minna', 'Carol', 'Gunnar', 'Malena', 'Oakley', 'Jocelyn', 'Benjamin', 'Chika', 'Alma']
```

This code will reverse the order of `list1` using the `reverse()` method, combine `list2` and the reversed `list1` using the `+` operator, and return the combined list.

    ['Minna', 'Carol', 'Gunnar', 'Malena', 'Oakley', 'Jocelyn', 'Benjamin', 'Chika', 'Alma']

**4.** Fill in the blanks to complete the "increments" function. This function should use a list comprehension to create a list of numbers incremented by 2(n+2). The function receives two variables and should return a list of incremented consecutive number between "star" and "end" inclusively (meaning the range should include both the "start" and "end" values). Complete the list comprehension in this function so that input like "square(2,3)" will produce the output "[4,5]".

```python
def increments(start, end):
    return [ ___ ] # Create the required list comprehension.


print(increments(2, 3)) # Should print [4, 5]
print(increments(1, 5)) # Should print [3, 4, 5, 6, 7]
print(increments(0, 10)) # Should print [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
```

To create a list of numbers incremented by 2(n+2) using a list comprehension, you can use the range function to generate a sequence of numbers from `start` to `end` (inclusive), and then apply the increment formula `2*(n+2)` to each number in the range. Here's the updated code:

```python
def increments(start, end):
    return [2*(n+2) for n in range(start, end+1)]


print(increments(2, 3))  # Should print [4, 5]
print(increments(1, 5))  # Should print [3, 4, 5, 6, 7]
print(increments(0, 10))  # Should print [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
```

This code will generate a list comprehension that iterates over the range from `start` to `end+1` (inclusive), and for each number `n`, it applies the increment formula `2*(n+2)` to create the incremented number. The resulting list will contain all the incremented numbers.

    [8, 10]
    [6, 8, 10, 12, 14]
    [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]

**5.** Fill in the blanks to complete the "car_listing" function. This function accepts a "car_prices" dictionary. It should iterate through the keys (car models) and values (car prices) in that dictionary. For each item pair, the function should format a string so that a dictionary entry like ""Kia soul:19000" will print "A Kia Soul costs 19000 dollars".. Each new string should appear on its own line.

```python
def car_listing(car_prices):
  result = ""
  # Complete the for loop to iterate through the key and value items 
  # in the dictionary.
  for __ 
    result += ___ # Use a string method to format the required string. 
  return result

print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))

# Should print:
# A Kia Soul costs 19000 dollars
# A Lamborghini Diablo costs 55000 dollars
# A Ford Fiesta costs 13000 dollars
# A Toyota Prius costs 24000 dollars
```

To iterate through the key-value pairs in the `car_prices` dictionary and format a string for each pair, you can use the `items()` method to get the key-value pairs, and then use string formatting to create the required string. Here's the updated code:

```python
def car_listing(car_prices):
    result = ""
    # Complete the for loop to iterate through the key and value items 
    # in the dictionary.
    for car, price in car_prices.items():
        result += f"A {car} costs {price} dollars\n"  # Use string formatting to create the required string.
    return result

print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))

# Should print:
# A Kia Soul costs 19000 dollars
# A Lamborghini Diablo costs 55000 dollars
# A Ford Fiesta costs 13000 dollars
# A Toyota Prius costs 24000 dollars
```

This code will iterate through the key-value pairs in the `car_prices` dictionary using the `items()` method. For each pair, it will use string formatting (`f"A {car} costs {price} dollars\n"`) to create the required string and append it to the `result` variable. Finally, it will return the `result` string.

    A Kia Soul costs 19000 dollars
    A Lamborghini Diablo costs 55000 dollars
    A Ford Fiesta costs 13000 dollars
    A Toyota Prius costs 24000 dollars

**6.** Consider the following scenario using Python dictionaries and lists:

Tessa and Rick are hosting a party. Before they send out invitations, they want to add all of the people they are inviting yo a dictionary so they can also add how many guests each friend is bringing to the party:

Complete the function so that it accepts a list os people, the iterates over the list and adds all of the names (elements) to the dictionary as key with a starting value of 0. Tessa and Rick plan to update these values with the n umber of guests their friends will bring with them to the party. Then, print the new dictionaty.

This function should:

1. accept a list variable named ""guest_list" through the function's parameters;

2. add the contents os the list as keys to a new, blank dictionary;

3. assign each new key with the value 0:

4. print the new dictionary.

```python
def setup_guests(guest_list):
    # loop over the guest list and add each guest to the dictionary with
    # an initial value of 0
    result = ___ # Initialize a new dictionary 
    for ___ # Iterate over the elements in the list 
        ___ # Add each list element to the dictionary as a key with 
            # the starting value of 0
    return result

guests = ["Adam","Camila","David","Jamal","Charley","Titus","Raj","Noemi","Sakira","Chidi"]

print(setup_guests(guests))
# Should print {'Adam': 0, 'Camila': 0, 'David': 0, 'Jamal': 0, 'Charley': 0, 'Titus': 0, 'Raj': 0, 'Noemi': 0, 'Sakira': 0, 'Chidi': 0}
```

To complete the `setup_guests` function as described, you can follow these steps:

1. Initialize a new dictionary.
2. Iterate over the elements in the `guest_list`.
3. Add each list element to the dictionary as a key with the starting value of 0.
4. Return the resulting dictionary.

Here's the updated code:

```python
def setup_guests(guest_list):
    # Initialize a new dictionary
    result = {}
    for guest in guest_list:
        # Add each list element to the dictionary as a key with the starting value of 0
        result[guest] = 0
    return result

guests = ["Adam", "Camila", "David", "Jamal", "Charley", "Titus", "Raj", "Noemi", "Sakira", "Chidi"]

print(setup_guests(guests))
# Should print {'Adam': 0, 'Camila': 0, 'David': 0, 'Jamal': 0, 'Charley': 0, 'Titus': 0, 'Raj': 0, 'Noemi': 0, 'Sakira': 0, 'Chidi': 0}
```

This code will create a new dictionary called `result` and iterate over each element in the `guest_list`. For each element, it will add the element as a key to the dictionary with the starting value of 0. Finally, it will return the resulting dictionary.

    {'Adam': 0, 'Camila': 0, 'David': 0, 'Jamal': 0, 'Charley': 0, 'Titus': 0, 'Raj': 0, 'Noemi': 0, 'Sakira': 0, 'Chidi': 0}

**7.** Use a dictionary to count the frequency of numbers in the given "text" string. Only numbers should be counted. Do not count blank spaces. letters, or punctuation. Complete the function so that input like "1001000111101" will return a dictionary that holds the count of each number that occurs in the string {'1': 7, '0': 6}. This function should:

1. accept a string "text" variable through the function's parameters;

2. initialize an new dictionary:

3. iterate over each text character to check if the character is a number:

4. count the frequency of numbers in the input string, ignoring all other characters;

5. populate the new dictionary with the numbers a keys, ensuring each key is unique, and assign the value foe each key with the count of that number;

6. return the new dictionary.

```python
def count_numbers(text):
  # Initialize a new dictionary.
  dictionary = ___ 
  # Complete the for loop to iterate through each "text" character.
  for ___
    # Complete the if-statement using a string method to check if the
    # character is a number.
    if___:
      # Complete the if-statement using a logical operator to check if 
      # the number is not already in the dictionary.
      if ___:
           # Use a dictionary operation to add the number as a key
           # and set the initial count value to zero.
           ___
      # Use a dictionary operation to increment the number count value 
      # for the existing key.
      ___
  return dictionary

print(count_numbers("1001000111101"))
# Should be {'1': 7, '0': 6}

print(count_numbers("Math is fun! 2+2=4"))
# Should be {'2': 2, '4': 1}

print(count_numbers("This is a sentence."))
# Should be {}

print(count_numbers("55 North Center Drive"))
# Should be {'5': 2}
```

To count the frequency of numbers in the given `text` string and store the counts in a dictionary, you can follow these steps:

1. Initialize a new dictionary.
2. Iterate over each character in the `text` string.
3. Check if the character is a number using the `isdigit()` method.
4. If the character is a number and not already in the dictionary, add it as a key with an initial count value of 0.
5. Increment the count value for the existing key in the dictionary.
6. Return the resulting dictionary.

Here's the updated code:

```python
def count_numbers(text):
    # Initialize a new dictionary.
    dictionary = {}
    # Iterate over each character in the "text" string.
    for char in text:
        # Check if the character is a number using the `isdigit()` method.
        if char.isdigit():
            # Check if the number is not already in the dictionary.
            if char not in dictionary:
                # Add the number as a key and set the initial count value to zero.
                dictionary[char] = 0
            # Increment the number count value for the existing key.
            dictionary[char] += 1
    return dictionary

print(count_numbers("1001000111101"))
# Should be {'1': 7, '0': 6}

print(count_numbers("Math is fun! 2+2=4"))
# Should be {'2': 2, '4': 1}

print(count_numbers("This is a sentence."))
# Should be {}

print(count_numbers("55 North Center Drive"))
# Should be {'5': 2}
```

This code will iterate over each character in the `text` string and check if it is a number using the `isdigit()` method. If the character is a number and not already in the dictionary, it will add it as a key with an initial count value of 0. If the key already exists, it will increment the count value. Finally, it will return the resulting dictionary.

    {'1': 7, '0': 6}
    {'2': 2, '4': 1}
    {}
    {'5': 2}

**8.** what do the following commands return when animal="Hippopotamus"?

```python
print(animal[3:6])
print(animal[-5])
print(animal[10:])
```
When `animal = "Hippopotamus"`, the following commands will return the following results:

1. `print(animal[3:6])` will return `"pop"`. This is because the slice `[3:6]` extracts the characters at indices 3, 4, and 5 from the string `animal`, which are "p", "o", and "p" respectively.

2. `print(animal[-5])` will return `"t"`. This is because the index `-5` refers to the fifth character from the end of the string `animal`, which is "t".

3. `print(animal[10:])` will return `"us"`. This is because the slice `[10:]` extracts all the characters starting from index 10 until the end of the string `animal`, which are "u" and "s".

**9.** What does the list "music_genres" contain after these commands are executed?

```python
music_genres = ["rock", "pop", "country"]
music_genres.append("blues")
```

After executing the given commands, the list `music_genres` will contain the following elements:

`["rock", "pop", "country", "blues"]`

The `append()` method is used to add the element "blues" to the end of the `music_genres` list. Therefore, the list will have four elements: "rock", "pop", "country", and "blues".

**10.** What do the following commands return?

```python
teacher_names= {"Math": "Aniyah Cook", "Science": "Ines Bisset", "Engineering": "Wayne Branon"}
teacher_names.values()
```

The commands will return the values of the `teacher_names` dictionary.

Output:

```python
dict_values(['Aniyah Cook', 'Ines Bisset', 'Wayne Branon'])
```

The `values()` method returns a view object that contains the values of the dictionary. In this case, it will return `dict_values(['Aniyah Cook', 'Ines Bisset', 'Wayne Branon'])`, which is a view object containing the values "Aniyah Cook", "Ines Bisset", and "Wayne Branon".