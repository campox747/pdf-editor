# PDF Toolkit: Merge & Reorder Utility

pdf-editor allows you to merge PDFs and reorder the pages as you wish.

## Overview
A lightweight, web-based utility designed to handle common, frustrating PDF tasks without the need for expensive software. This tool allows users to easily upload multiple PDF files to append them together (merge) or change the exact sequence of pages within a single PDF document (reorder).

## Features
* **Merge PDFs:** Upload two or more PDF files and stitch them together in your desired order into a single, continuous document.
* **Reorder Pages:** Upload a single PDF, view its total page count, and specify a new custom order for the pages (e.g., move page 5 to the front).
* **Local Processing:** Powered by Python, ensuring that document manipulation happens securely and efficiently.
* **Web Interface:** A clean, intuitive, drag-and-drop UI built with Streamlit.

## Tech Stack
* **Language:** Python 3.13.1.
* **Core Logic / PDF Manipulation:** [`pypdf`](https://pypi.org/project/pypdf/) - A pure-Python library built for splitting, merging, cropping, and transforming PDF pages.
* **Frontend UI:** [`Streamlit`](https://streamlit.io/) - A rapid-prototyping framework that turns Python scripts into interactive web apps.

## Architecture & Logic
This project is separated into backend logic and frontend UI:
1. **The Merge Engine:** Creates a blank `PdfWriter` object in memory, iterates through the uploaded `PdfReader` objects, and appends the pages sequentially before exporting.
2. **The Reorder Engine:** Reads a single uploaded PDF, accepts an array of new page indices from the user, fetches those specific pages in the new order, and writes them to a new file.

## Installation & Setup (Local Development)

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/vfi27/pdf-editor.git](https://github.com/vfi27/pdf-editor.git)
   cd pdf-editor

2. **Create a virtual environment (recommended):**
  ```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. **Install the required dependencies:**
 ```bash
pip install -e .
 ```

4. **Run the application (from any terminal):**
```bash pdf-toolkit
```
