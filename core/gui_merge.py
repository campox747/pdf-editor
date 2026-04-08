import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QListWidget,
    QAbstractItemView,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QFileDialog,
    QMessageBox
)
from pathlib import Path

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Merge Files")

        # Create the label (title)
        label = QLabel("Please select the files you want to merge in order:")
        font = label.font()
        font.setPointSize(15)
        label.setFont(font)
        label.setAlignment(Qt.AlignmentFlag.AlignLeft)

        # Create List Widget for chosen files (Drag-&-Drop reordering)
        self.files_list = QListWidget()
        self.files_list.setDragDropMode(QAbstractItemView.DragDropMode.InternalMove)

        # Create button to browse files
        files_button = QPushButton("Browse Files...")
        files_button.clicked.connect(self.open_file_browser)

        # Create Merge button to confirm selection and close window
        merge_button = QPushButton("Merge Selected Files")
        merge_button.clicked.connect(self.confirm_and_close)

        ### TO DO: Create Output field to choose the file name and destination folder
        output_button = QPushButton("Choose destination folder") 
        output_button.clicked.connect(self.store_output)

        # Create layout to hold all items
        layout = QVBoxLayout()
        layout.setContentsMargins(30, 15, 30, 15)

        layout.addWidget(label)
        layout.addSpacing(30)

        layout.addWidget(self.files_list)
        layout.addWidget(files_button, alignment=Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(output_button, alignment=Qt.AlignmentFlag.AlignLeft)

        layout.addWidget(merge_button, alignment=Qt.AlignmentFlag.AlignRight)
        layout.addStretch()

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

        # Initialize selected files list and output path
        self.selected_files = []
        self.out_path = None

    # Open file browser and make user select files to merge
    def open_file_browser(self):
        file_paths, _ = QFileDialog.getOpenFileNames(
            self,
            "Select PDFs to Merge",    
            "",                        
            "PDF Files (*.pdf)"        
        )

        if file_paths:
            print("Files Uploaded:")

            # Print files in terminal for later cross-checking
            for file in file_paths:
                print(f"Files: {file}")

            self.files_list.clear()

            # Display the chosen files to the list
            self.files_list.addItems(file_paths)
        
        else:
            print("No files uploaded")


    def store_output(self):
        self.out_path, _ = QFileDialog.getSaveFileName(
            self,
            "Save merged PDF as",
            "",
            "PDF Files (*.pdf)"
        )
        
        if self.out_path:
            self.out_path = Path(self.out_path)


    # Confirm selection and close window if valid
    def confirm_and_close(self):

        # Get current items from the list (in order)
        self.selected_files = [self.files_list.item(i).text() for i in range(self.files_list.count())]

        if len(self.selected_files) < 2:
            QMessageBox.warning(self, "Insufficient Files", "Please select at least 2 PDF files to merge.")
            return

        # Close the window
        self.close()
