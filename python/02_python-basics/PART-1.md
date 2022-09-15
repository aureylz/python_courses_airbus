# Python Basics Part 1

- [Python Basics Part 1](#python-basics-part-1)
  - [Getting started](#getting-started)
    - [Basic testing](#basic-testing)
  - [Syntax](#syntax)
    - [Indentation](#indentation)
    - [Comments](#comments)
    - [Variables](#variables)
      - [Conditional assignment](#conditional-assignment)
    - [namingconvention.org](#namingconventionorg)
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
  - [Built-in functions](#built-in-functions)
  - [Operators](#operators)
    - [Arithmetic operators](#arithmetic-operators)
    - [Assignment operators](#assignment-operators)
    - [Comparison operators](#comparison-operators)
    - [Logical operators](#logical-operators)
    - [Identity operators](#identity-operators)
    - [Membership operators](#membership-operators)
    - [Bitwise operators](#bitwise-operators)

---

## Getting started

---

### Basic testing

We will see in this module some basics of python language.

You can use python interpreter also called REPL (Read Evaluate Print Loop), to check code snippets given in the module.  

---


```bash
/usr/local/bin/python3
>>> x = 'you'
>>> print('hello '+x)

hello you
```

> Use "ctrl + z" (Windows) or "ctrl + d" (Linux/ Mac) to quit REPL.

---

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

---

### Comments

```python
# start a line with the dash (#) sign to create a 'line comment'
"""
One can also use multiline string without assigning it to a variable.
This is an alternative as there's no multi-lines comments symbols in python
"""
vrai = True  # I could also be True (<- comments can be appened after code)
```

---

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

---

#### Conditional assignment

```python
my_var = 7
even = True if my_var % 2 == 0 else False 
# even == True

my_word='blue'
color = True if my_word in ('red', 'blue', 'yellow') else None  
# color == True
```

---

### [namingconvention.org](https://namingconvention.org/python/)

| Type       | Public              | Internal             |
| ---------- | ------------------- | -------------------- |
| Packages   | ```low_w_under```   |                      |
| Modules    | ```low_w_under```   | ```_low_w_under```   |
| Classes    | ```CapWords```      | ```_CapWords```      |
| Exceptions | ```CapWords```      |                      |
| Functions  | ```low_w_under()``` | ```_low_w_under()``` |

---

| Type         | Public              | Internal            |
| ------------ | ------------------- | ------------------- |
| Const        | ```CAPS_WI_UNDER``` | ```_CAPS_W_UNDER``` |
| Var          | ```low_w_under```   | ```low_w_under```   |
| Method Names | ```low_w_under()``` | ```low_w_under()``` |
| FParameters  | ```low_w_under```   |                     |

---

## Built-in data types

---

### ```None```

```python
x = None
```

---

### String

No ```char``` type in python, only ```str```, but individual characters can be accessed with the ```[]```operator.

---

```python
"I'm a string"
'And this is another string'
str(10) == str('10')
r'hello\nyou'    # 'hello\\nyou'  (raw)

len('azerty')    # 6
'azerty'[0]      # 'a'
```

---

#### String formating

Python 3.7 introduced the concept of f-string which is a nicer syntax compared to the former ```.format() ``` approach:

---

```python
model = 'A220'
category = 'Single Aisle'
msg = f"Our {model} is a {category}"
```

Here, in the string ```msg``` the ```model``` and ```category``` variables will be replaced by their content.

Output:

```bash
Our A220 is a Single Aisle
```

---

#### Common ```str``` operations

Extract from the official [docs.python.org](https://docs.python.org/3.7/library/stdtypes.html#string-methods):

---

[str.encode(encoding="utf-8", errors="strict")](https://docs.python.org/3.7/library/stdtypes.html#str.encode):

Return an encoded version of the string as a bytes object

---

[str.endswith(suffix\[, start\[, end\]\])](https://docs.python.org/3.7/library/stdtypes.html#str.endswith):

Return True if the string ends with the specified suffix, otherwise return False

---

[str.find(sub\[, start\[, end\]\])](https://docs.python.org/3.7/library/stdtypes.html#str.find):

Return the lowest index in the string where substring sub is found within the slice s[start:end]. The find() method should be used only if you need to know the position of sub. Otherwise, use the ```in``` operator:

```python
if 'Py' in 'Python'
```

---

[str.index(sub\[, start\[, end\]\])](https://docs.python.org/3.7/library/stdtypes.html#str.index):

Like find(), but raise ValueError when the substring is not found

---

- [str.join(iterable)](https://docs.python.org/3.7/library/stdtypes.html#str.join): 
  - Return a string which is the concatenation of the strings in iterable. The separator between elements is the string providing this method.

---

[str.replace(old, new\[, count\])](https://docs.python.org/3.7/library/stdtypes.html#str.replace):

Return a copy of the string with all occurrences of substring old replaced by new.

---

[str.startswith(prefix\[, start\[, end\]\])](https://docs.python.org/3.7/library/stdtypes.html#str.startswith): 

Return True if string starts with the prefix, otherwise return False.

---

### Numerical

---

#### ```int```

```python
x = 1
y = 320
z = -2
x = int(320)
```

---

#### ```float```

```python
x = 35e3
y = 12E4
z = -87.7e100
pi = float(3.1415926)
```

---

#### ```complex```

```python
x = 3+5j
y = 5j
z = -5j
x = complex(1j)
```

---

### Sequences

---

#### ```list```

Collection of ordered and indexed items.  

```python
aircrafts = list(("A320", "A330", "A350")) 
# ['A320', 'A330', 'A350']
```

---

##### ```list``` comprehension

Concise syntax to build lists (equivalent to a ```for``` loop).  

```python
words = ["tree", "flower", "bee"]
numbers = [len(word) for word in words] # [4, 6, 3]
```

---

#### ```tuple```

Immutable sequences of ordered and indexed items.  

```python
helicopters = tuple(("H160", "H175")) # ('H160', 'H175')
```

---

#### ```range```

Sequence representing an arithmetic progression of integers.  

```python
x = range(6) 
list(x) # [0, 1, 2, 3, 4, 5]
```

---

### Dictionaries

```dict```: collection of ordered (since python 3.7) and unique items (key-value pairs).  

```python
aircrafts_types = dict(name='A320', age='single_aisle') 
# {'name': 'A320', 'age': 'single_aisle'}
aircrafts_types.keys()
aircrafts_types.values()
aircrafts_types.items()
```

---

#### ```dict``` comprehension

Concise syntax to build dictionaries (equivalent to a ```for``` loop).  

```python
cities = {'paris':'france', 'madrid':'spain', 'hamburg':'germany'}
countries = {c:city for city,c in cities.items()}    
# {'france': 'paris', 'spain': 'madrid', 'germany': 'hamburg'}
```

---

### Sets

Unordered collection of unique (and unindexed) elements.  

---

#### ```set```

```python
single_aisle = set(("A319", "A320", "A321")) 
# {'A321', 'A320', 'A319'}
wide_bodies = set(("A330", "A350", "A380")) 
# {'A380', 'A330', 'A350'}
```

---

#### ```frozenset```

```python
oldies = frozenset(("concorde", "caravel", "a300"))
```

---

#### ```bool```

Almost any value is evaluated to True if it has some sort of content.

Any string is True, except empty strings.  
Any number is True, except 0.  
Any list, tuple, set, and dictionary are True, except empty ones.

---

```python
# Values evaluated to True:
bool(True) == bool(5) == bool("hello") == bool ([1,2,3])
# Values evaluated to False:
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
```

---

### Binary

---

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

---

## Built-in functions

[Official documentation](https://docs.python.org/3/library/functions.html)

---

[enumerate(iterable, start=0)](https://docs.python.org/3/library/functions.html#enumerate): 

returns a tuple containing a count (from start which defaults to 0) and the values obtained from iterating over iterable.

```python
for idx, value in enumerate(['A', 'B', 'C']):
    print(idx, value)
```
```bash
# Result:
0 A  
1 B  
2 C
```
---

[input([prompt])](https://docs.python.org/3/library/functions.html#input): 

If the prompt argument is present, it is written to standard output without a trailing newline. The function then reads a line from input

```python
name = input("What's your name: ")
```

---

[len(s)](https://docs.python.org/3/library/functions.html#len): 

Return the length (the number of items) of an object. The argument may be a sequence (such as a string, bytes, tuple, list, or range) or a collection (such as a dictionary, set, or frozen set)

```python
len([1, 2, 3])
```
```bash
# Result:
3
```

---

[open(file, mode='r', buffering=- 1, encoding=None, errors=None, newline=None, closefd=True, opener=None)](https://docs.python.org/3/library/functions.html#open): 

Open file and return a corresponding file object.

Cf PART-3 > Files I/O

---

[print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)](https://docs.python.org/3/library/functions.html#print): 

Print objects to the text stream file, separated by sep and followed by end. sep, end, file, and flush, if present, must be given as keyword arguments.

```python
name = "John"
print("Hello ", name)
```
```bash
# Result:
Hello John
```

---

[zip(*iterables, strict=False)](https://docs.python.org/3/library/functions.html#zip):

Iterate over several iterables in parallel, producing tuples with an item from each one.

```python
tuples = zip( ['A','B','C'], [1,2,3] )
print(list(tuples))
```
```bash
# Result:
[('A', 1), ('B', 2), ('C', 3)]
```

---

[slice(start, stop[, step])](https://docs.python.org/3/library/functions.html#slice): 

Return a slice object representing the set of indices specified by range(start, stop, step). Use slice to get a portion of an iterable.

```python
pair = slice(1, 10, 2)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10][pair]
```
```bash
# Result:
[2, 4, 6, 8, 10]
```

---

## Operators

---

### Arithmetic operators

| Operator | Name           | Example      |
| :------: | -------------- | ------------ |
| ```+```  | Addition       | ```x + y```  |
| ```-```  | Subtraction    | ```x - y```  |
| ```*```  | Multiplication | ```x * y```  |
| ```/```  | Division       | ```x / y```  |
| ```%```  | Modulus        | ```x % y```  |
| ```**``` | Exponentiation | ```x ** y``` |
| ```//``` | Floor division | ```x // y``` |

---

### Assignment operators

| Operator | Example      | Same as         |
| :------: | ------------ | --------------- |
| ```=```  | ```x = 5```  | ```x = 5```     |
| ```+=``` | ```x += 3``` | ```x = x + 3``` |
| ```-=``` | ```x -= 3``` | ```x = x - 3``` |
| ```*=``` | ```x *= 3``` | ```x = x * 3``` |
| ```/=``` | ```x /= 3``` | ```x = x / 3``` |
| ```%=``` | ```x %= 3``` | ```x = x % 3``` |

---

| Operator  | Example       | Same as          |
| :-------: | ------------- | ---------------- |
| ```//=``` | ```x //= 3``` | ```x = x // 3``` |
| ```**=``` | ```x **= 3``` | ```x = x ** 3``` |
| ```&=```  | ```x &= 3```  | ```x = x & 3```  |
| ```\|=``` | ```x \|= 3``` | ```x = x \| 3``` |
| ```^=```  | ```x ^= 3```  | ```x = x ^ 3```  |
| ```>>=``` | ```x >>= 3``` | ```x = x >> 3``` |
| ```<<=``` | ```x <<= 3``` | ```x = x << 3``` |

---

### Comparison operators

| Operator | Name                     | Example      |
| :------: | ------------------------ | ------------ |
| ```==``` | Equal                    | ```x == y``` |
| ```!=``` | Not equal                | ```x != y``` |
| ```>```  | Greater than             | ```x > y```  |
| ```<```  | Less than                | ```x < y```  |
| ```>=``` | Greater than or equal to | ```x >= y``` |
| ```<=``` | Less than or equal to    | ```x <= y``` |

---

### Logical operators

| Operator  | Name                                                    | Example                     |
| :-------: | ------------------------------------------------------- | --------------------------- |
| ```and``` | Returns True if both statements are true                | ```x < 5 and  x < 10```     |
| ```or```  | Returns True if one of the statements is true           | ```x < 5 or x < 4```        |
| ```not``` | Reverse the result, returns False if the result is true | ```not(x < 5 and x < 10)``` |

---

### Identity operators

|   Operator   | Name                                                   | Example          |
| :----------: | ------------------------------------------------------ | ---------------- |
|   ```is```   | Returns True if both variables are the same object     | ```x is y```     |
| ```is not``` | Returns True if both variables are not the same object | ```x is not y``` |

---

### Membership operators

|   Operator   | Name                                                                             | Example          |
| :----------: | -------------------------------------------------------------------------------- | ---------------- |
|   ```in```   | Returns True if a sequence with the specified value is present in the object     | ```x in y```     |
| ```not in``` | Returns True if a sequence with the specified value is not present in the object | ```x not in y``` |

---

### Bitwise operators

| Operator | Name     | Example                                         |
| :------: | -------- | ----------------------------------------------- |
| ```+```  | Addition | ```x + y```                                     |
| ```&```  | AND      | Sets each bit to 1 if both bits are 1           |
| ```\|``` | OR       | Sets each bit to 1 if one of two bits is 1      |
| ```^```  | XOR      | Sets each bit to 1 if only one of two bits is 1 |

---

| Operator | Name                 | Example                                                                                                 |
| :------: | -------------------- | ------------------------------------------------------------------------------------------------------- |
| ```~```  | NOT                  | Inverts all the bits                                                                                    |
| ```<<``` | Zero fill left shift | Shift left by pushing zeros in from the right and let the leftmost bits fall off                        |
| ```>>``` | Signed right shift   | Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off |

