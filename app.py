import questionary
import sys
from rich import print
from rich.panel import Panel
from rich.console import Console
from core.merge import merge_files
from rich.align import Align
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from core.gui_merge import MainWindow

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
    "Use [bold white]Ctrl + C[/bold white] (on Windows & macOS) to abort.",
    title="[bold yellow]💡 Note[/bold yellow]",
    border_style="yellow",
    style="yellow",
    expand=False
    )
    console.print(note_panel)
    console.print("\n")

    # Ask user about type of operation
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

        app = QApplication(sys.argv)

        window = MainWindow()
        window.show()

        app.exec()

        # Retrieve selected files from the GUI
        selected_files = window.selected_files

        if not selected_files:
            console.print("[bold red]No files selected. Operation cancelled.[/bold red]\n")
            return

        console.print(f"\n[yellow]Merging {len(selected_files)} files...[/yellow]")

        # TODO: Define output file path (e.g., ask user or use a default)
        output = "merged_output.pdf"  # Placeholder - replace with user input logic

        try:
            merge_files(selected_files, output)
            console.print("[bold green]Merged successfully![/bold green]\n")
        except FileNotFoundError:
            console.print("[bold red]Error: One of the files you typed does not exist.[/bold red]\n")
        except Exception as e:
            console.print(f"[bold red]An unexpected error occurred: {e}[/bold red]\n")
