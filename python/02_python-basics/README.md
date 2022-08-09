# Module 2: Python basics (6h)

- [Module 2: Python basics (6h)](#module-2-python-basics-6h)
  - [Getting started](#getting-started)
  - [Syntax](#syntax)
    - [Indentation](#indentation)
    - [Comments](#comments)
    - [Variables](#variables)
      - [Conditional assignment](#conditional-assignment)
  - [Entry point](#entry-point)
  - [Built-in data types](#built-in-data-types)
    - [```None```](#none)
    - [String](#string)
      - [String formating](#string-formating)
      - [Common ```str``` operations](#common-str-operations)
    - [Numerical](#numerical)
      - [```int```](#int)
      - [```float```](#float)
      - [```complex```](#complex)
    - [Sequences](#sequences)
      - [```list```](#list)
        - [```list``` comprehension](#list-comprehension)
      - [```tuple```](#tuple)
      - [```range```](#range)
    - [Dictionaries](#dictionaries)
      - [```dict``` comprehension](#dict-comprehension)
    - [Sets](#sets)
      - [```set```](#set)
      - [```frozenset```](#frozenset)
      - [```bool```](#bool)
    - [Binary](#binary)
      - [```bytes```](#bytes)
      - [```bytearray```](#bytearray)
      - [```memoryview```](#memoryview)
  - [Operators](#operators)
    - [Arithmetic operators](#arithmetic-operators)
    - [Assignment operators](#assignment-operators)
    - [Comparison operators](#comparison-operators)
    - [Logical operators](#logical-operators)
    - [Identity operators](#identity-operators)
    - [Membership operators](#membership-operators)
    - [Bitwise operators](#bitwise-operators)
  - [Flow control](#flow-control)
    - [Conditionals](#conditionals)
      - [```if``` .. ```elif``` .. ```else```](#if--elif--else)
    - [Loops](#loops)
      - [for](#for)
      - [while](#while)
    - [Exceptions handling](#exceptions-handling)
  - [Functions](#functions)
    - [Variable named (keyword) arguments](#variable-named-keyword-arguments)
    - [Both positional and names parameters](#both-positional-and-names-parameters)
  - [Files I/O](#files-io)
  - [Parsing](#parsing)
    - [JSON](#json)
    - [CSV](#csv)
  - [Unit tests](#unit-tests)

## Getting started

We will see in this module some basics of python language.

You can use python interpreter also called REPL (Read Evaluate Print Loop), to check code snippets given in the module.  

Note: "ctrl + d" to quit REPL.

```bash
/usr/local/bin/python3
>>> x = 'you'
>>> print('hello '+x)
```

## Syntax

### Indentation

Used so that Python can infer your code structure / skeleton.

```python
if True:
    # do that n times
    for i in range(5):
        print(f'Hello World {i}')
else:
    # this never happens

```

### Comments

```python
# start a line with the dash (#) sign to create a 'line comment'
"""
One can also use multiline string without assigning it to a variable.
This is an alternative as there's no multi-lines comments symbols in python
"""
vrai = True  # I could also be True (<- comments can be appened after code)
```

### Variables

Created when you assign a value to it.

Are case sensitive.

Are dynamically typed at runtime and can change type based on their content after they've been set.

```python
my_str = "Airbus Cyber Diploma"     # this is a string
my_pi = 3.1415926                   # float
vrai = True                         # boolean
my_pi = vrai                        # now my_pi is a boolean
```

#### Conditional assignment

```python
my_var = 7
even = True if my_var % 2 == 0 else False

my_word='blue'
color = my_word if my_word in ('red', 'blue', 'green', 'yellow', 'white', 'black') else None
```

## Entry point

Python uses some special variables and functions that are being assigned depending on the execution context.

Those variables and functions are easy to identify, they're all wrapped within double underscores (```__```)

When the interpreter runs a module, it'll set the ```__name__``` to the name of the Python file or to ```__main__`` if this file is the main program entry point.

One can leverage that to run some part of the code when the file is the entry point only.

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

## Built-in data types

### ```None```

```python
x = None
```

### String

No ```char``` type in python, only ```str```, but individual characters can be accessed with the ```[]```operator.

```python
"I'm a string"
'And this is another string'
str(10) == str('10')
r'hello\nyou'    # => 'hello\\nyou'  (raw)

len('azerty')    # == 6
'azerty'[0]      # == 'a'
```

#### String formating

Python 3.7 introduced the concept of f-string which is a nicer syntax compared to the former ```.format() ``` approach:

```python
model = 'A220'
category = 'Single Aisle'
msg = f"Our {model} is a {category}" 
```

Here, in the string ```msg``` the ```model``` and ```category``` variables will be replaced by their content.

Output:

=> Our ```A220``` is a ```Single Aisle```

#### Common ```str``` operations

Extract from the official [docs.python.org](https://docs.python.org/3.7/library/stdtypes.html#string-methods):

- [str.encode(encoding="utf-8", errors="strict")](https://docs.python.org/3.7/library/stdtypes.html#str.encode): Return an encoded version of the string as a bytes object

- [str.endswith(suffix[, start[, end]])](https://docs.python.org/3.7/library/stdtypes.html#str.endswith): Return True if the string ends with the specified suffix, otherwise return False

- [str.find(sub[, start[, end]])](https://docs.python.org/3.7/library/stdtypes.html#str.find): Return the lowest index in the string where substring sub is found within the slice s[start:end]. The find() method should be used only if you need to know the position of sub. Otherwise, use the ```in``` operator:
  > ```if 'Py' in 'Python'```

- [str.index(sub[, start[, end]])](https://docs.python.org/3.7/library/stdtypes.html#str.index): Like find(), but raise ValueError when the substring is not found

- [str.join(iterable)](https://docs.python.org/3.7/library/stdtypes.html#str.join): Return a string which is the concatenation of the strings in iterable. The separator between elements is the string providing this method.

- [str.replace(old, new[, count])](https://docs.python.org/3.7/library/stdtypes.html#str.replace): Return a copy of the string with all occurrences of substring old replaced by new.

- [str.startswith(prefix[, start[, end]])](https://docs.python.org/3.7/library/stdtypes.html#str.startswith): Return True if string starts with the prefix, otherwise return False.

### Numerical

#### ```int```

```python
x = 1
y = 320
z = -2
x = int(320)
```

#### ```float```

```python
x = 35e3
y = 12E4
z = -87.7e100
pi = float(3.1415926)
```

#### ```complex```

```python
x = 3+5j
y = 5j
z = -5j
x = complex(1j)
```

### Sequences

#### ```list```

Collection of ordered and indexed items.  

```python
aircrafts = list(("A320", "A330", "A350")) # ['A320', 'A330', 'A350']
```

##### ```list``` comprehension

Concise syntax to build lists (equivalent to a ```for``` loop).  

```python
words = ["tree", "flower", "bee"]
numbers = [len(word) for word in words] # [4, 6, 3]
```

#### ```tuple```

Immutable sequences of ordered and indexed items.  

```python
helicopters = tuple(("H160", "H175")) # ('H160', 'H175')
```

#### ```range```

Sequence representing an arithmetic progression of integers.  

```python
x = range(6) # list(x) => [0, 1, 2, 3, 4, 5]
```

### Dictionaries

```dict``` is collection of ordered (since python 3.7) and unique items (key-value pairs).  

```python
aircrafts_types = dict(name='A320', age='single_aisle') # {'name': 'A320', 'age': 'single_aisle'}
aircrafts_types.keys()
aircrafts_types.values()
aircrafts_types.items()
```

#### ```dict``` comprehension

Concise syntax to build dictionaries (equivalent to a ```for``` loop).  

```python
cities = {'paris':'france', 'madrid':'spain', 'hamburg':'germany'}
countries = {c:city for city,c in cities.items()}    # {'france': 'paris', 'spain': 'madrid', 'germany': 'hamburg'}
```

### Sets

Unordered collection of unique (and unindexed) elements.  

#### ```set```

```python
single_aisle = set(("A319", "A320", "A321")) # {'A321', 'A320', 'A319'}
wide_bodies = set(("A330", "A350", "A380")) # {'A380', 'A330', 'A350'}
```

#### ```frozenset```

```python
oldies = frozenset(("concorde", "caravel", "a300"))
```

#### ```bool```

Almost any value is evaluated to True if it has some sort of content.

Any string is True, except empty strings.  
Any number is True, except 0.  
Any list, tuple, set, and dictionary are True, except empty ones.

```python
bool(True) == bool(5) == bool("hello") == bool ([1,2,3])
# These are the list of values which evaluates to False
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
```

### Binary

#### ```bytes```

```python
x = bytes(5)
```

#### ```bytearray```

```python
x = bytearray(5)
```

#### ```memoryview```

```python
x = memoryview(bytes(5))
```

## Operators

> penser crypto avec div euclidienne, puissance, etc...

liste, dictionnaire, tuple,

### Arithmetic operators

| Operator | Name | Example |
|:-:|---|---|
| ```+``` | Addition | ```x + y``` |
| ```-``` | Subtraction | ```x - y``` |
| ```*``` | Multiplication | ```x * y``` |
| ```/``` | Division | ```x / y``` |
| ```%``` | Modulus | ```x % y``` |
| ```**``` | Exponentiation | ```x ** y``` |
| ```//``` | Floor division | ```x // y``` |

### Assignment operators

| Operator | Example | Same as |
|:-:|---|---|
| ```=``` | ```x = 5``` | ```x = 5``` |
| ```+=``` | ```x += 3``` | ```x = x + 3``` |
| ```-=``` | ```x -= 3``` | ```x = x - 3``` |
| ```*=``` | ```x *= 3``` | ```x = x * 3``` |
| ```/=``` | ```x /= 3``` | ```x = x / 3``` |
| ```%=``` | ```x %= 3``` | ```x = x % 3``` |
| ```//=```| ```x //= 3``` | ```x = x // 3``` |
| ```**=``` | ```x **= 3``` | ```x = x ** 3``` |
| ```&=``` | ```x &= 3``` | ```x = x & 3``` |
| ```\|=``` | ```x \|= 3``` | ```x = x \| 3``` |
| ```^=``` | ```x ^= 3``` | ```x = x ^ 3``` |
| ```>>=```  | ```x >>= 3``` | ```x = x >> 3``` |
| ```<<=```  | ```x <<= 3``` | ```x = x << 3``` |

### Comparison operators

| Operator | Name | Example |
|:-:|---|---|
| ```==``` | Equal | ```x == y``` |
| ```!=``` | Not equal | ```x != y``` |
| ```>``` | Greater than | ```x > y``` |
| ```<``` | Less than | ```x < y``` |
| ```>=``` | Greater than or equal to | ```x >= y``` |
| ```<=``` | Less than or equal to | ```x <= y``` |

### Logical operators

| Operator | Name | Example |
|:-:|---|---|
| ```and``` | Returns True if both statements are true | ```x < 5 and  x < 10``` |
| ```or``` | Returns True if one of the statements is true | ```x < 5 or x < 4``` |
| ```not``` | Reverse the result, returns False if the result is true | ```not(x < 5 and x < 10)``` |

### Identity operators

| Operator | Name | Example |
|:-:|---|---|
| ```is``` | Returns True if both variables are the same object | ```x is y``` |
| ```is not``` | Returns True if both variables are not the same object | ```x is not y``` |

### Membership operators

| Operator | Name | Example |
|:-:|---|---|
| ```in``` | Returns True if a sequence with the specified value is present in the object | ```x in y``` |
| ```not in``` | Returns True if a sequence with the specified value is not present in the object | ```x not in y``` |

### Bitwise operators

| Operator | Name | Example |
|:-:|---|---|
| ```+``` | Addition | ```x + y``` |
| ```&``` | AND | Sets each bit to 1 if both bits are 1 |
| ```\|``` | OR | Sets each bit to 1 if one of two bits is 1 |
| ```^``` | XOR | Sets each bit to 1 if only one of two bits is 1 |
| ```~``` | NOT | Inverts all the bits |
| ```<<``` | Zero fill left shift | Shift left by pushing zeros in from the right and let the leftmost bits fall off |
| ```>>``` | Signed right shift | Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off |

## Flow control

### Conditionals

Conditions can be used to execute a block of code if and only if some criterias are met.

Conditions can be nested (indented).

There is no ```select...case``` construct in Python, just use ```if``` .. ```elif```

#### ```if``` .. ```elif``` .. ```else```

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

### Loops

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


# continue keyword (also work with while loops)
for x in range(-10, 10):
    if x == 0:
        # the continue statement will skip the current block of code and keep looping
        continue
    print(f'y({x}) = 1/{x} = {1/x}')
```

#### while

```python
while True:
    s=input()
    if(s=='end'):
        break
```

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

## Functions

```python
def square(x):
    return x * x

square(3)
```

### Variable named (keyword) arguments

> Use the double asterisk ```**``` before kwargs as the unpacking operator

```python
def my_catalog(p1: str, p2: int, **kwargs):
    print(p1, p2)
    for key, value in kwargs.items():
        print(key, '-', value)

if __name__ == "__main__":
    myFunction(a = 'A220', b = 'A319', c = 'A320', d = 'A321')
```

### Both positional and names parameters

```python
def my_catalog_2(*args, **kwargs):
    print(args)
    print(kwargs)

if __name__ == "__main__":
    myFunction("A320", "A400M", a = 319, b = 320, c = 321)
```

## Files I/O

Write or read file with Python  

```python
f = open('python-test.txt', 'x') # x: create if not existing / a: append / w: overwrite
f.write("content file!")
f.write("\nnew line")

f=open('python-test.txt', 'r')  # read mode
f.read()        # read until the end
f.seek(0)       # point at the beginning
f.readline()    # read first line
f.close()
```

Using a with-block:  

```python
with open('python-test.txt') as f:
    f.read()
```

## Parsing

### JSON

Parse json string (to python dict).  

```python
import json
json_string = '{"PAR":"Paris", "MRS":"Marseille", "TLS":"Toulouse"}' # read string or file
json_dict = json.loads(json_string)
json_dict['MRS']
```

Convert python dict to json string.  

```python
import json
json_dict = {
    "PAR": "Paris", 
    "MRS": "Marseille", 
    "TLS": "Toulouse"
}
json_string = json.dumps(json_dict)
print(json_string)
```

### CSV

Write a csv file.  

```python
import csv
with open('cities.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['TLS','Toulouse'])
    writer.writerow(['MRS','Marseille'])
    writer.writerow(['PAR','Paris'])

# or with DictWriter
fieldnames = ['code', 'city']
with open('cities.csv', 'w', newline='') as csvfile:
    fieldnames = ['code', 'city']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'code': 'TLS', 'city': 'Toulouse'})
    writer.writerow({'code': 'MRS', 'city': 'Marseille'})
    writer.writerow({'code': 'PAR', 'city': 'Paris'})
```

Read csv file.

```python
import csv
with open('cities.csv', encoding="utf8") as f:
    reader = csv.reader(f)
    for line in reader:
        next(reader)    # return next line as a list
        print('|'.join(line))     # can also print(line[1])

# or with DictReader
fieldnames = ['code', 'city']
with open('cities.csv', encoding="utf8") as f:
    reader = csv.DictReader(f, fieldnames)
    next(reader)    # return next line as a dict
    for line in reader:
        print(f"code {line['code']} for city {line['city']}")
```

## Unit tests

```python
assert sum(range(5)) == 10                  # ok => no output
assert sum(range(5)) == 11, "Should be 10"  # ko => AssertionError: Should be 10
```

In a file (function + test):

```python
def square(x):
    return x**2

def test_square_5():
    assert square(5) == 25, "Should be 25"


def test_square_12():
    assert square(12) == 144, "Should be 144"


if __name__ == "__main__":
    test_square_5()
    test_square_12()
    print("OK all tests done")
```

Launch test:

```bash
python test_square.py
```

To write unit tests on your application choose a test runner: unittest, pytest, nose...
