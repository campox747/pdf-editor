from pypdf import PdfReader, PdfWriter
from pathlib import Path

def get_page_count(file_path):
    reader = PdfReader(file_path)
    total = len(reader.pages)
    return total

def validate_sequence(raw_input, max_pages):
    clean_sequence = []
    try:
        parts = raw_input.replace(",", " ").split()
        if len(parts) != max_pages:
            return False
        
        for part in parts:
            if not part.isdigit():
                return False
            
            page_num = int(part)
            if page_num < 1 or page_num > max_pages:
                return False
            
            clean_sequence.append(page_num - 1)
        
        # check for duplicates
        if len(set(clean_sequence)) != max_pages:
            return False
        
        return clean_sequence
    except:
        return False

def reorder_pages(target_file, output_name, output_path):
    reader = PdfReader(target_file)
    writer = PdfWriter()
    total = len(reader.pages)
    
    raw_input = input(f"Enter the new page order (1-{total}, comma-separated): ")
    clean_sequence = validate_sequence(raw_input, total)
    
    if not clean_sequence:
        print("Invalid sequence. Please try again.")
        return
    
    for page_num in clean_sequence:
        writer.add_page(reader.pages[page_num])
    
    if output_path is None:
        writer.write(Path.home() / "Downloads" / output_name)
    else:
        writer.write(output_path)
    
    print("Done!")