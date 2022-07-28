# Module 2: Python basics (5h30)

## Getting started

We will see in this modules some basics of python language.  
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

Python 3.7 introduced the concept of f-string which is a nicer syntax compared to the old ```.fmt() approach:

```python
model = 'A220'
category = 'Single Aisle'
msg = f"Our {model} is a {category}" 
```

Result:

=> Our ```A220``` is a ```Single Aisle```

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

## Comprehension

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

#### if .. elif .. else

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
