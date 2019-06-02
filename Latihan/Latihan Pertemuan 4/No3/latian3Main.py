from PyQt5.QtWidgets import QWidget, QPushButton
from latian3Other import *

class latian3Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()
    def setupUi(self):
        self.resize(400, 300)
        self.move(300, 300)
        self.setWindowTitle('Multiple Window')
        self.button = QPushButton('Tampilkan Form Lain')
        self.button1 = QPushButton('Tutup')
        self.button.move(150, 130)
        self.button1.move(310, 260)
        self.button.setParent(self)
        self.button1.setParent(self)
        self.button.clicked.connect(self.buttonClick)
        self.button1.clicked.connect(self.buttonClick1)
    def buttonClick(self):
        self.form = latian3Other()
        self.form.show()
    def buttonClick1(self):
        self.close()