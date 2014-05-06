import formula
from PyQt4 import QtCore, QtGui, uic
import sys
from main_window import main_window
import logic_manip

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = QtGui.QMainWindow()
    ui = main_window()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())



