import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QFileDialog
)

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Merge Files")

        # Create the label
        label = QLabel("Please select the files you want to merge in order:")
        font = label.font()
        font.setPointSize(15)
        label.setFont(font)
        label.setAlignment(Qt.AlignmentFlag.AlignLeft)

        file1 = QLabel("Your Files:")
        files_button = QPushButton("Browse Files...")

        files_button.clicked.connect(self.open_file_browser)

        # Create a layout to hold your items
        layout = QVBoxLayout()
        layout.setContentsMargins(30, 15, 30, 15)

        layout.addWidget(label)

        layout.addSpacing(30)

        layout.addWidget(file1)
        layout.addWidget(files_button, alignment=Qt.AlignmentFlag.AlignLeft)

        layout.addStretch()

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    # Open file browser and make user selct files to merge
    def open_file_browser(self):
        file_paths, _ = QFileDialog.getOpenFileNames(
            self,
            "Select PDFs to Merge",    
            "",                        
            "PDF Files (*.pdf)"        
        )

        if file_paths:
            print(f"Files: {file_paths}")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()