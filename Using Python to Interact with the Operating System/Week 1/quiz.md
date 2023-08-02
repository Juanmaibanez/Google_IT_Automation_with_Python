1. The create_python_script function creates a new python script in the current working directory, adds the line of comments to it declared by the 'comments' variable, and returns the size of the new file. Fill in the gaps to create a script called "program.py".

```python
def create_python_script(filename):
  comments = "# Start of a new Python program"
  with ___:
    filesize = ___
  return(filesize)

print(create_python_script("program.py"))
```


```python
import os

def create_python_script(filename):
    comments = "# Start of a new Python program"
    with open(filename, 'w') as file:
        file.write(comments)
    filesize = os.path.getsize(filename)
    return filesize

print(create_python_script("program.py"))
```

In this code, the `create_python_script` function takes a `filename` parameter and assigns the comments to the `comments` variable. It then uses the `open` function with the mode `'w'` to open the file in write mode. The comments are written to the file using the `write` method. After that, the `os.path.getsize` function is used to get the size of the file. Finally, the size of the file is returned and printed using the `print` statement.

2. The new_directory function creates a new directory inside the current working directory, then creates a new empty file inside the new directory, and retruns the list of files in that directory. Fill in the gaps to create a file "script.py" in the directory "PythonPrograms".

```python
import os

def new_directory(directory, filename):
  # Before creating a new directory, check to see if it already exists
  if os.path.isdir(directory) == False:
    ___

  # Create the new file inside of the new directory
  os.chdir(___)
  with open (___) as file:
    pass

  # Return the list of files in the new directory
  return ___

print(new_directory("PythonPrograms", "script.py"))
```

```python
import os

def new_directory(directory, filename):
  # Create the full path to the directory
  directory_path = os.path.join('/tmp', directory)

  # Before creating a new directory, check to see if it already exists
  if not os.path.isdir(directory_path):
    os.mkdir(directory_path)

  # Create the new file inside the new directory
  os.chdir(directory_path)
  with open(filename, 'w') as file:
    pass

  # Return the list of files in the new directory
  return os.listdir(directory_path)

print(new_directory("PythonPrograms", "script.py"))
```


4. The fiel_date function creates a new file in the current working directory, checks the date that the file was modified, and returns just the date portion of the timestamp in the format of yyyy-mm-dd. Fill in the gaps to create a file called "newfile.txt" and check the date that it was modified.

```python
import os
import datetime

def file_date(filename):
  # Create the file in the current directory
  ___
  timestamp = ___
  # Convert the timestamp into a readable format, then into a string
  ___
  # Return just the date portion 
  # Hint: how many characters are in “yyyy-mm-dd”? 
  return ("{___}".format(___))

print(file_date("newfile.txt")) 
# Should be today's date in the format of yyyy-mm-dd
```

Here's the completed code:

```python
import os
import datetime

def file_date(filename):
  # Check if the file exists
  if os.path.exists(filename):
    # Get the timestamp when the file was last modified
    timestamp = os.path.getmtime(filename)
    # Convert the timestamp into a readable format, then into a string
    date = datetime.datetime.fromtimestamp(timestamp).date()
    # Return just the date portion
    return date.strftime("%Y-%m-%d")
  else:
    return "File does not exist"

print(file_date("existingfile.txt")) 
# Should be the modified date of the existing file in the format of yyyy-mm-dd

print(file_date("newfile.txt")) 
# Should print "File does not exist" since the file does not exist
```

5. The parent_directory function returns the name of the directory that's located just above the current working directory. Remember that '..' is a relative path alias taht means "go to the parent directory". Fill in the gaps to complete this function.

```python
import os
def parent_directory():
  # Create a relative path to the parent 
  # of the current working directory 
  relative_parent = os.path.join(___, ___)

  # Return the absolute path of the parent directory
  return ___

print(parent_directory())
```

```python
import os
def parent_directory():
  # Create a relative path to the parent 
  # of the current working directory 
  relative_parent = os.path.join(os.getcwd(), '..')

  # Return the absolute path of the parent directory
  return os.path.abspath(relative_parent)

print(parent_directory())
```