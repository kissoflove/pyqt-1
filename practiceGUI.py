import sys
from PyQt4 import QtGui

def window():
	app = QtGui.QApplication(sys.argv)
	window = QtGui.QWidget()
	label = QtGui.QLabel(window)
	label.setText('Hello World')
	window.setGeometry(100,100,200,50)
	label.move(50,20)
	window.setWindowTitle("First Gui (PyQt4)")
	window.show()
	sys.exit(app.exec_())

if __name__=='__main__':
	window()
