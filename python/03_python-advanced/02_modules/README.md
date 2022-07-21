# Importation/Structuration de modules
🕑 1h

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

## Hands-on
Using your favorite IDE
### step1 - Define a package "greetings" with to functions:
 1. ```say_hello()```
 2. ```say_something(text)```

### step2 - Use this module from the main file
 1. create ```main.py``` file
 2. call ```say_hello()``` function
 3. call ```say_something("World")``` function

### step3 - Use alias
Use an alias in order to be able to call the functions like this:
```python
g.say_something("Hello World")
```

### step4 - Make the module "runnable"
Add the following code to the greeting package
```python
if __name__ == "__main__":
     say_something("Hello from Greeting modeule module")
```

Launch
```python
python3 greetings.py
python3 main.py
```

❓What are the differences ? <br>
❓How do you explain the different behaviours ? 

### step5 - For the braves 💪
1. Create a module called ```sys```
2. Create a function ```getprofile```. This function should return a constant of your choice.
3. Create a function ```gettemperature```. This function should return "100 degrees".
4. Import your ```sys``` module from ```main.py```
5. Call ```print(sys.gettemperature())```
6. Call ```print(sys.getprofile())```

❓ What happens ? <br>
❓ Why ? 


## Tricks
List definitions inside a module 

```python
import os
dir (os)
```


