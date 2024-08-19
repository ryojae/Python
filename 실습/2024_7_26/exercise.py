# #no.1
# import turtle as t
# t.shape('turtle')
# n=6
# t.color('red')
# t.begin_fill()
# for i in range(n):
#     t.forward(100)
#     t.right(360/n)
# t.end_fill()

# #no.2
# import sys 
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *
# def window():
#     app = QApplication(sys.argv)
#     w=QWidget()
#     b=QLabel(w)
#     b.setText('Hello World')
#     w.setGeometry(100,100,200,50)
#     b.move(50,20)
#     w.setWindowTitle('PyQt5')
#     w.show()
#     sys.exit(app.exec())

# if __name__=='__main__':
#     window()

# #no.3
# import sys
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *
# class window(QWidget):
#     def __init__(self, parent = None):
#         super(window,self).__init__(parent)
#         self.resize(200,50)
#         self.setWindowTitle('PyQt5')
#         self.label = QLabel(self)
#         self.label.setText('Hello World')
#         font = QFont()
#         font.setFamily('Arial')
#         font.setPointSize(16)
#         self.label.setFont(font)
#         self.label.move(50,20)
# def main():
#     app = QApplication(sys.argv)
#     ex = window()
#     ex.show()
#     sys.exit(app.exec_())
# if __name__=='__main__':
#     main()

# #no.5
# import sys
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *
# def window():
#     app = QApplication(sys.argv)
#     win = QDialog()
#     b1 = QPushButton(win)
#     b1.setText("Button1")
#     b1.move(50,20)
#     b1.clicked.connect(b1_clicked)
#     b2 = QPushButton(win)
#     b2.setText("Button2")
#     b2.move(50,50)
#     b2.clicked.connect(b2_clicked)
#     win.setGeometry(120,300,200,100)
#     win.setWindowTitle("PyQt5")
#     win.show()
#     sys.exit(app.exec_())
# def b1_clicked():
#     print ("Button 1 clicked")
# def b2_clicked():
#     print ("Button 2 clicked")
# if __name__ == '__main__':
#     window()

# #no.6
# import sys
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *
# def window():
#     app = QApplication(sys.argv)
#     win = QWidget()
#     b1 = QPushButton("Button1")
#     b2 = QPushButton("Button2")
#     vbox = QVBoxLayout()
#     vbox.addWidget(b1)
#     vbox.addStretch()
#     vbox.addWidget(b2)
#     hbox = QHBoxLayout()
#     b3 = QPushButton("Button3")
#     b4 = QPushButton("Button4")
#     hbox.addWidget(b3)
#     hbox.addStretch()
#     hbox.addWidget(b4)
#     vbox.addStretch()
#     vbox.addLayout(hbox)
#     win.setLayout(vbox)
#     win.setWindowTitle("PyQt")
#     win.show()
#     sys.exit(app.exec_())
# if __name__ == '__main__':
#     window()

# #no.7
# import sys
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *
# def window():
#     app = QApplication(sys.argv)
#     win = QWidget()
#     grid = QGridLayout()    
#     for i in range(1,7):
#         for j in range(1,5):
#             grid.addWidget(QPushButton("B"+str(i)+str(j)),i,j)  
#     win.setLayout(grid)
#     win.setGeometry(100,100,200,100)
#     win.setWindowTitle("PyQt Grid Layout")
#     win.show()
#     sys.exit(app.exec_())
# if __name__ == '__main__':
#  window()

# #no.8
# import sys
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *
# def window():
#  app = QApplication(sys.argv)
#  win = QWidget()
#  l1 = QLabel("Name")
#  nm = QLineEdit()

#  l2 = QLabel("Address")
#  add1 = QLineEdit()
#  add2 = QLineEdit()
#  fbox = QFormLayout()
#  fbox.addRow(l1,nm)
#  vbox = QVBoxLayout()

#  vbox.addWidget(add1)
#  vbox.addWidget(add2)
#  fbox.addRow(l2,vbox)
#  hbox = QHBoxLayout()

#  r1 = QRadioButton("Male")
#  r2 = QRadioButton("Female")
#  hbox.addWidget(r1)
#  hbox.addWidget(r2)
#  hbox.addStretch()
#  fbox.addRow(QLabel("sex"),hbox)
#  fbox.addRow(QPushButton("Submit"),QPushButton("Cancel"))

#  win.setLayout(fbox)

#  win.setWindowTitle("PyQt5 Form Layout")
#  win.show()
#  sys.exit(app.exec_())
# if __name__ == '__main__':
#  window()

# #no.9
# import sys
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *
# def window():
#  app = QApplication(sys.argv)
#  win = QWidget()

#  e1 = QLineEdit()
#  e1.setValidator(QIntValidator())
#  e1.setMaxLength(4)
#  e1.setAlignment(Qt.AlignRight)
#  e1.setFont(QFont("Arial",20))

#  e2 = QLineEdit()
#  e2.setValidator(QDoubleValidator(0.99,99.99,2))

#  flo = QFormLayout()
#  flo.addRow("integer validator", e1)
#  flo.addRow("Double validator",e2)

#  e3 = QLineEdit()
#  e3.setInputMask('+99_9999_999999')
#  flo.addRow("Input Mask",e3)
 

#  e4 = QLineEdit()
#  e4.textChanged.connect(textchanged)
#  flo.addRow("Text changed",e4)

#  e5 = QLineEdit()
#  e5.setEchoMode(QLineEdit.Password)
#  flo.addRow("Password",e5)

#  e6 = QLineEdit("Hello Python")
#  e6.setReadOnly(True)
#  flo.addRow("Read Only",e6)

#  e5.editingFinished.connect(enterPress)
#  win.setLayout(flo)
#  win.setWindowTitle("PyQt")
#  win.show()

#  sys.exit(app.exec_())
# def textchanged(text):
#  print ("contents of text box: {}".format(text))

# def enterPress():
#  print ("editeing finished")
# if __name__ == '__main__':
#  window()

# #no.10
# import turtle as t
# screen=t.Screen()
# screen.bgcolor('black')
# t.shape('turtle')
# color=['red','blue','green','purple','white']
# t.speed('slow')
# for i in range(5):
#     t.color(color[i])
#     t.forward(100)
#     t.right(144)
# t.hideturtle()
# screen.mainloop()

# #no.11
# import turtle
# screen = turtle.Screen()
# screen.bgcolor('black')
# t=turtle.Turtle()
# t.speed(9)
# color=['red','orange','yellow','green','blue','navy','purple']
# r=50
# for i in color:
#     t.color('black')
#     t.forward(r)
#     t.color(i)
#     t.left(90)
#     t.circle(r,180)
#     t.left(90)
#     t.color('black')
#     t.forward(r)
#     r+=50
# screen.mainloop()