from core.reorder import reorder_pages
import questionary
import sys
from rich import print
from rich.panel import Panel
from rich.console import Console
from core.merge import merge_files
from rich.align import Align
from PyQt6.QtWidgets import QApplication
from core.gui_merge import MainWindow
from core.gui_reorder import ReorderWindow

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
        "Press [bold white]Enter [/bold white]to select. \n [bold white]Use Ctrl + C [/bold white](on Windows & macOS) to abort.",
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

        output_name = "merged_output.pdf" 
        output_path = None

        if getattr(window, "out_path", None):
            output_path = window.out_path
            output_name = window.out_path.name
            console.print(f"Output will be saved to: {output_path}")
        else:
            console.print(f"Output will be saved to default Downloads path as: {output_name}")

        try:
            merge_files(selected_files, output_name, output_path)
            console.print("[bold green]Merged successfully![/bold green]\n")
        except FileNotFoundError:
            console.print("[bold red]Error: One of the files you typed does not exist.[/bold red]\n")
        except Exception as e:
            console.print(f"[bold red]An unexpected error occurred: {e}[/bold red]\n")

    elif (operation == "Reorder PDF"):

        app = QApplication(sys.argv)

        window = ReorderWindow()
        window.show()

        app.exec()

        # Retrieve selected files from the GUI
        selected_files = window.selected_files

        # Check if they selected nothing
        if not selected_files:
            console.print("[bold red]No files selected. Operation cancelled.[/bold red]\n")
            return

        # Check if they selected too many files
        if len(selected_files) > 1:
            console.print("[bold red]Error: Please select only ONE file to reorder.[/bold red]\n")
            return

        # Extract the single target file
        target_file = selected_files[0]

        console.print(f"\n[yellow]Preparing to reorder: {target_file}[/yellow]")

        output_name = "reordered_output.pdf" 
        output_path = None

        if getattr(window, "out_path", None):
            output_path = window.out_path
            output_name = window.out_path.name
            console.print(f"Output will be saved to: {output_path}")
        else:
            console.print(f"Output will be saved to default Downloads path as: {output_name}")

        try:
            reorder_pages(target_file, output_name, output_path)
            console.print("[bold green]Reordered successfully![/bold green]\n")
        except FileNotFoundError:
            console.print("[bold red]Error: One of the files you typed does not exist.[/bold red]\n")
        except Exception as e:
            console.print(f"[bold red]An unexpected error occurred: {e}[/bold red]\n")
