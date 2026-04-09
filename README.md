# PDF Toolkit: Merge & Reorder Utility

pdf-editor allows you to merge PDFs and reorder the pages as you wish through a simple and interactive program run directly form your terminal.

## Overview
A lightweight, local utility designed to handle common PDF tasks without the need for expensive software or internet connection. This tool allows users to easily upload multiple PDF files to append them together (merge) or change the exact sequence of pages within a single PDF document (reorder).

## Features
* **Merge PDFs:** Upload two or more PDF files and stitch them together in your desired order into a single, continuous document.
* **Reorder Pages:** Upload a single PDF, view its total page count, and specify a new custom order for the pages (e.g., move page 5 to the front).
* **Local Processing:** Powered by Python, ensuring that document manipulation happens securely and efficiently.
* **User Interface:** A clean and minimal terminal UI built with PyQt6 and rich.

## Tech Stack
* **Language:** Python 3.13.1
* **Core Logic / PDF Manipulation:** [`pypdf`](https://pypi.org/project/pypdf/) — a pure-Python library for splitting, merging, cropping, and transforming PDF pages.
* **Frontend UI:** [`PyQt6`](https://www.riverbankcomputing.com/static/Docs/PyQt6/) — used for building an intuitive desktop interface.
* **Terminal Styling:** [`rich`](https://rich.readthedocs.io/en/latest/index.html) — for colorful, readable terminal output.

## Architecture & Logic
This project separates backend processing from the frontend interface:
1. **Merge Engine:** Initializes a `PdfWriter`, iterates over the uploaded PDF files, and appends their pages in order before exporting. The merged document is saved to the user-provided path and filename, or to the default Downloads folder if no custom output is selected.
2. **Reorder Engine:** Reads a single uploaded PDF, accepts a new page order from the user, selects pages in that order, and writes the reordered document to a new file.

## Installation & Setup (Local Development)

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/vfi27/pdf-editor.git](https://github.com/vfi27/pdf-editor.git)
   cd pdf-editor

2. **Create a virtual environment (recommended):**
  ```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. **Install the required dependencies:**
 ```bash
pip install -e .
 ```

4. **Run the application (from any terminal):**
```bash
 pdf-toolkit
```
