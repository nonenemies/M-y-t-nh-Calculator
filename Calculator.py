import sys
import re
import math
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                             QGridLayout, QPushButton, QLineEdit, QTextEdit, QLabel, QSizePolicy)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont


class ExtendedCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Máy tính Khoa học Mở rộng - Responsive")

        self.setMinimumSize(750, 450) 
        self.resize(850, 550)

        self.initUI()

    def initUI(self):
        self.main_layout = QHBoxLayout()
        self.main_layout.setContentsMargins(15, 15, 15, 15)
        self.main_layout.setSpacing(20)

        self.calc_layout = QVBoxLayout()

        self.display = QLineEdit('0')
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setFont(QFont("Arial", 26, QFont.Weight.Bold))
        self.display.setMinimumHeight(80)
        self.display.setStyleSheet("""
            QLineEdit {
                background-color: #e8f4f8; 
                padding: 10px; 
                border: 2px solid #b0c4de; 
                border-radius: 8px;
                color: #333333;
            }
        """)
        self.calc_layout.addWidget(self.display)


        self.grid_layout = QGridLayout()
        self.grid_layout.setSpacing(8)

        buttons = [
            ('(', 0, 0), (')', 0, 1), ('C', 0, 2), ('⌫', 0, 3), ('/', 0, 4),
            ('sin', 1, 0), ('cos', 1, 1), ('tan', 1, 2), ('π', 1, 3), ('*', 1, 4),
            ('√', 2, 0), ('7', 2, 1), ('8', 2, 2), ('9', 2, 3), ('-', 2, 4),
            ('x²', 3, 0), ('4', 3, 1), ('5', 3, 2), ('6', 3, 3), ('+', 3, 4),
            ('log', 4, 0), ('1', 4, 1), ('2', 4, 2), ('3', 4, 3), ('=', 4, 4, 2, 1),
            ('^', 5, 0), ('0', 5, 1, 1, 2), ('.', 5, 3)
        ]

        for btn_data in buttons:
            text = btn_data[0]
            btn = QPushButton(text)
            btn.setFont(QFont("Arial", 14, QFont.Weight.Bold))

            if text in ['+', '-', '*', '/']:
                btn.setStyleSheet("background-color: #ff9900; color: white; border-radius: 6px;")
            elif text == 'C':
                btn.setStyleSheet("background-color: #ff4c4c; color: white; border-radius: 6px;")
            elif text == '⌫':
                btn.setStyleSheet("background-color: #f4a261; color: white; border-radius: 6px;")
            elif text == '=':
                btn.setStyleSheet("background-color: #4CAF50; color: white; border-radius: 6px;")
            elif text in ['sin', 'cos', 'tan', 'log', '√', 'x²', '^', 'π', '(', ')']:
                btn.setStyleSheet("background-color: #457b9d; color: white; border-radius: 6px;")
            else:
                btn.setStyleSheet("background-color: #ffffff; color: #333; border: 1px solid #ccc; border-radius: 6px;")

            btn.clicked.connect(self.on_button_click)

            btn.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
            btn.setMinimumHeight(50)

            row, col = btn_data[1], btn_data[2]
            rowSpan = btn_data[3] if len(btn_data) > 3 else 1
            colSpan = btn_data[4] if len(btn_data) > 4 else 1

            self.grid_layout.addWidget(btn, row, col, rowSpan, colSpan)

        self.calc_layout.addLayout(self.grid_layout)

        self.history_layout = QVBoxLayout()

        self.history_label = QLabel("Lịch sử tính toán")
        self.history_label.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        self.history_layout.addWidget(self.history_label)

        self.history_display = QTextEdit()
        self.history_display.setReadOnly(True)
        self.history_display.setFont(QFont("Arial", 12))
        self.history_display.setStyleSheet(
            "background-color: #fdfdfd; padding: 5px; border: 1px solid #ccc; border-radius: 8px;")

        self.history_display.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.history_layout.addWidget(self.history_display)

        self.clear_history_btn = QPushButton("🗑 Xóa lịch sử")
        self.clear_history_btn.setFont(QFont("Arial", 11, QFont.Weight.Bold))
        self.clear_history_btn.setMinimumHeight(40)
        self.clear_history_btn.setStyleSheet("background-color: #6c757d; color: white; border-radius: 6px;")
        self.clear_history_btn.clicked.connect(lambda: self.history_display.clear())
        self.history_layout.addWidget(self.clear_history_btn)

        self.main_layout.addLayout(self.calc_layout, 65)
        self.main_layout.addLayout(self.history_layout, 35)

        self.setLayout(self.main_layout)

    def on_button_click(self):
        btn = self.sender()
        text = btn.text()
        current_text = self.display.text()

        if "Lỗi" in current_text:
            current_text = '0'

        if text == 'C':
            self.display.setText('0')
        elif text == '⌫':
            if len(current_text) > 1:
                self.display.setText(current_text[:-1])
            else:
                self.display.setText('0')
        elif text == '=':
            self.calculate_result(current_text)
        else:
            self.handle_input(text, current_text)

    def handle_input(self, text, current_text):
        if text in ['sin', 'cos', 'tan', 'log', '√']:
            text += '('
        if text == 'x²':
            text = '²'
        if text in '+-*/^':
            if current_text[-1] in '+-*/^':
                current_text = current_text[:-1]
        if text == '.':
            last_number = re.split(r'[\+\-\*\/\^\(\)]', current_text)[-1]
            if '.' in last_number:
                return

        if current_text == '0' and text not in '+-*/^².)':
            self.display.setText(text)
        else:
            self.display.setText(current_text + text)

    def calculate_result(self, expression):
        original_expression = expression
        try:
            expression = expression.replace('²', '**2')
            expression = expression.replace('^', '**')
            expression = expression.replace('π', str(math.pi))

            expression = expression.replace('sin', 'math.sin')
            expression = expression.replace('cos', 'math.cos')
            expression = expression.replace('tan', 'math.tan')
            expression = expression.replace('log', 'math.log10')
            expression = expression.replace('√', 'math.sqrt')

            open_brackets = expression.count('(')
            close_brackets = expression.count(')')
            if open_brackets > close_brackets:
                expression += ')' * (open_brackets - close_brackets)

            if expression[-1] in '+-*/':
                expression = expression[:-1]

            result = eval(expression)

            if isinstance(result, float):
                result = round(result, 10)
                if result.is_integer():
                    result = int(result)

            result_str = str(result)
            self.display.setText(result_str)

            history_text = f"{original_expression}\n= {result_str}\n"
            self.history_display.append(history_text)

        except ZeroDivisionError:
            self.display.setText("Lỗi: Chia cho 0")
        except ValueError:
            self.display.setText("Lỗi miền giá trị")
        except SyntaxError:
            self.display.setText("Lỗi cú pháp")
        except Exception as e:
            self.display.setText("Lỗi")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = ExtendedCalculator()
    calc.show()
    sys.exit(app.exec())
