# PART 1 - Presentation

# 1.1 Who are you?

# 1.1.1
name = "Micael"

# 1.1.2
age = 40

# 1.1.3
age = str(age)
print(age, type(age))

age = float(age)
print(age, type(age))

age = hex(int(age))
print(age, type(age))

age = int(age, 16)
print(age, type(age))

# 1.1.4
python_xp = True

# 1.1.5
level = "I already have some experience" if python_xp else "I'm a beginner"

# 1.1.6
len(name)

# 1.1.7
print(name[0])
print(name[len(name) - 1])
# This also returns the last letter
print(name[-1])

# 1.1.8
print(name.endswith(("a", "e", "i", "o", "u", "y")))

# 1.1.9
presentation = f"My name is {name}, I'm {age} years old and {level} in Python"
# or "My name is {0} I'm {1} years old and {2} in Python".format(name,age,level)
# == "My name is {} I'm {} years old and {} in Python".format(name,age,level)
# == "My name is {n} I'm {a} years old and {l} in Python".format(n=name,a=age,l=level)
print(presentation)

# 1.2  Names from Lilianna

# 1.2.1
name = "Lilianna".upper()

# 1.2.2
found = "anna" in name.lower()  # preferred way if you don't need position
position = name.lower().find("anna")  # or name.lower().index('anna')

# 1.2.3
name = name.lower()
print(name.count("li"))
print(name.find("li"))  # first position of substring

# 1.2.4
print(name.rstrip("an").capitalize())
print(name.lstrip("li").capitalize())

# 1.2.5
print(name[::2])

# 1.3 Leap year

# 1.3.1
year = 2022
is_leap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
year = 1900
is_leap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
# 1.3.2
leap_years = range(1904, 2022, 4)

# 1.3.3
print(f"Is 2022 a leap year? {2022 in leap_years}")

# 1.3.4
leap_years[-1]

# 1.3.5 a
third = slice(0, len(leap_years), 3)
list(leap_years[third])

# 1.3.5 b
list(leap_years)[0:-1:3]
