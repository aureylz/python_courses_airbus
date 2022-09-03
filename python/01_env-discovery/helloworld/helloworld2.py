#!/usr/bin/env python


def helloworld(name):
    """Basic Hello World. Print the name given.

    Args:
        name (str): Name to be greeted
    """
    output = f"Hello World, {name} !"
    print(output)
    return output


if __name__ == "__main__":
    # Execute when the module is not initialized from an import statement.
    helloworld("Airbus CyberDiploma")
