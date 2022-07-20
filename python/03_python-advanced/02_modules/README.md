# Importation/Structuration de modules
## Definition
A module are used to organize code into files and folders.<br>
Basically a module is a .py file containing python code.

There can be 3 kinds of modules:
 - system packages
 - third party packages
 - owned packages

As any python fie, a module may contain any definition such as:
 - functions
 - classes
 - variables

## Syntax
```python
# Import module called "my_module"
import my_module 

# Uses a function from "my_module"
my_module.say_hello()
```

## Syntax 
Importing a module makes all the definitions available from the source (where import is done).<br>
The default namespace is the name of the module.

```python
import my_module 
my_module.say_hello()
```

but you can create an alias for better code understanding.
```python
import my_module as m
m.say_hello()
```

You can also choose to import only a subset of a module
```python
import my_module.say_hello as m
m.say_hello()
```
in that case, all other definitions from the module are ignored.

## Standards modules
Standards module are available by default from python installation. They are core packages installed by default.<br>
Some commons modules are:
 - <span style="color: #dc1a1a;background-color: #f9f2f4;">datetime</span> for date and time functions
 - <span style="color: #dc1a1a;background-color: #f9f2f4;">math</span> for... hu, obvious ?
 - <span style="color: #dc1a1a;background-color: #f9f2f4;">os</span> for operating system functions such as file, path, env, ...
 - <span style="color: #dc1a1a;background-color: #f9f2f4;">re</span> for regexp
 - <span style="color: #dc1a1a;background-color: #f9f2f4;">urllib</span> for url functions
All these packages are listed in [official site standard library](https://docs.python.org/3/library/index.html)

## How does it works ?
### Path resolution
When you use import statement, the python interpreter will try to find a .py file using the following strategy:
 1. current folder
 2. PYTHONPATH
 3. default lib folder (like /usr/local/lib/python/)

### Directories and files
To group modules you can use a packet.
Most of the time packet are folders with a file by module
```python
import avionincs.tools.say_hello as m
m.say_hello()
```


## Tricks
List definitions inside a module 

```python
import os
dir (os)
```


