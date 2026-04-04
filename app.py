import argparse
import core
from pypdf import PdfWriter
from core.merge import merge_files


def main():
    # 1. Initialize the parser
    parser = argparse.ArgumentParser(description="Merge multiple PDFs into one.")

    # 2. Define the arguments you expect
    parser.add_argument('mode', choices=['merge', 'reorder'], help="Name the operation you want to perform")

    parser.add_argument('inputs', nargs='+', help="The PDF files you want to merge")

    # -o or --output is an optional flag, defaulting to 'pdf-toolkit.pdf' if not provided
    parser.add_argument('-o', '--output', default='pdf-toolkit.pdf', help="Name of the output file")

    # 3. Parse what the user actually typed in the terminal
    args = parser.parse_args()

    if args.mode == 'merge':
        print(f"Merging these files: {args.inputs}")
        print(f"Saving as: {args.output}")

        try:
            merge_files(args.inputs, args.output) 
            print("Merge successful!")
        except FileNotFoundError:
            print("Error: One of the files you typed does not exist in this folder.")
        except Exception as e:
            # This catches any other weird errors and tells you exactly what they are
            print(f"An unexpected error occurred: {e}")
