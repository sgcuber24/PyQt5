# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 19:09:10 2018

@author: G Sriram
"""
import os
import sys
from PyQt5 import QtWidgets, QtGui 
class Notepad(QtWidgets.QWidget):
  def __init__(self):
    super(Notepad, self).__init__()
    self.text=QtWidgets.QTextEdit(self)
    self.init_ui()
    
  def init_ui(self):
    v_box=QtWidgets.QVBoxLayout()
    v_box.addWidget(self.text)
    self.setLayout(v_box)
    self.setWindowTitle("Text Editor")
  def save_text(self):
    filename=QtWidgets.QFileDialog.getSaveFileName(self,'Save File', os.getenv('HOME'))
    f=open((filename[0]),'a')
    mytext=self.text.toPlainText()
    f.write(mytext)
    f.close()
  def clear_text(self):
    self.text.clear()
  def opn_text(self):
    filename=QtWidgets.QFileDialog.getOpenFileName(self,'Open File', os.getenv('HOME'))
    f=open((filename[0]), 'r')
    mytext=f.read()
    self.text.setText(mytext)

class Writer(QtWidgets.QMainWindow):
  def __init__(self):
    super().__init__()
    self.form_widget=Notepad()
    self.setCentralWidget(self.form_widget)
    self.init_ui()
  def init_ui(self):
    bar=self.menuBar()
    file=bar.addMenu('File')
    new_action=QtWidgets.QAction('New',self)
    new_action.setShortcut('Ctrl+N')
    save_action=QtWidgets.QAction('Save', self)
    save_action.setShortcut('Ctrl+S')
    open_action=QtWidgets.QAction('Open',self)
    open_action.setShortcut('Ctrl+O')
    quit_action=QtWidgets.QAction('Quit', self)
    quit_action.setShortcut('Ctrl+Q')
    file.addAction(new_action)
    file.addAction(save_action)
    file.addAction(open_action)
    file.addAction(quit_action)
    quit_action.triggered.connect(self.quit_trigger)
    file.triggered.connect(self.respond)
    self.setWindowTitle('Text Editor')
    self.show()
  def quit_trigger(self):
    QtWidgets.qApp.quit()    
  def respond(self, q):
    signal=q.text()
    if(signal=='New'):
      self.form_widget.clear_text()
    elif(signal=='Open'):
      self.form_widget.opn_text()
    elif(signal=='Save'):
      self.form_widget.save_text()
app=QtWidgets.QApplication(sys.argv)

w=Writer()

sys.exit(app.exec_())