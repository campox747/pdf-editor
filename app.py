import questionary
from rich import print
from rich.panel import Panel
from rich.console import Console
from core.merge import merge_files
from rich.align import Align

# Initialize Console
console = Console()

def main():

    # Print title

    title_panel = Panel(
    "[bold cyan]Welcome to PDF Toolkit![/bold cyan]",
    border_style="cyan",
    padding=(1, 5),  # Adds 1 line of vertical padding, 5 spaces of horizontal padding
    expand=False
    )

    console.print("\n")
    console.print(Align.center(title_panel))
    console.print("\n")

    # Print Info Note
    
    note_panel = Panel(
    "Use [bold white]Ctrl + C[/bold white] (on Windows & macOS) to go back a stage.",
    title="[bold yellow]💡 Note[/bold yellow]",
    border_style="yellow",
    style="yellow",
    expand=False
    )
    console.print(note_panel)
    console.print("\n")

    # Ask user about the type of operation

    operation = questionary.select(
        "What would you like to do?",
        choices=["Merge PDFs",
                 "Reorder PDF",
                 "Help",
                 "Exit"
        ]).ask()
    
    if (operation == "Exit"):

        # Exit program
        console.print("See you later!")
        return

    elif (operation == "Merge PDFs"):
    
        # TO DO: Open pop up to make user upload PDFs with drag-and-drop
        # Inside pop-up, make user upload files and make sure there are at least two. When done, go ahead.


        console.print(f"\n[yellow]Merging {len(input)} files...[/yellow]")


        try:
            merge_files(input, output)
            console.print("[bold green]Merged successfully![/bold green]\n")
        except FileNotFoundError:
            console.print("[bold red]Error: One of the files you typed does not exist.[/bold red]\n")
        except Exception as e:
            console.print(f"[bold red]An unexpected error occurred: {e}[/bold red]\n")
