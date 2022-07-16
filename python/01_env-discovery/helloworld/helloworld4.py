#!/usr/bin/env python

from rich.console import Console
from time import sleep

console = Console()


def hello():
    data = [1, 2, 3]
    with console.status("[bold green]Fetching data...") as status:
        while data:
            num = data.pop(0)
            sleep(0.3)
            console.log(f"[green]Finish fetching data[/green] {num}")
        console.log(f"[bold][red]Done!")
    console.log("")
    console.log("[i]Hello[/i] [bold blue]World[/]! :fireworks: ")


if __name__ == "__main__":
    # Execute when the module is not initialized from an import statement.
    hello()
