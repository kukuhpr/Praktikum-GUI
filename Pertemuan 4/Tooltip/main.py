import sys

from PyQt5.QtWidgets import QApplication

from ToolTip import*

if __name__ == '__main__':
    a = QApplication(sys.argv)
    form = ToolTip()
    form.show()
    a.exec_()
