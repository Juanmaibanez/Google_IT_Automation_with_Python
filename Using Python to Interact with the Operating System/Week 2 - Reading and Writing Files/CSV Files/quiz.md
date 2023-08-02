1. We're working with a list of flowers and some information about each one. The create_file function writes this information to a CSV file. The contents_of-file function reads this file into records and returns the information in a nicely formatted block. Fill in the gaps of the contents_of_file function to turn the data in the CSV file into a dictionary using DictReader.

```python
import os
import csv

# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")


# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ""

  # Call the function to create the file 
  create_file(filename)

  # Open the file
  ___
    # Read the rows of the file into a dictionary
    ___
    # Process each item of the dictionary
    for ___:
      return_string += "a {} {} is {}\n".format(row["color"], row["name"], row["type"])
  return return_string


#Call the function
print(contents_of_file("flowers.csv"))
```

```python
import os
import csv

# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")


# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ""

  # Call the function to create the file 
  create_file(filename)

  # Open the file
  with open(filename, "r") as file:
    # Read the rows of the file into a dictionary
    reader = csv.DictReader(file)
    # Process each item of the dictionary
    for row in reader:
      return_string += "a {} {} is {}\n".format(row["color"], row["name"], row["type"])
  return return_string


#Call the function
print(contents_of_file("flowers.csv"))
```

Let's go through the code step by step:

1. The `create_file` function is used to create a CSV file with some data in it. It opens the file in write mode and writes the header row and several rows of flower data.

2. The `contents_of_file` function takes a filename as input and returns a nicely formatted string containing the information from the CSV file.

3. Inside the `contents_of_file` function, a variable `return_string` is initialized to an empty string. This variable will store the formatted information.

4. The `create_file` function is called to create the CSV file with the flower data.

5. The file is then opened using the `open` function with the filename and "r" (read) mode.

6. The `csv.DictReader` class is used to read the rows of the file into a dictionary. This class automatically interprets the first row of the file as the header row and maps each subsequent row to a dictionary where the keys are the header column names and the values are the corresponding values in each row.

7. A `for` loop is used to iterate over each row in the `reader` object.

8. Inside the loop, the values from each row are accessed using the keys "color", "name", and "type" and formatted into a string using the `format` method. This string is then appended to the `return_string` variable.

9. After processing all the rows, the `return_string` variable containing the formatted information is returned.

10. Finally, the `contents_of_file` function is called with the filename "flowers.csv" and the result is printed.

The output of the program will be:

```
a pink carnation is annual
a yellow daffodil is perennial
a blue iris is perennial
a red poinsettia is perennial
a yellow sunflower is annual
```

This output shows the color, name, and type of each flower in the CSV file, formatted as specified in the `return_string` variable.

2. Using the CSV file of flowers again, fill in the gaps of the contents_of_file function to process the data without turning it into a dictionary. How do you skip over the header record with the field names?

```python
import os
import csv

# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")

# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ""

  # Call the function to create the file 
  create_file(filename)

  # Open the file
  ___
    # Read the rows of the file
    rows = ___
    # Process each row
    for row in rows:
      ___ = row
      # Format the return string for data rows only

          return_string += "a {} {} is {}\n".format(___)
  return return_string

#Call the function
print(contents_of_file("flowers.csv"))
```

To skip over the header record with the field names, you can use the `next()` function to read and discard the first row before processing the rest of the rows. Here's the modified code:

```python
import os
import csv

# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")

# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ""

  # Call the function to create the file 
  create_file(filename)

  # Open the file
  with open(filename, "r") as file:
    # Create a CSV reader object
    reader = csv.reader(file)
    
    # Skip the header row
    next(reader)
    
    # Read the rows of the file
    rows = list(reader)
    
    # Process each row
    for row in rows:
      name, color, flower_type = row
      
      # Format the return string for data rows only
      return_string += "a {} {} is {}\n".format(color, name, flower_type)
  
  return return_string

# Call the function
print(contents_of_file("flowers.csv"))
```

This code will skip over the header row and process the remaining rows, formatting the return string for each data row.