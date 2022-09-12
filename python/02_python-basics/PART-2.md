# Python Basics Part 2

- [Python Basics Part 2](#python-basics-part-2)
  - [Flow control](#flow-control)
    - [Conditionals](#conditionals)
      - [```if``` .. ```elif``` .. ```else```](#if--elif--else)
    - [Loops](#loops)
      - [for](#for)
      - [while](#while)
    - [Exceptions](#exceptions)
      - [Examples](#examples)
      - [Handle exceptions](#handle-exceptions)
      - [Raise exception](#raise-exception)
  - [Functions](#functions)
    - [Positional arguments](#positional-arguments)
    - [Named (keyword) arguments](#named-keyword-arguments)
    - [Using both positional and keyword arguments](#using-both-positional-and-keyword-arguments)
    - [Type hints](#type-hints)
      - [Examples](#examples-1)
    - [Entry point](#entry-point)

---

## Flow control

---

### Conditionals

---

Conditions can be used to execute a block of code if and only if some criterias are met.

Criterias are evaluated at run-time and based on your code's variables content.

---

```python
my_var: float = 3.15
if my_var == 3.1415926:
    print('I recognized Pi')

# Result?


my_var: float = 3.1415926
if my_var == 3.1415926:
    print('I recognized Pi')

# Result ?

```

---

Conditions also can be nested (indented).

There is no ```select...case``` construct in Python, just use ```if``` .. ```elif```

---

#### ```if``` .. ```elif``` .. ```else```

---

```python
catalog_item = 'A220'
is_aircraft = False
is_single_aisle = False
is_cargo = False
```
```python
if catalog_item.upper().startswith('A'):
    is_aircraft = True; 
    if catalog_item in ('A220', 'A319', 'A320', 'A321'):
        is_single_aisle = True
    elif catalog_item in ('A330', 'A350'):
        is_single_aisle = True
    if catalog_item == 'A350F':
        is_cargo = True
elif catalog_item.upper().startswith('H'):
    pass # does nothing
else:
    raise KeyError(f'{catalog_item} does not belong to our catalog')
```
```python
print(f"\ncatalog_item:{catalog_item} aircraft?{is_aircraft}")
print(f"\nsingle aisle?{is_single_aisle} cargo?{is_cargo}")
```

```bash
# Result
catalog_item:A220 aircraft?True
single aisle? cargo?False
```

---

### Loops

Loops are used to repeat a block of code a certain amount of times.

The amount of iterations can be the number of items in a list or based on some criterias.

The ```continue``` keyword can be used to skip a specific iteration and is usually used within an ```if ... else``` construct.

---

#### for

Loop over a collection

```python
for i in ['a', 'b', 'c']:
    print(i)
```
```bash
# Result 
a
b
c
```

---

Nested loops

```python
for i in ['a', 'b', 'c']:
    for j in range(3):
        print(i+str(j), end=" ")
    print()
```
```bash
# Result 
a0 a1 a2 
b0 b1 b2 
c0 c1 c2 
```

---

Loop over dictionary

```python
cities={'TLS':'Toulouse', 'NYC': 'New York'}
for code in cities:
    print(code, ' : ', cities[code])
```
```bash
# Result 
TLS  :  Toulouse
NYC  :  New York
```

---

`continue` keyword (also works with while loops)

```python
for x in range(-10, 10):
    if x == 0:
        # skip the current block of code and keep looping
        # thus print line is not executed if x == 0
        continue
    print(f'y({x}) = 1/{x} = {1/x}')
```
```bash
# Result 
y(-10) = 1/-10 = -0.1
y(-9) = 1/-9 = -0.111111111111111
...
```
---

#### while

Execute statements until a condition is satisfied.

```python
res=''
while True:
    s=input('enter some text:')
    if(s=='end'):
        break
    else:
        res+=s
```

---

### Exceptions 

Even if the syntax of your code is correct errors can happen at execution time.  

An exception raised and not handled terminates abruptly the program.  

---

#### Examples

```python
>>> 10/0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero

>>> x = int("string")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'string'

>>> print(not_defined_here)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'not_defined_here' is not defined
```

---

#### Handle exceptions

> try ... except ... [else ...] [finally ...]

```python
try:
    x = int("not_an_int")   # exception generated
except ValueError as err:   # exception catched
    print(err)  # executed in this case
except BaseException as err:
    # would be executed if type of exception was not ValueError
    print(f"Unexpected {type(err)}") 
else:
    # would be executed if valid int is used, eg: x = int(1)
    print(f"result is: {x}") 
finally:
    print("Operation done") # always executed
```
```bash
# Result
invalid literal for int() with base 10: 'not_an_int'
Operation done
```

---

#### Raise exception

You can raise your custom exception.

```python
try:
    raise ValueError('custom error')    # raise an error
    print('wont be executed')
except(ValueError) as e:                # catch the error
    print('catch error:', e)
finally:                                # executed at the end
    print('clean up')
```
```bash
# Result
catch error: custom error
clean up
```
---

## Functions

A function is a block of code that is executed when called. 

It is convenient to organize and reuse your code.

A function accepts parameters and can return a result.  

```python
def square(x):
    return x * x

square(3) # 9
```

---

### Positional arguments

A function can accept several parameters and identify them according to their order.  

```python
def sum(x, y):
    return x + y

sum(4,5)  # 9
```

---

Python allows to pass a varying number of parameters, without using a list.

To do so use the unpacking operator ```*```.

```python
def sum(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

sum(1,2,3,4,5)  # 15
```

---

### Named (keyword) arguments

```python
def sum(x, y):
    return x + y

sum(x=4, y=5)  # 9
```

You can use the unpacking operator ```**``` for named (keywords arguments).

```python
def my_catalog(p1: str, p2: int, **kwargs):
    print(p1, p2)
    for key, value in kwargs.items():
        print(key, '-', value)

my_catalog(p1 = 'A220', p2 = 'A319', p3 = 'A320', p4 = 'A321')
```
```bash
# Result
A220 A319
p3 - A320
p4 - A321
```
---

### Using both positional and keyword arguments

```python
def my_catalog_2(*args, **kwargs):
    print(args)
    print(kwargs)

my_catalog_2("A320", "A400M", a = 319, b = 320, c = 321)
```
```bash
# Result
('A320', 'A400M')
{'a': 319, 'b': 320, 'c': 321}
```
---

### Type hints

See also [official doc](https://docs.python.org/3/library/typing.html) and [PEP 483](https://peps.python.org/pep-0483/).

Type hints are optional annotations that one can add to the source code in order to be more explicit.

The intent is to help the programmer / readers of the code to better understand the expected and returned data-types in functions and variables.

---

> The Python runtime does not enforce function and variable type annotations. They can be used by third party tools such as type checkers, IDEs, linters, etc.
> Python ```linters``` are typically leveraging the ```type hints``` to issue warnings and point-out potential pitfalls in your code.

---

#### Examples

Let's define a function without typings:

```python
l = [1,2]
def append_pi(lst):
    lst += [3.14]
```
```bash
>>> l
[1, 2, 3.14]
```
---

The same function, but with typing annotations:

```python
def append_pi(lst: list[float]) -> None:
    lst += [3.14]
```  

At first read, one can now clearly says:
- this functions expects a list of floats
- this function returns nothing, but has a side effect on the passed-in parameter

---

### Entry point

Python uses some special variables and functions that are being assigned depending on the execution context.

Those variables and functions are easy to identify, they're all wrapped within double underscores: ```__``` (```__var__``` is usually called "dunder var").

---

When the interpreter runs a module, it'll set the ```__name__``` to the name of the Python file or to ```__main__``` if this file is the main program entry point.

One can leverage that to run some part of the code when the file is the entry point only.

---

Example to run unit tests when file is executed from command line:

 ```python
# my_module.py

def unit_tests():
    # here go some unit tests
    ...

def my_module_func_1()
    # sample function availabe once this module is imported
    ...

# Code executed if script is called as main 
# but not if it is imported in a module
if __name__ == "__main__":
   unit_tests
 ```

> Last block above is executed if and only if one directly call the module from the command line  
> `python3 my_module.py`  
> but it is not run when one uses this file as a module from another python file  
> `import my_module.py`

---
