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
    - [Variable named (keyword) arguments](#variable-named-keyword-arguments)
    - [Both positional and names parameters](#both-positional-and-names-parameters)

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

```python
def square(x):
    return x * x

square(3)
```

---

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

---

### Both positional and names parameters

```python
def my_catalog_2(*args, **kwargs):
    print(args)
    print(kwargs)

if __name__ == "__main__":
    myFunction("A320", "A400M", a = 319, b = 320, c = 321)
```

---