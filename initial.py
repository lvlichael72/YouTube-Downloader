import sys
from PySide2 import QtWidgets
from pythonGenui import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.connectMe()
        self.setWindowTitle("Hello World from Badprog :D")
        #self.setFixedWidth(500)
        #self.setFixedHeight(500)
    def connectMe(self):
        self.pushButton.clicked.connect(self.slotButton)

    def slotButton(self):
        self.label.setText("fuck :D ")

if (__name__ == '__main__'):
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())