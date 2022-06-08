# Requests

1. [What is this?](#What-is-this?)
2. [How to install?](#How-to-install?)
3. [How to use it?](#How-to-use-it?)
    1. [Development](#Development)
    2. [Usage](#Usage)
4. [References](#References)

## What is this?

Requests is a library that allows you to make HTTP Requests with a simple fashion.

## How to install?

```shell
pip install requests
```

_Tips:_ Think to add it in your **requirements.txt** file

## How to use it?

### Development

Import the module

```python 
import requests
```

Minimal example : 

```python
def get_request():
    response = requests.get("https://python.org")
    # Response will be the object containing the data from the URL
    print(response)
    # Will print <Response [200]>
    
    print(response.text)
    # Will display the body of the response, here will respond with the page itself (html)

```


### Usage

Query parameters and headers can be added like this : 

```python
response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'},
    headers={'Accept': 'application/vnd.github.v3.text-match+json'},
)
```

You can simply use all HTTP verbs like this : 

```python
requests.post('https://httpbin.org/post', data={'key':'value'})
requests.put('https://httpbin.org/put', data={'key':'value'})
requests.delete('https://httpbin.org/delete')
requests.head('https://httpbin.org/get')
requests.patch('https://httpbin.org/patch', data={'key':'value'})
requests.options('https://httpbin.org/get')
```

The ```response``` will allow you to retrieve everything you need

```python
response = requests.get("https://python.org")

response.status_code # Will print the status, 200 if everything is ok
response.text # Will print the response text
response.json() # Will print the response formatted in json, very useful for API calls
```

## References

- https://requests.readthedocs.io/en/latest/