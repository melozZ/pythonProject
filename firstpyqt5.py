import sys
from PyQt5.QtWidgets import QApplication,QWidget

if __name__ == '__main__':
	app=QApplication(sys.argv)
	windows=QWidget()
	windows.resize(400,300)
	windows.setWindowTitle("PYQT第一课")
	windows.show()
	sys.exit(app.exec_())