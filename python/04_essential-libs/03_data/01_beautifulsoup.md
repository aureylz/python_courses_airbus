# Beautifulsoup

## Plan

1. [What is this?](#What-is-this?)
2. [How to install?](#How-to-install?)
3. [How to use it?](#How-to-use-it?)
    1. [Development](#Development)
    2. [Usage](#Usage)
4. [References](#References)

## What is this?

It's a Python package for parsing HTML and XML documents. It creates a parse tree for parsed pages that can be used to
extract data from HTML, which is useful for web scraping

## How to install?

````shell
pip install beautifulsoup4
````

_Tips:_ Think to add it in your **requirements.txt** file

## How to use it?

### Development

Import the module

````python 
from bs4 import BeautifulSoup
````

Define the HTML page

````python 
html_doc = """
<html>
    <head>
    <title>Hello</title>
    </head>
    <body>
        <p>Texte à lire 1</p>
        <p>Texte à lire 2</p>
    </body>
</html>
"""
````

Load the HTML in Beautifulsoup

````python 
soup = BeautifulSoup(html_doc) 
````

Display each content of the HTML page

````python
for p in soup.find_all('p'):
    print(p)
````

### Usage

Execute your python script with the help of the CLI:

````shell 
$ python hello.py
````

Which display the following information:

````text
<p>Texte à lire 1</p>
<p>Texte à lire 2</p>
````

## References

- https://python.doctor/page-beautifulsoup-html-parser-python-library-xml