# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gcode_modeling.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets,Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1264, 766)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.open_button = QtWidgets.QPushButton(self.frame)
        self.open_button.setObjectName("open_button")
        self.horizontalLayout.addWidget(self.open_button)
        self.save_button = QtWidgets.QPushButton(self.frame)
        self.save_button.setObjectName("save_button")
        self.horizontalLayout.addWidget(self.save_button)
        self.save_as_button = QtWidgets.QPushButton(self.frame)
        self.save_as_button.setObjectName("save_as_button")
        self.horizontalLayout.addWidget(self.save_as_button)
        self.verticalLayout.addLayout(self.horizontalLayout)


        self.editor = PlainTextEdit(self.frame)
        self.editor.setObjectName("editor")
        self.editor.setLineWrapMode(PlainTextEdit.LineWrapMode.NoWrap)
        self.verticalLayout.addWidget(self.editor)
        self.reload_button = QtWidgets.QPushButton(self.frame)
        self.reload_button.setObjectName("reload_button")
        self.verticalLayout.addWidget(self.reload_button)
        self.message_console = QtWidgets.QTextEdit(self.frame)
        self.message_console.setObjectName("message_console")
        self.verticalLayout.addWidget(self.message_console)
        self.verticalLayout.setStretch(1, 10)
        self.verticalLayout.setStretch(3, 1)
        self.horizontalLayout_2.addWidget(self.frame)
        self.graphicsView = opengl.GLViewWidget(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayout_2.addWidget(self.graphicsView)
        self.frame1 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame1.sizePolicy().hasHeightForWidth())
        self.frame1.setSizePolicy(sizePolicy)
        self.frame1.setObjectName("frame1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Slider = QtWidgets.QSlider(self.frame1)
        self.Slider.setOrientation(QtCore.Qt.Vertical)
        self.Slider.setObjectName("Slider")
        self.verticalLayout_3.addWidget(self.Slider)
        self.up_button = QtWidgets.QToolButton(self.frame1)
        self.up_button.setObjectName("up_button")
        self.verticalLayout_3.addWidget(self.up_button)
        self.down_button = QtWidgets.QToolButton(self.frame1)
        self.down_button.setObjectName("down_button")
        self.verticalLayout_3.addWidget(self.down_button)
        self.horizontalLayout_2.addWidget(self.frame1)
        self.frame2 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame2.sizePolicy().hasHeightForWidth())
        self.frame2.setSizePolicy(sizePolicy)
        self.frame2.setObjectName("frame2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.parameter_tree = ParameterTree(self.frame2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.parameter_tree.sizePolicy().hasHeightForWidth())
        self.parameter_tree.setSizePolicy(sizePolicy)
        self.parameter_tree.setMinimumSize(QtCore.QSize(250, 540))
        self.parameter_tree.setObjectName("parameter_tree")
        self.verticalLayout_2.addWidget(self.parameter_tree)
        self.gcode_export_button = QtWidgets.QPushButton(self.frame2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gcode_export_button.sizePolicy().hasHeightForWidth())
        self.gcode_export_button.setSizePolicy(sizePolicy)
        self.gcode_export_button.setObjectName("gcode_export_button")
        self.verticalLayout_2.addWidget(self.gcode_export_button)
        self.horizontalLayout_2.addWidget(self.frame2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1264, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QtWidgets.QToolBar(MainWindow)
        self.toolBar_2.setObjectName("toolBar_2")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_2)

        self.retranslateUi(MainWindow)
        self.open_button.pressed.connect(MainWindow.file_open) # type: ignore
        self.save_button.pressed.connect(MainWindow.file_save) # type: ignore
        self.save_as_button.pressed.connect(MainWindow.file_save_as) # type: ignore
        self.reload_button.pressed.connect(MainWindow.save_as_modeling) # type: ignore
        self.reload_button.pressed.connect(MainWindow.draw_updated_object) # type: ignore
        self.gcode_export_button.pressed.connect(MainWindow.Gcode_create) # type: ignore
        self.Slider.valueChanged['int'].connect(MainWindow.redraw_object) # type: ignore
        self.up_button.pressed.connect(MainWindow.up_button_pressed) # type: ignore
        self.down_button.pressed.connect(MainWindow.down_button_pressed) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.open_button.setText(_translate("MainWindow", "       Open File       "))
        self.save_button.setText(_translate("MainWindow", "Save"))
        self.save_as_button.setText(_translate("MainWindow", "Save As"))
        self.reload_button.setText(_translate("MainWindow", "reload"))
        self.up_button.setText(_translate("MainWindow", "..."))
        self.down_button.setText(_translate("MainWindow", "..."))
        self.gcode_export_button.setText(_translate("MainWindow", "Gcode Export"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.toolBar_2.setWindowTitle(_translate("MainWindow", "toolBar_2"))

class PlainTextEdit(QPlainTextEdit):
    def keyPressEvent(self, event):
        #オートインデントの処理
        if event.key() in (Qt.Key_Return, Qt.Key_Enter):

            indent_width = 4
            line_number = self.textCursor().blockNumber()
            #print(line_number)
            line_text = self.document().findBlockByLineNumber(line_number).text()
            indent_level = line_text.count(" " * indent_width)
            if line_text.endswith(":"):
                indent_level += 1
            self.insertPlainText("\n")
            self.insertPlainText( " " * indent_width * indent_level)


            return
        super(PlainTextEdit, self).keyPressEvent(event)

from pyqtgraph import opengl
from pyqtgraph.parametertree import ParameterTree
