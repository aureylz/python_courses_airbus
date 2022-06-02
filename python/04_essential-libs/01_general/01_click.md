# Click

1. [What is this?](#What-is-this?)
2. [How to install?](#How-to-install?)
3. [How to use it?](#How-to-use-it?)
    1. [Development](#Development)
    2. [Usage](#Usage)
4. [References](#References)

## What is this?

Click is a Python package for creating beautiful command line interfaces in a composable way with as little code as
necessary. It’s the “Command Line Interface Creation Kit”. It’s highly configurable but comes with sensible defaults out
of the box.

It aims to make the process of writing command line tools quick and fun while also preventing any frustration caused by
the inability to implement an intended CLI API.

Click in three points:

1. arbitrary nesting of commands
2. automatic help page generation
3. supports lazy loading of subcommands at runtime

## How to install?

````shell
pip install click
````

_Tips:_ Think to add it in your **requirements.txt** file

## How to use it?

### Development

Import the module

````python 
import click 
````

Initiate the minimal contract of commands

````python 
@click.command() 
````

Define the CLI arguments

````python
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name', help='The person to greet.')
````

Integrate it in your code

````python
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo(f"Hello {name}!")

        
if __name__ == '__main__':
    hello()
````

### Usage

Execute your python script with the help of the CLI, it will ask you to add your name:

````shell
$ python hello.py --count=3
Your name: 
````

This will display the following result (if the name was John :)

````text
Hello John!
Hello John!
Hello John!
````

## References

- https://click.palletsprojects.com/en/8.1.x
