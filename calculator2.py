import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit
from PyQt5.QtCore import Qt


class Calc(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Máy tính")
        layout = QVBoxLayout(self)
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        layout.addWidget(self.display)
        grid = QGridLayout()
        layout.addLayout(grid)
        keys = "C ( ) / 7 8 9 * 4 5 6 - 1 2 3 + 0 . ⌫ =".split()
        for i, k in enumerate(keys):
            btn = QPushButton(k)
            btn.clicked.connect(lambda _, k=k: self.press(k))
            grid.addWidget(btn, i // 4, i % 4)

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