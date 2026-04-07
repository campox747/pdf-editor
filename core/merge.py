from pypdf import PdfWriter
from pathlib import Path


# Merges two PDFs together  
def merge_files(args, output_name, output_path, default):
    merger = PdfWriter()

    for pdf in args:
        merger.append(pdf)
    
    default_path = Path.home() / "Downloads" / "output.pdf"

    if default:
        merger.write(default_path)
    else:
        merger.write(output_path)
    print("Done!")

