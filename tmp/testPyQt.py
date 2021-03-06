import sys
# from PyQt5.QtCore import Qt, QSize
# from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QToolBar, QAction, QCheckBox, QStatusBar
# from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Window(QMainWindow): 
    def __init__(self): 
        super().__init__() 
  
        # setting title 
        self.setWindowTitle("Python ") 
  
        # setting geometry left, top, width, height
        self.setGeometry(1000, 100, 600, 400) 
  
        # calling method 
        self.UiComponents() 
  
        # showing all the widgets 
        self.show() 
  
    # method for widgets 
    def UiComponents(self): 
  
        # creating a push button 
        button = QPushButton(self) 
        # button = QPushButton("CLICK", self) 
  
        # setting geometry of button 
        button.setGeometry(200, 150, 100, 100) 
  
        # adding action to a button 
        button.clicked.connect(self.clickme) 
  
        button:pressed
        # setting image to the button 
        button.setStyleSheet("border-image : url(images/dice4.png);")

        button.setCheckable(True)
  
  
    # action method 
    def clickme(self): 
  
        # printing pressed 
        print("pressed")
        bt.setStyleSheet("border-image : url(images/dice1.png);")

  
# create pyqt5 app 
App = QApplication(sys.argv) 
  
# create the instance of our Window 
window = Window() 
  
# start the app 
sys.exit(App.exec()) 