from pypdf import PdfWriter

# Merges two PDFs together  
def merge_files(args, output_name):
    merger = PdfWriter()

    for pdf in args:
        merger.append(pdf)

    merger.write(output_name)
    print("Done!")