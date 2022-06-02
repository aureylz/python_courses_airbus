# Loguru

1. [What is this?](#What-is-this?)
2. [How to install?](#How-to-install?)
3. [How to use it?](#How-to-use-it?)
    1. [Development](#Development)
    2. [Usage](#Usage)
4. [References](#References)

## What is this?

Loguru is a library which aims to bring enjoyable logging in Python.

#### What is logging?

It's the fact to record the application's events in a storage to allow to track, debug, monitor... the behaviour of the
application.

## How to install?

````shell
pip install loguru
````

_Tips:_ Think to add it in your **requirements.txt** file

## How to use it?

### Development

Import the module

````python 
from loguru import logger
````

Integrate it in your code

````python
logger.add("file_{time}.log")

logger.debug("hello")
````

### Usage

Track the function usage with the following example:

````python
import sys
from loguru import logger

logger.add("can_crash_{time}.log")
logger.add(sys.stderr, format="{time} {level} {message}", level="INFO")


@logger.catch
def can_crash(x):
    logger.debug(x)
    if x == 0:
        logger.info(f"It'll crash!")
    res = 1 / x
    logger.debug(res)
    return res


if __name__ == '__main__':
    can_crash(1)
    can_crash(0)
````

Execute your python script with the help of the CLI:

````shell
$ python can_crash.py
````

It will display the following result

````shell
2022-06-02 22:25:27.500 | DEBUG    | __main__:can_crash:10 - 1
2022-06-02 22:25:27.501 | DEBUG    | __main__:can_crash:14 - 1.0
2022-06-02 22:25:27.501 | DEBUG    | __main__:can_crash:10 - 0
2022-06-02 22:25:27.501 | INFO     | __main__:can_crash:12 - It'll crash!
2022-06-02T22:25:27.501497+0200 INFO It'll crash!
2022-06-02 22:25:27.501 | ERROR    | __main__:<module>:20 - An error has been caught in function '<module>', process 'MainProcess' (82510), thread 'MainThread' (4346654144):
Traceback (most recent call last):

> File "t.py", line 20, in <module>
    can_crash(0)
    └ <function can_crash at 0x1014eea70>

  File "t.py", line 13, in can_crash
    res = 1 / x
              └ 0

ZeroDivisionError: division by zero
2022-06-02T22:25:27.501638+0200 ERROR An error has been caught in function '<module>', process 'MainProcess' (82510), thread 'MainThread' (4346654144):
Traceback (most recent call last):

> File "t.py", line 20, in <module>
    can_crash(0)
    └ <function can_crash at 0x1014eea70>

  File "t.py", line 13, in can_crash
    res = 1 / x
              └ 0

ZeroDivisionError: division by zero
````

And you can get the information from the log file also:

````shell
% cat can_crash_2022-06-02_22-25-27_495887.log 
2022-06-02 22:25:27.500 | DEBUG    | __main__:can_crash:10 - 1
2022-06-02 22:25:27.501 | DEBUG    | __main__:can_crash:14 - 1.0
2022-06-02 22:25:27.501 | DEBUG    | __main__:can_crash:10 - 0
2022-06-02 22:25:27.501 | INFO     | __main__:can_crash:12 - It'll crash!
2022-06-02 22:25:27.501 | ERROR    | __main__:<module>:20 - An error has been caught in function '<module>', process 'MainProcess' (82510), thread 'MainThread' (4346654144):
Traceback (most recent call last):

> File "t.py", line 20, in <module>
    can_crash(0)
    └ <function can_crash at 0x1014eea70>

  File "t.py", line 13, in can_crash
    res = 1 / x
              └ 0
````

## References

- https://loguru.readthedocs.io/en/stable/overview.html#features