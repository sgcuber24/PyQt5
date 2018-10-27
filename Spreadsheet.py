# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 16:17:12 2018

@author: G Sriram
"""
import os
import csv
import sys
from PyQt5 import QtWidgets
class MyTable(QtWidgets.QTableWidget):
  def __init__(self, r, c):
    super().__init__(r,c)
    self.check_change=True
    self.init_ui()
  def init_ui(self):
    self.show()
  def open_sheet(self):
    self.check_change=False
    path=QtWidgets.QFileDialog.getOpenFileName(self, 'Open CSV', os.getenv('HOME'), 'CSV(*.csv)')
    if(path[0]!=''):
      with open(path[0], newline='') as csv_file:
        self.setRowCount(0)
        self.setColumnCount(10)
        myfile=csv.reader(csv_file, delimiter=',', quotechar='|')
        for row_data in myfile:
          row=self.rowCount()
          self.insertRow(row)
          if(len(row_data)>10):
            self.setColumnCount(len(row_data))
          for column, stuff in enumerate(row_data):
            item=QtWidgets.QTableWidgetItem(stuff)
            self.setItem(row,column,item)
  def save_sheet(self):
    path=QtWidgets.QFileDialog.getSaveFileName(self, 'Save CSV', os.getenv('HOME'), 'CSV(*.csv)')
    if(path[0]!=''):
      with open(path[0], 'w') as csv_file:
        writer=csv.writer(csv_file, dialect='excel')
        for row in range(self.rowCount()):
          row_data=[]
          for column in range(self.columnCount()):
            item=self.item(row,column)
            if(item is not None):
              row_data.append(item.text())
            else:
              row_data.append('')
          writer.writerow(row_data)
  
          
class Sheet(QtWidgets.QMainWindow):
  def __init__(self):
    super().__init__()
    self.form_widget=MyTable(10,10)
    self.setCentralWidget(self.form_widget)
    col_headers=['A','B','C','D','E','F','G','H','I','J']
    self.form_widget.setHorizontalHeaderLabels(col_headers)
    bar=self.menuBar()
    file=bar.addMenu('File')
    save_action=QtWidgets.QAction('Save', self)
    save_action.setShortcut('Ctrl+S')
    open_action=QtWidgets.QAction('Open',self)
    open_action.setShortcut('Ctrl+O')
    quit_action=QtWidgets.QAction('Quit', self)
    quit_action.setShortcut('Ctrl+Q')
    file.addAction(save_action)
    file.addAction(open_action)
    file.addAction(quit_action)
    quit_action.triggered.connect(self.quit_trigger)
    save_action.triggered.connect(self.form_widget.save_sheet)
    open_action.triggered.connect(self.form_widget.open_sheet)
    self.setWindowTitle('Spreadsheet')
    self.show()
  def quit_trigger(self):
    QtWidgets.qApp.quit()
app=QtWidgets.QApplication(sys.argv)
sheet=Sheet()
sys.exit(app.exec_())


    
    
