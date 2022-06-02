# Threading

1. [What is this?](#What-is-this?)
2. [How to install?](#How-to-install?)
3. [How to use it?](#How-to-use-it?)
    1. [Development](#Development)
    2. [Usage](#Usage)
4. [References](#References)

## What is this?

Python threading allows you to have different parts of your program run concurrently and can simplify your design. If
you’ve got some experience in Python and want to speed up your program using threads, then this tutorial is for you!

## How to install?

Nothing todo, it's available by default in the python environment :)

## How to use it?

### Development

Import the module

````python 
import threading
````

Integrate it in your code

````python
x = threading.Thread(target=thread_function, args=(1,))
````

### Usage

Write a python script as follow

````shell
import logging
import threading
import time

def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    threads = list()
    for index in range(3):
        logging.info(f"Main    : create and start thread {index}")
        x = threading.Thread(target=thread_function, args=(index,))
        threads.append(x)
        x.start()

    for index, thread in enumerate(threads):
        logging.info(f"Main    : before joining thread {index}")
        thread.join()
        logging.info(f"Main    : thread {index} done")
````

And execute it by CLI:

````shell
$ python hello.py
22:51:05: Main    : create and start thread 0
22:51:05: Thread 0: starting
22:51:05: Main    : create and start thread 1
22:51:05: Thread 1: starting
22:51:05: Main    : create and start thread 2
22:51:05: Thread 2: starting
22:51:05: Main    : before joining thread 0
22:51:07: Thread 0: finishing
22:51:07: Main    : thread 0 done
22:51:07: Main    : before joining thread 1
22:51:07: Thread 1: finishing
22:51:07: Thread 2: finishing
22:51:07: Main    : thread 1 done
22:51:07: Main    : before joining thread 2
22:51:07: Main    : thread 2 done
````

## References

- https://realpython.com/intro-to-python-threading
- https://docs.python.org/3/library/threading.html