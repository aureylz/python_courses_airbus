# Table of Content
- [Table of Content](#table-of-content)
  - [Files I/O](#files-io)
  - [Parsing](#parsing)
    - [JSON](#json)
    - [CSV](#csv)
  - [Unit tests](#unit-tests)

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
