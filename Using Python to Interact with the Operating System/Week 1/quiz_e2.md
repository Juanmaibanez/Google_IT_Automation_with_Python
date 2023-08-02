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

The error is occurring because the directory "PythonPrograms" does not exist in the current working directory. To fix this, you can use the `os.path.join()` function to create the full path to the directory.

Here's the modified code:

```python
import os

def new_directory(directory, filename):
  # Create the full path to the directory
  directory_path = os.path.join(os.getcwd(), directory)

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

In this code, `os.path.join()` is used to create the full path to the directory by joining the current working directory (`os.getcwd()`) with the directory name ("PythonPrograms"). This ensures that the correct directory path is used when creating the directory and the file.

```
Error on line 19:
    print(new_directory("PythonPrograms", "script.py"))
Error on line 9:
    os.mkdir(directory_path)
OSError: [Errno 30] Read-only file system: '/var/task/PythonPrograms'
```

The error message suggests that the current working directory is a read-only file system, which means you don't have permission to create a new directory or file in that location. 

To fix this, you can specify a different directory where you have write permissions. For example, you can use the `/tmp` directory, which is commonly writable.

Here's the modified code:

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

In this code, the `directory_path` is set to `/tmp/PythonPrograms`, which is a writable directory. This should resolve the issue and allow you to create the directory and file successfully.