# Collections

1. [What is this?](#What-is-this?)
2. [How to install?](#How-to-install?)
3. [How to use it?](#How-to-use-it?)
    1. [Development](#Development)
    2. [Usage](#Usage)
4. [References](#References)

## What is this?

The collection Module in Python provides different types of containers. A Container is an object that is used to store
different objects and provide a way to access the contained objects and iterate over them. Some of the built-in
containers are Tuple, List, Dictionary, etc. In this article, we will discuss the different containers provided by the
collections module.

## How to install?

Nothing todo, it's available by default in the python environment :)

## How to use it?

### Development

Import the module

```python 
import collections
```

Or better, load only the concerned function which can be:

- Counters
- OrderedDict
- DefaultDict
- ChainMap
- NamedTuple
- DeQue
- UserDict
- UserList
- UserString

Example:

```python
from collections import UserList
```

Integrate it in your code

```python
from collections import UserList


# Creating a List where deletion is not allowed 
class MyList(UserList):

    # Function to stop deletion from List 
    def remove(self, s=None):
        raise RuntimeError("Deletion not allowed")

    # Function to stop pop from List 
    def pop(self, s=None):
        raise RuntimeError("Deletion not allowed")


# Driver's code 
L = MyList([1, 2, 3, 4])

print("Original List")
print(L)

# Inserting to List" 
L.append(5)
print("After Insertion")
print(L)

# Deleting From List 
L.remove()
```

### Usage

Execute your python script with the help of the CLI

```shell
$ python my_list.py
```

It will display the following result

```shell
Original List
[1, 2, 3, 4]
After Insertion
[1, 2, 3, 4, 5]
Traceback (most recent call last):
  File "my_list.py", line 33, in <module>
    L.remove() 
  File "my_list.py", line 8, in remove
    raise RuntimeError("Deletion not allowed") 
RuntimeError: Deletion not allowed
```

## References

- https://docs.python.org/3/library/collections.html
- https://www.geeksforgeeks.org/python-collections-module