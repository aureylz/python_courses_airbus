# Python Basics Part 2

- [Python Basics Part 2](#python-basics-part-2)
  - [Flow control](#flow-control)
    - [Conditionals](#conditionals)
      - [```if``` .. ```elif``` .. ```else```](#if--elif--else)
    - [Loops](#loops)
      - [for](#for)
      - [while](#while)
    - [Exceptions handling](#exceptions-handling)
  - [Functions](#functions)
    - [Positional arguments](#positional-arguments)
    - [Named (keyword) arguments](#named-keyword-arguments)
    - [Using both positional and keyword arguments](#using-both-positional-and-keyword-arguments)
  - [Type hints](#type-hints)
    - [Examples](#examples)
  - [Entry point](#entry-point)

---

## Flow control

---

### Conditionals

---

Conditions can be used to execute a block of code if and only if some criterias are met.

Criterias are evaluated at run-time and based on your code's variables content.

---

Uncomment the first line, run the sample.
Then uncomment the second line only, and run the sample again.

```python
# my_var: float = 3.15
# my_var: float = 3.1415926

if my_var == 3.1415926:
    print('I recognized Pi')
```

---

Conditions also can be nested (indented).

There is no ```select...case``` construct in Python, just use ```if``` .. ```elif```

---

#### ```if``` .. ```elif``` .. ```else```

---

```python
catalog_item = 'A220'
is_military = False
is_aircraft = None
is_single_aisle = None
is_wide_body = None
is_helicopter = None
is_cargo = False
if catalog_item.upper().startwith('A'):
    is_helicopter = False
    is_aircraft = True
    if catalog_item in ('A220', 'A319', 'A320', 'A321'):
        is_single_aisle = True
        is_wide_body = False
    elif catalog_item in ('A330', 'A350'):
        is_single_aisle = True
        is_wide_body = False
    if catalog_item == 'A350F':
        is_cargo = True
    if catalog_item == 'A400M':
        is_cargo = True
        is_military = True
elif catalog_item.upper().startwith('H'):
    pass
else:
    raise KeyError(f'{catalog_item} does not belong to our catalog')
```

---

### Loops

Loops are used to repeat a block of code a certain amount of times.

The amount of iterations can be the number of items in a list or based on some criterias.

The ```continue``` keyword can be used to skip a specific iteration and is usually used within an ```if ... else``` construct.

---

#### for

```python
# loop over simple collections
for i in ['a', 'b', 'c']:
    for j in range(3):
        print(i+str(j), end=" ")
    print()

# loop over dictionary
cities={'TLS':'Toulouse', 'NYC': 'New York'}
for code in cities:
    print(code, ' : ', cities[code])

---

# continue keyword (also work with while loops)
for x in range(-10, 10):
    if x == 0:
        # the continue statement will skip the current block of code and keep looping
        continue
    print(f'y({x}) = 1/{x} = {1/x}')
```

---

#### while

```python
while True:
    s=input()
    if(s=='end'):
        break
```

---

### Exceptions handling

```python
try:
    raise ValueError('custom error')    # execution will raise an error
    print('wont be executed')
except(ValueError) as e:                # catch the error
    print('catch error:', e)
finally:                                # block executed after
    print('always executed at the end')
```

---

## Functions

A function is block of code that is executed when called. 

It is convenient to organize and reuse your code.

A function accepts parameters and can return a result.  

```python
def square(x):
    return x * x

square(3)
```

---

### Positional arguments

A function can accept several parameters and identify them according to their order.  

```python
def sum(x, y):
    return x + y

sum(4,5)
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

sum(1,2,3,4,5)
```

---

### Named (keyword) arguments

You can use the unpacking operator ```**``` for named (keywords arguments).

```python
def my_catalog(p1: str, p2: int, **kwargs):
    print(p1, p2)
    for key, value in kwargs.items():
        print(key, '-', value)

my_catalog(p1 = 'A220', p2 = 'A319', p3 = 'A320', p4 = 'A321')
```

---

### Using both positional and keyword arguments

```python
def my_catalog_2(*args, **kwargs):
    print(args)
    print(kwargs)

my_catalog_2("A320", "A400M", a = 319, b = 320, c = 321)
```

---

## Type hints

See also [official doc](https://docs.python.org/3/library/typing.html) and [PEP 483](https://peps.python.org/pep-0483/).

Type hints are optional annotations that one can add to the source code in order to be more explicit.

The intent is to help the programmer / readers of the code to better understand the expected and returned data-types in functions and variables.

---

> The Python runtime does not enforce function and variable type annotations. They can be used by third party tools such as type checkers, IDEs, linters, etc.
> Python ```linters``` are typically leveraging the ```type hints``` to issue warnings and point-out potential pitfalls in your code.

---

### Examples

Let's define a function without typings:

```python
def append_pi(lst):
    lst += [3.14]
```

---

The same function, but with typing annotations:

```python
def append_pi(lst: List[float]) -> None:
    lst += [3.14]
```

---

In the second version, at first read, one can clearly says:

- this functions expects a list of floats
- this function returns nothing, but has a side effect on the passed-in parameter

---

## Entry point

Python uses some special variables and functions that are being assigned depending on the execution context.

Those variables and functions are easy to identify, they're all wrapped within double underscores (```__```)

---

When the interpreter runs a module, it'll set the ```__name__``` to the name of the Python file or to ```__main__``` if this file is the main program entry point.

One can leverage that to run some part of the code when the file is the entry point only.

---

The following construct allows us to run code when we directly execute this file, but not when it's being imported as a module:

 ```python
# my_module.py
def unit_tests():
    # here go some unit tests
    ...

def my_module_func_1()
    # sample function that will be availabe once this module is imported
    ...

## this block will be executed if and only if one directly called the module from the command line (python 3 my_module.py)
## but it will not run when one uses this file as a module from another python file (import my_module.py)
if __name__ == "__main__":
   unit_tests
 ```

---
