# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calc.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 600)
        MainWindow.setMinimumSize(QtCore.QSize(400, 600))
        MainWindow.setMaximumSize(QtCore.QSize(400, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(40, 40))
        self.frame.setStyleSheet("background-color: rgb(60, 60, 60);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setContentsMargins(5, 0, 5, 0)
        self.gridLayout_2.setHorizontalSpacing(5)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btn_close = QtWidgets.QPushButton(self.frame)
        self.btn_close.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_close.setMaximumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono SemiLight")
        font.setPointSize(12)
        self.btn_close.setFont(font)
        self.btn_close.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"")
        self.btn_close.setObjectName("btn_close")
        self.gridLayout_2.addWidget(self.btn_close, 6, 3, 1, 1)
        self.btn_dot = QtWidgets.QPushButton(self.frame)
        self.btn_dot.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_dot.setMaximumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono SemiLight")
        font.setPointSize(12)
        self.btn_dot.setFont(font)
        self.btn_dot.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"")
        self.btn_dot.setObjectName("btn_dot")
        self.gridLayout_2.addWidget(self.btn_dot, 6, 1, 1, 1)
        self.btn_5 = QtWidgets.QPushButton(self.frame)
        self.btn_5.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_5.setMaximumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono SemiLight")
        font.setPointSize(12)
        self.btn_5.setFont(font)
        self.btn_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"")
        self.btn_5.setObjectName("btn_5")
        self.gridLayout_2.addWidget(self.btn_5, 4, 1, 1, 1)
        self.btn_9 = QtWidgets.QPushButton(self.frame)
        self.btn_9.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_9.setMaximumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono SemiLight")
        font.setPointSize(12)
        self.btn_9.setFont(font)
        self.btn_9.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"")
        self.btn_9.setObjectName("btn_9")
        self.gridLayout_2.addWidget(self.btn_9, 3, 2, 1, 1)
        self.btn_dell = QtWidgets.QPushButton(self.frame)
        self.btn_dell.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_dell.setMaximumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono SemiLight")
        font.setPointSize(12)
        self.btn_dell.setFont(font)
        self.btn_dell.setStyleSheet("background-color: rgb(255, 65, 77);\n"
"\n"
"")
        self.btn_dell.setObjectName("btn_dell")
        self.gridLayout_2.addWidget(self.btn_dell, 3, 3, 1, 1)
        self.btn_clear = QtWidgets.QPushButton(self.frame)
        self.btn_clear.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_clear.setMaximumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono SemiLight")
        font.setPointSize(12)
        self.btn_clear.setFont(font)
        self.btn_clear.setStyleSheet("background-color: rgb(255, 65, 77);\n"
"")
        self.btn_clear.setObjectName("btn_clear")
        self.gridLayout_2.addWidget(self.btn_clear, 3, 4, 1, 1)
        self.btn_6 = QtWidgets.QPushButton(self.frame)
        self.btn_6.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_6.setMaximumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono SemiLight")
        font.setPointSize(12)
        self.btn_6.setFont(font)
        self.btn_6.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"")
        self.btn_6.setObjectName("btn_6")
        self.gridLayout_2.addWidget(self.btn_6, 4, 2, 1, 1)
        self.btn_mult = QtWidgets.QPushButton(self.frame)
        self.btn_mult.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_mult.setMaximumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono SemiLight")
        font.setPointSize(12)
        self.btn_mult.setFont(font)
        self.btn_mult.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"")
        self.btn_mult.setObjectName("btn_mult")
        self.gridLayout_2.addWidget(self.btn_mult, 4, 3, 1, 1)
        self.btn_div = QtWidgets.QPushButton(self.frame)
        self.btn_div.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_div.setMaximumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono SemiLight")
        font.setPointSize(12)
        self.btn_div.setFont(font)
        self.btn_div.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"")
        self.btn_div.setObjectName("btn_div")
        self.gridLayout_2.addWidget(self.btn_div, 4, 4, 1, 1)
        self.btn_1 = QtWidgets.QPushButton(self.frame)
        self.btn_1.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_1.setMaximumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono SemiLight")
        font.setPointSize(12)
        self.btn_1.setFont(font)
        self.btn_1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"")
        self.btn_1.setObjectName("btn_1")
        self.gridLayout_2.addWidget(self.btn_1, 5, 0, 1, 1)
        self.btn_8 = QtWidgets.QPushButton(self.frame)
        self.btn_8.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_8.setMaximumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono SemiLight")
        font.setPointSize(12)
        self.btn_8.setFont(font)
        self.btn_8.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"")
        self.btn_8.setObjectName("btn_8")
        self.gridLayout_2.addWidget(self.btn_8, 3, 1, 1, 1)
        self.btn_min = QtWidgets.QPushButton(self.frame)
        self.btn_min.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_min.setMaximumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono SemiLight")
        font.setPointSize(12)
        self.btn_min.setFont(font)
        self.btn_min.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"")
        self.btn_min.setObjectName("btn_min")
        self.gridLayout_2.addWidget(self.btn_min, 5, 4, 1, 1)
        self.btn_3 = QtWidgets.QPushButton(self.frame)
        self.btn_3.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_3.setMaximumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono SemiLight")
        font.setPointSize(12)
        self.btn_3.setFont(font)
        self.btn_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"")
        self.btn_3.setObjectName("btn_3")
        self.gridLayout_2.addWidget(self.btn_3, 5, 2, 1, 1)
        self.btn_2 = QtWidgets.QPushButton(self.frame)
        self.btn_2.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_2.setMaximumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono SemiLight")
        font.setPointSize(12)
        self.btn_2.setFont(font)
        self.btn_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"")
        self.btn_2.setObjectName("btn_2")
        self.gridLayout_2.addWidget(self.btn_2, 5, 1, 1, 1)
        self.btn_0 = QtWidgets.QPushButton(self.frame)
        self.btn_0.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_0.setMaximumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono SemiLight")
        font.setPointSize(12)
        self.btn_0.setFont(font)
        self.btn_0.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"")
        self.btn_0.setObjectName("btn_0")
        self.gridLayout_2.addWidget(self.btn_0, 6, 0, 1, 1)
        self.btn_plus = QtWidgets.QPushButton(self.frame)
        self.btn_plus.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_plus.setMaximumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono SemiLight")
        font.setPointSize(12)
        self.btn_plus.setFont(font)
        self.btn_plus.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"")
        self.btn_plus.setObjectName("btn_plus")
        self.gridLayout_2.addWidget(self.btn_plus, 5, 3, 1, 1)
        self.btn_7 = QtWidgets.QPushButton(self.frame)
        self.btn_7.setMinimumSize(QtCore.QSize(40, 40))
        self.btn_7.setMaximumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono SemiLight")
        font.setPointSize(12)
        self.btn_7.setFont(font)
        self.btn_7.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"")
        self.btn_7.setObjectName("btn_7")
        self.gridLayout_2.addWidget(self.btn_7, 3, 0, 1, 1)
        self.btn_4 = QtWidgets.QPushButton(self.frame)
        self.btn_4.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_4.setMaximumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono SemiLight")
        font.setPointSize(12)
        self.btn_4.setFont(font)
        self.btn_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"")
        self.btn_4.setObjectName("btn_4")
        self.gridLayout_2.addWidget(self.btn_4, 4, 0, 1, 1)
        self.btn_open = QtWidgets.QPushButton(self.frame)
        self.btn_open.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_open.setMaximumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono SemiLight")
        font.setPointSize(12)
        self.btn_open.setFont(font)
        self.btn_open.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"")
        self.btn_open.setObjectName("btn_open")
        self.gridLayout_2.addWidget(self.btn_open, 6, 2, 1, 1)
        self.display = QtWidgets.QLabel(self.frame)
        self.display.setMinimumSize(QtCore.QSize(50, 80))
        self.display.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.display.setFont(font)
        self.display.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.display.setFrameShape(QtWidgets.QFrame.Box)
        self.display.setFrameShadow(QtWidgets.QFrame.Raised)
        self.display.setText("")
        self.display.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.display.setObjectName("display")
        self.gridLayout_2.addWidget(self.display, 0, 0, 1, 5)
        self.btn_eq = QtWidgets.QPushButton(self.frame)
        self.btn_eq.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_eq.setMaximumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono SemiLight")
        font.setPointSize(12)
        self.btn_eq.setFont(font)
        self.btn_eq.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"")
        self.btn_eq.setObjectName("btn_eq")
        self.gridLayout_2.addWidget(self.btn_eq, 6, 4, 1, 1)
        self.btn_sin = QtWidgets.QPushButton(self.frame)
        self.btn_sin.setMinimumSize(QtCore.QSize(40, 40))
        self.btn_sin.setMaximumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono SemiLight")
        font.setPointSize(12)
        self.btn_sin.setFont(font)
        self.btn_sin.setStyleSheet("background-color: rgb(197, 197, 197);\n"
"\n"
"")
        self.btn_sin.setObjectName("btn_sin")
        self.gridLayout_2.addWidget(self.btn_sin, 2, 0, 1, 1)
        self.btn_tan = QtWidgets.QPushButton(self.frame)
        self.btn_tan.setMinimumSize(QtCore.QSize(40, 40))
        self.btn_tan.setMaximumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono SemiLight")
        font.setPointSize(12)
        self.btn_tan.setFont(font)
        self.btn_tan.setStyleSheet("background-color: rgb(197, 197, 197);\n"
"\n"
"")
        self.btn_tan.setObjectName("btn_tan")
        self.gridLayout_2.addWidget(self.btn_tan, 2, 2, 1, 1)
        self.btn_cos = QtWidgets.QPushButton(self.frame)
        self.btn_cos.setMinimumSize(QtCore.QSize(40, 40))
        self.btn_cos.setMaximumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono SemiLight")
        font.setPointSize(12)
        self.btn_cos.setFont(font)
        self.btn_cos.setStyleSheet("background-color: rgb(197, 197, 197);\n"
"\n"
"")
        self.btn_cos.setObjectName("btn_cos")
        self.gridLayout_2.addWidget(self.btn_cos, 2, 1, 1, 1)
        self.btn_cub = QtWidgets.QPushButton(self.frame)
        self.btn_cub.setMinimumSize(QtCore.QSize(40, 40))
        self.btn_cub.setMaximumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono SemiLight")
        font.setPointSize(12)
        self.btn_cub.setFont(font)
        self.btn_cub.setMouseTracking(False)
        self.btn_cub.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btn_cub.setAutoFillBackground(False)
        self.btn_cub.setStyleSheet("background-color: rgb(197, 197, 197);\n"
"")
        self.btn_cub.setCheckable(False)
        self.btn_cub.setFlat(False)
        self.btn_cub.setObjectName("btn_cub")
        self.gridLayout_2.addWidget(self.btn_cub, 2, 4, 1, 1)
        self.btn_squared = QtWidgets.QPushButton(self.frame)
        self.btn_squared.setMinimumSize(QtCore.QSize(40, 40))
        self.btn_squared.setMaximumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono SemiLight")
        font.setPointSize(12)
        self.btn_squared.setFont(font)
        self.btn_squared.setStyleSheet("background-color: rgb(197, 197, 197);\n"
"\n"
"")
        self.btn_squared.setObjectName("btn_squared")
        self.gridLayout_2.addWidget(self.btn_squared, 2, 3, 1, 1)
        self.btn_log = QtWidgets.QPushButton(self.frame)
        self.btn_log.setMinimumSize(QtCore.QSize(40, 40))
        self.btn_log.setMaximumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono SemiLight")
        font.setPointSize(12)
        self.btn_log.setFont(font)
        self.btn_log.setStyleSheet("background-color: rgb(197, 197, 197);\n"
"\n"
"")
        self.btn_log.setObjectName("btn_log")
        self.gridLayout_2.addWidget(self.btn_log, 1, 1, 1, 1)
        self.btn_sqrt = QtWidgets.QPushButton(self.frame)
        self.btn_sqrt.setMinimumSize(QtCore.QSize(40, 40))
        self.btn_sqrt.setMaximumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono SemiLight")
        font.setPointSize(12)
        self.btn_sqrt.setFont(font)
        self.btn_sqrt.setStyleSheet("background-color: rgb(197, 197, 197);\n"
"\n"
"")
        self.btn_sqrt.setObjectName("btn_sqrt")
        self.gridLayout_2.addWidget(self.btn_sqrt, 1, 0, 1, 1)
        self.btn_ln = QtWidgets.QPushButton(self.frame)
        self.btn_ln.setMinimumSize(QtCore.QSize(40, 40))
        self.btn_ln.setMaximumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono SemiLight")
        font.setPointSize(12)
        self.btn_ln.setFont(font)
        self.btn_ln.setStyleSheet("background-color: rgb(197, 197, 197);\n"
"\n"
"")
        self.btn_ln.setObjectName("btn_ln")
        self.gridLayout_2.addWidget(self.btn_ln, 1, 2, 1, 1)
        self.btn_fact = QtWidgets.QPushButton(self.frame)
        self.btn_fact.setMinimumSize(QtCore.QSize(40, 40))
        self.btn_fact.setMaximumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono SemiLight")
        font.setPointSize(12)
        self.btn_fact.setFont(font)
        self.btn_fact.setStyleSheet("background-color: rgb(197, 197, 197);\n"
"\n"
"")
        self.btn_fact.setObjectName("btn_fact")
        self.gridLayout_2.addWidget(self.btn_fact, 1, 3, 1, 1)
        self.btn_pi = QtWidgets.QPushButton(self.frame)
        self.btn_pi.setMinimumSize(QtCore.QSize(40, 40))
        self.btn_pi.setMaximumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono SemiLight")
        font.setPointSize(12)
        self.btn_pi.setFont(font)
        self.btn_pi.setStyleSheet("background-color: rgb(197, 197, 197);\n"
"\n"
"")
        self.btn_pi.setObjectName("btn_pi")
        self.gridLayout_2.addWidget(self.btn_pi, 1, 4, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Basic Calculator"))
        self.btn_close.setText(_translate("MainWindow", ")"))
        self.btn_dot.setText(_translate("MainWindow", "."))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_dell.setText(_translate("MainWindow", "DEL"))
        self.btn_clear.setText(_translate("MainWindow", "AC"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_mult.setText(_translate("MainWindow", "X"))
        self.btn_div.setText(_translate("MainWindow", "/"))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.btn_min.setText(_translate("MainWindow", "-"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_0.setText(_translate("MainWindow", "0"))
        self.btn_plus.setText(_translate("MainWindow", "+"))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_open.setText(_translate("MainWindow", "("))
        self.btn_eq.setText(_translate("MainWindow", "="))
        self.btn_sin.setText(_translate("MainWindow", "sin"))
        self.btn_tan.setText(_translate("MainWindow", "tan"))
        self.btn_cos.setText(_translate("MainWindow", "cos"))
        self.btn_cub.setText(_translate("MainWindow", "x³"))
        self.btn_squared.setText(_translate("MainWindow", "x²"))
        self.btn_log.setText(_translate("MainWindow", "log"))
        self.btn_sqrt.setText(_translate("MainWindow", "sqrt()"))
        self.btn_ln.setText(_translate("MainWindow", "ln"))
        self.btn_fact.setText(_translate("MainWindow", "!"))
        self.btn_pi.setText(_translate("MainWindow", "PI"))