import sys
#from PySide2.QtUiTools import QUiLoader
from PySide2 import QtUiTools
#from PySide2.QtWidgets import QApplication
#from PySide2.QtCore import QFile
from PySide2 import QtCore , QtWidgets


if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    app = QtWidgets.QApplication(sys.argv)

    ui_file = QtCore.QFile("un.ui")
    ui_file.open(QtCore.QFile.ReadOnly)

    loader = QtUiTools.QUiLoader()
    window = loader.load(ui_file)
    ui_file.close()
    window.show()
    
    sys.exit(app.exec_())