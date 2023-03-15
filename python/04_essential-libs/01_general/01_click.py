# Import the module
import click

# Initiate the minimal contract of commands
@click.command()

# Define the CLI arguments
@click.option("--count", default=1, help="Number of greetings.")
@click.option("--name", prompt="Your name", help="The person to greet.")

# Integrate it in your code
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo(f"Hello {name}!")


if __name__ == "__main__":
    hello()
