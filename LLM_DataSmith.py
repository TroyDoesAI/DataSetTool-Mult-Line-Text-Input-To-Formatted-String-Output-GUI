import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QTextEdit,
    QPushButton,
    QLabel
)

class TextToStringConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("Text to Python String Converter")
        
        # Main layout
        layout = QVBoxLayout()
        
        # Label + Input box
        layout.addWidget(QLabel("Paste your text here:"))
        self.input_edit = QTextEdit()
        layout.addWidget(self.input_edit)
        
        # Convert button
        convert_button = QPushButton("Convert")
        convert_button.clicked.connect(self.convert_text)
        layout.addWidget(convert_button)
        
        # Label + Output box
        layout.addWidget(QLabel("Python formatted string:"))
        self.output_edit = QTextEdit()
        self.output_edit.setReadOnly(True)
        layout.addWidget(self.output_edit)
        
        # Copy button
        copy_button = QPushButton("Copy Output")
        copy_button.clicked.connect(self.copy_output)
        layout.addWidget(copy_button)
        
        # Set the layout
        self.setLayout(layout)
        
    def convert_text(self):
        """Convert the input text into a Python literal string with escapes."""
        input_text = self.input_edit.toPlainText()
        # Use repr() to get Python-friendly literal, including \n and \t escapes.
        formatted_text = repr(input_text)
        self.output_edit.setPlainText(formatted_text)
        
    def copy_output(self):
        """Copy the output to the clipboard."""
        clipboard = QApplication.clipboard()
        clipboard.setText(self.output_edit.toPlainText())

def main():
    app = QApplication(sys.argv)
    window = TextToStringConverter()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
