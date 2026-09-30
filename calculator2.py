import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit
from PyQt5.QtCore import Qt

STYLE = """
QWidget { background: #f4f5f7; font-family: 'Segoe UI', Arial; }
QLineEdit { background: white; border: none; border-radius: 12px;
            padding: 14px; font-size: 34px; color: #222; }
QPushButton { background: white; border: none; border-radius: 12px;
              font-size: 22px; color: #222; min-height: 56px; }
QPushButton:hover { background: #e9ebef; }
QPushButton:pressed { background: #d9dce2; }
QPushButton[role="op"] { background: #e4edff; color: #2b6cf6; }
QPushButton[role="op"]:hover { background: #d3e2ff; }
QPushButton[role="clear"] { background: #ffe6e6; color: #e03e3e; }
QPushButton[role="clear"]:hover { background: #ffd6d6; }
QPushButton[role="eq"] { background: #2b6cf6; color: white; }
QPushButton[role="eq"]:hover { background: #1f5ae0; }
"""


class Calc(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Máy tính")
        self.setMinimumWidth(320)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(12)

        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        layout.addWidget(self.display)

        grid = QGridLayout()
        grid.setSpacing(10)
        layout.addLayout(grid)

        keys = "C ( ) / 7 8 9 * 4 5 6 - 1 2 3 + 0 . ⌫ =".split()
        for i, k in enumerate(keys):
            btn = QPushButton(k)
            if k in "+-*/()":
                btn.setProperty("role", "op")
            elif k in "C⌫":
                btn.setProperty("role", "clear")
            elif k == "=":
                btn.setProperty("role", "eq")
            btn.clicked.connect(lambda _, k=k: self.press(k))
            grid.addWidget(btn, i // 4, i % 4)

        self.setStyleSheet(STYLE)

    def press(self, k):
        t = self.display.text()
        if t == "Lỗi":
            t = ""
        if k == "C":
            t = ""
        elif k == "⌫":
            t = t[:-1]
        elif k == "=":
            try:
                t = str(round(eval(t), 10))
            except Exception:
                t = "Lỗi"
        else:
            t += k
        self.display.setText(t)


app = QApplication(sys.argv)
w = Calc()
w.show()
sys.exit(app.exec_())
