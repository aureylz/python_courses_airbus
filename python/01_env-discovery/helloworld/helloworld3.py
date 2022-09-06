#!/usr/bin/env python
import random


class helloworld:
    """
    HelloWorld Class including utilities
    """

    def __init__(self, name):
        self.name = name

    def hello(self):
        """
        Basic Hello World. Greet the name stored in the class
        """
        output= f"Hello, {self.name} !"
        print(output)

    def goodbye(self):
        """
        Say Goodbye the name stored in the class
        """
        output= f"Goodbye, {self.name} !"
        print(output)


def demo1():
    """
    Demo function used to show how the class is used
    """
    jane = helloworld("Jane")
    bob = helloworld("Bob")
    jane.hello()
    bob.hello()
    jane.goodbye()
    bob.goodbye()


def demo2():
    """
    Demo function used to show advanced usage of the class
    """
    names = ["Bob", "Jane", "Jack", "James", "Mary"]
    helloworlds = [helloworld(x) for x in names]

    for name in helloworlds:
        name.hello()

    random.shuffle(helloworlds)
    for name in helloworlds:
        name.goodbye()

def demo3():
    pass

if __name__ == "__main__":
    # Execute when the module is not initialized from an import statement.
    demo3()
