from pypdf import PdfWriter
from pathlib import Path


# Merges two PDFs together  
def merge_files(args, output_name, output_path=None):
    merger = PdfWriter()

    for pdf in args:
        merger.append(pdf)
    
    if output_path is None:
        merger.write(Path.home() / "Downloads" / output_name)
    else:
        merger.write(output_path)
    print("Done!")

