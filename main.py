from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLineEdit
from PyQt5.QtGui import QFont, QPalette, QColor
from PyQt5.QtCore import Qt

class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculadora")
        self.setGeometry(100, 100, 350, 500)

        self.grid = QGridLayout()
        self.setLayout(self.grid)

        self.entry = QLineEdit()
        self.entry.setFont(QFont('Arial', 32))
        self.entry.setAlignment(Qt.AlignRight)
        self.entry.setReadOnly(True)
        self.entry.setStyleSheet("""
            background-color: #252526;
            color: #ffffff;
            border: 1px solid #444;
            padding: 15px;
            font-size: 32px;
            border-radius: 5px;
            """)
        self.grid.addWidget(self.entry, 0, 0, 1, 4)

        self.buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0, 1, 2), ('.', 4, 2), ('+', 4, 3),
            ('C', 5, 0, 1, 2), ('=', 5, 2, 1, 2)
        ]

        for button in self.buttons:
            if len(button) == 3:
                text, row, col = button
                rowspan = colspan = 1
            elif len(button) == 4:
                text, row, col, rowspan = button
                colspan = 1
            elif len(button) == 5:
                text, row, col, rowspan, colspan = button

            button_widget = QPushButton(text)
            button_widget.setFont(QFont('Arial', 24))
            button_widget.setStyleSheet(self.get_button_style(text))
            button_widget.clicked.connect(self.on_button_click)
            self.grid.addWidget(button_widget, row, col, rowspan, colspan)

        self.setStyleSheet("""
            QWidget {
                background-color: #1e1e1e;
                border-radius: 10px;
            }
        """)

    def get_button_style(self, text):
        if text in ['+', '-', '*', '/', '=']:
            return """
                background-color: #0078d4;
                color: white;
                border: 1px solid #005a9e;
                border-radius: 5px;
                padding: 15px;
                font-size: 24px;
            """
        elif text == 'C':
            return """
                background-color: #d83b01;
                color: white;
                border: 1px solid #a03600;
                border-radius: 5px;
                padding: 15px;
                font-size: 24px;
            """
        else:
            return """
                background-color: #333333;
                color: white;
                border: 1px solid #444;
                border-radius: 5px;
                padding: 15px;
                font-size: 24px;
            """

    def on_button_click(self):
        button_text = self.sender().text()
        current_text = self.entry.text()

        if button_text == '=':
            try:
                result = eval(current_text)
                self.entry.setText(str(result))
            except Exception:
                ''
        elif button_text == 'C':
            self.entry.clear()
        else:
            if button_text == '.' and ('.' in current_text or current_text[-1] in '+-*/'):
                return
            self.entry.setText(current_text + button_text)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
