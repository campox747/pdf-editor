import argparse
from pypdf import PdfWriter
from merge import merge_files


# 1. Initialize the parser
parser = argparse.ArgumentParser(description="Merge multiple PDFs into one.")

# 2. Define the arguments you expect
# nargs='+' means "expect one OR MORE files"
parser.add_argument('mode', choices=['merge', 'reorder'], help="Name the operation you want to perform")

parser.add_argument('inputs', nargs='+', help="The PDF files you want to merge")

# -o or --output is an optional flag, defaulting to 'merged.pdf' if not provided
parser.add_argument('-o', '--output', default='merged.pdf', help="Name of the output file")

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
