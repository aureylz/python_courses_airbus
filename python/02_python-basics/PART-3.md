# Python Basics Part 3

- [Python Basics Part 3](#python-basics-part-3)
  - [Files I/O](#files-io)
  - [Parsing](#parsing)
    - [JSON](#json)
  - [> json.loads to deserialize a string to a Python object](#-jsonloads-to-deserialize-a-string-to-a-python-object)
    - [CSV](#csv)
  - [Unit tests](#unit-tests)

---

## Files I/O

---

Write or read file with Python  

```python
 # x: create if not existing / a: append / w: overwrite
f = open('python-test.txt', 'x')
f.write("content file!")
f.write("\nnew line")

f=open('python-test.txt', 'r')  # read mode
f.read()        # read until the end
f.seek(0)       # point at the beginning
f.readline()    # read first line
f.close()
```

---

Using a with-block  
_=> standard way to read/ write in files_

```python
with open('python-test.txt') as f:
    f.read()
```
> Acts as a try/ catch and close resource at the end

---

## Parsing

---

### JSON

Parse json string (to python dict).  

```python
import json
# read string or file
json_string = '{"PAR":"Paris", "MRS":"Marseille", "TLS":"Toulouse"}'
json_dict = json.loads(json_string)
json_dict['MRS'] # Marseille
```
> json.loads to deserialize a string to a Python object
---

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
# {"PAR": "Paris", "MRS": "Marseille", "TLS": "Toulouse"}
```
> json.dumps to serialize an object as a json formatted `string`

---

Write a json file.

```python
import json
with open('cities.json', 'w') as jsonfile:
    json.dump({ "PAR": "Paris", "MRS": "Marseille",  "TLS": "Toulouse"}, jsonfile)
```
> json.dump to serialize an object as a json formatted `stream` into a file

---

Read a json file.

```python
import json
with open('cities.json', 'r') as jsonfile:
    cities_dict = json.load(jsonfile)
print(cities_dict)
```
> json.load to deserialize file content to a Python object 

### CSV

---

Write a csv file.  

```python
import csv
with open('cities.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['TLS','Toulouse'])
    writer.writerow(['MRS','Marseille'])
    writer.writerow(['PAR','Paris'])
```
```python
# or with DictWriter
fieldnames = ['code', 'city']
with open('cities.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames)
    writer.writeheader()
    writer.writerow({'code': 'TLS', 'city': 'Toulouse'})
    writer.writerow({'code': 'MRS', 'city': 'Marseille'})
    writer.writerow({'code': 'PAR', 'city': 'Paris'})
```

---

Read csv file.

```python
import csv
with open('cities.csv', encoding="utf8") as f:
    reader = csv.reader(f)
    for line in reader:
        next(reader)    # return next line as a list
        print('|'.join(line))     # can also print(line[1])
```
```python
# or with DictReader
fieldnames = ['code', 'city']
with open('cities.csv', encoding="utf8") as f:
    reader = csv.DictReader(f, fieldnames)
    next(reader)    # return next line as a dict
    for line in reader:
        print(f"code {line['code']} for city {line['city']}")
```

---

## Unit tests

---

```python
assert sum(range(5)) == 10                  # ok => no output
assert sum(range(5)) == 11, "Should be 10"  # ko => AssertionError: Should be 10
```

---

In a file (function + test):

---

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

---

Launch tests:

```bash
python my_file.py
```

To write unit tests on your application choose a test runner: unittest, pytest, nose...

```bash
pip install pytest
pytest my_file.py
```

---
