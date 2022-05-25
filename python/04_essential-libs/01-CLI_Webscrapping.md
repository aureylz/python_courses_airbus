# Python Essential Libs
## Part 1 CLI and web scrapping

## 1. Project presentation and setup
### Context
In this module, we are going to check common python liraries that fullfill particular, and useful tasks. 

One principle to consider here, is : You shouldn't code something by yourself it is already exists, or if you're
perfectly aware of what you are doing !

We will cover in this module three libraries that will all serve a particular purpose. 

### Objective of this hands-on session
We will construct an application in CLI that will gather information on the web and do somehting with is.
At the end, you should be able to :
- Build a simple CLI
- Go into debian.org/releases and get the main page
- Drill down to the release bullseye
- Follow the link
- Find link for AMD 64
- Answer with the physical memory supported by this distribution and print the appropriate sentences

Examples of output :

```
python scrapper --help
python scrapper get-releases --output yaml --random-flag
```
And should produce an output like this : 
```
Not yet implemented here :)
```

### Create venv and project structure
First, let's start by creating the project skeleton and its virtualenv.
Ensure the environment is created with python > 3.6
Create a directory to host the project "part1_cli_webscrapping" and in this directory create your virtualenv

```
python -m venv venv
venv\Scripts\Activate.ps1
```
Then create your directories like this :
```
part1_cli_webscrapping
|--scrapper
|  |--__init__.py
|  |--__main__.py
|--README.md
|--venv
```

## 2. Create your first Hello World, the CLI way
- In your main, create a method named hello_world, that prints Hello World
- Add in front of it the click.command decorator
``` python
@click.command()
def hello_world():
    print("Hello World !")


if __name__ == '__main__':
    hello_world()

```
- Test it !
```
python scrapper
python scrapper hello-world
```

Despite the fact that the addition of click do not add much to the "Hello World" scenario, 
the auto generation of the helper is useful, and you did not write a single line of code for it!

We are now going to add some options to our command. 

### 2.1 Add count option to hello World
Now it is time to add a count option to our hello world command. 
Here is what the program is supposed to do : 
```
python  scrapper hello-world --count 4
Hello World !
Hello World !
Hello World !
Hello World !
```

For your information, click supports a nicer way of printing info within the terminal. 
You can find the reference [here](https://click.palletsprojects.com/en/8.1.x/utils/#printing-to-stdout)

### 2.2 Options in a nutshell
There are various types of possibilities wîth options. Here are some samples
```python
@click.option('--n', required=True, help="A required option")
```
```python
@click.option("-c", "--count", help="Number of hello with default value", type=int, default=2)
```
```python
@click.option("--say-goodbye", is_flag=True, default=False, help="A flag has no argument it is a boolean value. Here we could replace hello by goodbye")
```

You can find all the documentation for options [here](https://click.palletsprojects.com/en/8.1.x/options/)

### 2.3 Grouping several subcommands
In the past example, within our program "Scrapper" we used two different things. 
We used a subcommand called "hello-world" and a particular option "--count".
Within the same program, we will now create a command scrap that will take other options and will have a different method. 

For that, reorganize the program like this :
````python
import click as click


@click.group
def main():
    pass


@main.command
@click.option("-c", "--count", help="Number of hello", type=int, default=2)
def hello_world(count):
    for i in range(count):
        click.echo("Hello World !")


@main.command
def scrap():
    click.echo("My super web scrapper")


if __name__ == '__main__':
    main()

````
Now we are ready to start the second part dedicated to implement the "scrap" method.
## 3. WebScrapping and BeautifulSoup
```python
raise NotImplementedError
```


