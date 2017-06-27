import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

def window():
   app = QApplication(sys.argv)
   win = QWidget()
	
   b1 = QPushButton("Button1")
   b1.clicked.connect(b1_event)
   
   b2 = QPushButton("Button2")
   b2.clicked.connect(b2_event)
   
   vbox = QVBoxLayout()
   vbox.addWidget(b1)
   vbox.addStretch()
   vbox.addWidget(b2)
   win.setLayout(vbox)

   win.setWindowTitle("PyQt")
   win.show()
   sys.exit(app.exec_())

def b1_event():
   print("Button 1 clicked")

def b2_event():
   print("Button 2 clicked")

if __name__ == '__main__':
   window()