import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QLabel

class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Calculator")
        self.setGeometry(100, 100, 300, 200)

        self.init_ui()

    def init_ui(self):
        # Create widgets
        self.result_label = QLabel(self)
        self.result_label.setText("Result:")
        self.input1 = QLineEdit(self)
        self.input2 = QLineEdit(self)
        self.result = QLineEdit(self)
        self.result.setReadOnly(True)

        # Create buttons for arithmetic operations
        add_button = QPushButton("Add", self)
        subtract_button = QPushButton("Subtract", self)
        multiply_button = QPushButton("Multiply", self)
        divide_button = QPushButton("Divide", self)

        # Add button click events
        add_button.clicked.connect(self.add)
        subtract_button.clicked.connect(self.subtract)
        multiply_button.clicked.connect(self.multiply)
        divide_button.clicked.connect(self.divide)

        # Create layout
        main_layout = QVBoxLayout()
        input_layout = QHBoxLayout()
        operation_layout = QHBoxLayout()

        input_layout.addWidget(self.input1)
        input_layout.addWidget(self.input2)

        operation_layout.addWidget(add_button)
        operation_layout.addWidget(subtract_button)
        operation_layout.addWidget(multiply_button)
        operation_layout.addWidget(divide_button)

        main_layout.addLayout(input_layout)
        main_layout.addLayout(operation_layout)
        main_layout.addWidget(self.result_label)
        main_layout.addWidget(self.result)

        self.setLayout(main_layout)

    def calculate(self, operation):
        try:
            num1 = float(self.input1.text())
            num2 = float(self.input2.text())
            if operation == 'add':
                result = num1 + num2
            elif operation == 'subtract':
                result = num1 - num2
            elif operation == 'multiply':
                result = num1 * num2
            elif operation == 'divide':
                if num2 == 0:
                    result = "Error: Division by zero"
                else:
                    result = num1 / num2
            else:
                result = "Invalid operation"
        except ValueError:
            result = "Invalid input"
        self.result.setText(str(result))

    def add(self):
        self.calculate('add')

    def subtract(self):
        self.calculate('subtract')

    def multiply(self):
        self.calculate('multiply')

    def divide(self):
        self.calculate('divide')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CalculatorApp()
    window.show()
    sys.exit(app.exec_())