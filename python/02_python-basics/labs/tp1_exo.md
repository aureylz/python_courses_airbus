# Python basics - Hands on

Excercises can be made directly in the REPL.  

```python3
>>> print("Starting exercices...")
```

## PART 1 - Presentation

### 1.1 Who are you? (var and str)

- 1.1.1 Write your ```name``` in a variable (string)
- 1.1.2 Write ```age``` in an other variable (int)
- 1.1.3 Convert your age to a string
  - Convert it to a float.  
  - Convert to hexadecimal number.  
  - Rest int value.  
- 1.1.4 Create a boolean ```python_xp``` variable to express whether you have already coded with python or not
- 1.1.5 Set ```level``` to "I'm a beginner" or "I already have some experience"  using ```python_xp``` (one line code)
- 1.1.6 Display length of your name
- 1.1.7 Display first and last letter of you name
- 1.1.8 Check if your firstname ends with a vowel
- 1.1.9 Set ```presentation``` variable following this pattern: "My name is Micael, I'm 40 years old and I already have some experience in Python"

### 1.2 Names from Lilianna (str methods)

Consider firstname: 'Lilianna'

- 1.2.1 Convert ```name```'s content to upper case
- 1.2.2 Does it contain 'Anna'? (not case sensitive)
  - Give postion where we can find 'anna' in the name
- 1.2.3 Convert ```name```'s content into lower case
  - How many times we can find 'li' in the name
  - What's the index of 'li' found in the name
- 1.2.4 Extract first half of the name (that is 'Lili'), convert the result to capital case using string methods. _Tip_: look for strip method
  - Do the same, but with the second part ('anna')
- 1.2.5 Extract the letters whose index is an even number (result == 'llan') in the variable ```name```. _Tip_: use string[ start: end: step]

### 1.3 Leap year (operators)

- 1.3.1 Compute if current year is a leap year?  (can be divided by 4 but not 100 or by 400)
  - Try the same with 1904
- 1.3.2 Build a sequence of leap years (from year 1904 to now)
- 1.3.3 Use previous sequence to check if current year is a leap year
- 1.3.4 Display last leap year from sequence
- 1.3.5 Use a slice to display one leap year over 3 from leap sequence (1904, 1916, ... 2012)
