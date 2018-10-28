# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 20:28:48 2018

@author: G Sriram
"""
from PyQt5 import QtCore, QtGui, QtWidgets
from add import Ui_Form
from search import Ui_display
from modify import Ui_modify
from delete import Ui_delete_2
class Ui_MainWindow(object):
    def openDelete(self):
        self.window3=QtWidgets.QWidget()
        self.ui3=Ui_delete_2()
        self.ui3.setupUi(self.window3)
        self.window3.show()
    def openModify(self):
      self.window2=QtWidgets.QWidget()
      self.ui2=Ui_modify()
      self.ui2.setupUi(self.window2)
      self.window2.show()
    def openSearch(self):
      self.window1=QtWidgets.QWidget()
      self.ui1=Ui_display()
      self.ui1.setupUi(self.window1)
      self.window1.show()
    def openAdd(self):
      self.window=QtWidgets.QWidget()
      self.ui=Ui_Form()
      self.ui.setupUi(self.window)
      self.window.show()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(842, 592)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 842, 26))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAdd = QtWidgets.QAction(MainWindow)
        self.actionAdd.setObjectName("actionAdd")
        self.actionSearch = QtWidgets.QAction(MainWindow)
        self.actionSearch.setObjectName("actionSearch")
        self.actionModify = QtWidgets.QAction(MainWindow)
        self.actionModify.setObjectName("actionModify")
        self.actionDelete = QtWidgets.QAction(MainWindow)
        self.actionDelete.setObjectName("actionDelete")
        self.menuMenu.addAction(self.actionAdd)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionSearch)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionModify)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionDelete)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.actionAdd.triggered.connect(self.openAdd)
        self.actionSearch.triggered.connect(self.openSearch)
        self.actionModify.triggered.connect(self.openModify)
        self.actionDelete.triggered.connect(self.openDelete)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Index"))
        self.label.setText(_translate("MainWindow", "WELCOME"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionAdd.setText(_translate("MainWindow", "Add"))
        self.actionAdd.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionSearch.setShortcut(_translate("MainWindow", "Ctrl+F"))
        self.actionModify.setShortcut(_translate("MainWindow", "Ctrl+H"))
        self.actionDelete.setShortcut(_translate("MainWindow", "Ctrl+D"))
        self.actionSearch.setText(_translate("MainWindow", "Search"))
        self.actionModify.setText(_translate("MainWindow", "Modify"))
        self.actionDelete.setText(_translate("MainWindow", "Delete"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

