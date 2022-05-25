# Module 2: Python basics

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
my_first_var = "I'm a string"
my_second_var = 'An this is another string'
my_pi = 3.1415926 # is a float
vrai = True
my_pi = vrai # now my_pi is a bool
```

#### Conditional assignment

```python
my_var = 7
even = True if my_var % 2 == 0 else False

my_word='blue'
color = my_word if my_word in ('red', 'blue', 'green', 'yellow', 'white', 'black') else None
```

## Built-in data types

### None

```python
x = None
```

### str

No char type in python

```python
x = str("Airbus Cyber Diploma")
print(x[2])  # = r
size = len('azerty') # = 6
```

### Numerical

#### int

```python
x = 1
y = 320
z = -2
x = int(320)
```

#### float

```python
x = 35e3
y = 12E4
z = -87.7e100
pi = float(3.1415926)
```

#### complex

```python
x = 3+5j
y = 5j
z = -5j
x = complex(1j)
```

### Sequences

#### list

```python
aircrafts = list(("A320", "A330", "A350"))
```

#### tuple

```python
helicopters = tuple(("H160", "H175"))
```

#### range

```python
x = range(6)
```

### dict

```python
aircrafts_types = dict(name='A320', age='single_aisle')
```

### Sets

#### set

```python
single_aisle = set(("A319", "A320", "A321"))
wide_bodies = set(("A330", "A350", "A380"))
```

#### frozenset

```python
oldies = frozenset(("concorde", "caravel", "a300"))
```

#### bool

Almost any value is evaluated to True if it has some sort of content.

Any string is True, except empty strings.

Any number is True, except 0.

Any list, tuple, set, and dictionary are True, except empty ones.

```python
x = bool(5)
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

#### bytes

```python
x = bytes(5)
```

#### bytearray

```python
x = bytearray(5)
```

#### memoryview

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

#### while

### Exceptions handling

## Functions

## Files I/O

## Parsing

> Beaucoup de parsing de format sur des notebook jupyter.

### JSON

### CSV

## Comprehension

### list

### dict

## Unit tests
