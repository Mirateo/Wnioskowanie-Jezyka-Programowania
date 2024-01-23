# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'exp.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSlider,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(810, 612)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.centralwidget.setAutoFillBackground(True)
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(-10, 30, 821, 20))
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy1)
        self.label_10.setMouseTracking(False)
        self.label_10.setLayoutDirection(Qt.LeftToRight)
        self.label_10.setAutoFillBackground(True)
        self.label_10.setLocale(QLocale(QLocale.Polish, QLocale.Poland))
        self.label_10.setFrameShape(QFrame.Box)
        self.label_10.setFrameShadow(QFrame.Plain)
        self.label_10.setTextFormat(Qt.AutoText)
        self.label_10.setScaledContents(False)
        self.label_10.setAlignment(Qt.AlignCenter)
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(0, 0, 831, 31))
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy2)
        self.label_9.setMouseTracking(False)
        self.label_9.setLayoutDirection(Qt.LeftToRight)
        self.label_9.setAutoFillBackground(True)
        self.label_9.setLocale(QLocale(QLocale.Polish, QLocale.Poland))
        self.label_9.setFrameShape(QFrame.Box)
        self.label_9.setFrameShadow(QFrame.Plain)
        self.label_9.setTextFormat(Qt.AutoText)
        self.label_9.setScaledContents(False)
        self.label_9.setAlignment(Qt.AlignCenter)
        self.formLayoutWidget = QWidget(self.centralwidget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(20, 60, 661, 511))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.pythonSlider = QSlider(self.formLayoutWidget)
        self.pythonSlider.setObjectName(u"pythonSlider")
        sizePolicy3 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pythonSlider.sizePolicy().hasHeightForWidth())
        self.pythonSlider.setSizePolicy(sizePolicy3)
        self.pythonSlider.setMaximumSize(QSize(16777215, 15))
        self.pythonSlider.setMaximum(100)
        self.pythonSlider.setOrientation(Qt.Horizontal)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.pythonSlider)

        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.cSlider = QSlider(self.formLayoutWidget)
        self.cSlider.setObjectName(u"cSlider")
        sizePolicy3.setHeightForWidth(self.cSlider.sizePolicy().hasHeightForWidth())
        self.cSlider.setSizePolicy(sizePolicy3)
        self.cSlider.setMaximumSize(QSize(16777215, 15))
        self.cSlider.setMaximum(100)
        self.cSlider.setOrientation(Qt.Horizontal)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.cSlider)

        self.label_3 = QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.cppSlider = QSlider(self.formLayoutWidget)
        self.cppSlider.setObjectName(u"cppSlider")
        sizePolicy3.setHeightForWidth(self.cppSlider.sizePolicy().hasHeightForWidth())
        self.cppSlider.setSizePolicy(sizePolicy3)
        self.cppSlider.setMaximumSize(QSize(16777215, 15))
        self.cppSlider.setMaximum(100)
        self.cppSlider.setOrientation(Qt.Horizontal)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.cppSlider)

        self.label_5 = QLabel(self.formLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_5)

        self.csSlider = QSlider(self.formLayoutWidget)
        self.csSlider.setObjectName(u"csSlider")
        sizePolicy3.setHeightForWidth(self.csSlider.sizePolicy().hasHeightForWidth())
        self.csSlider.setSizePolicy(sizePolicy3)
        self.csSlider.setMaximumSize(QSize(16777215, 15))
        self.csSlider.setMaximum(100)
        self.csSlider.setOrientation(Qt.Horizontal)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.csSlider)

        self.label_6 = QLabel(self.formLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_6)

        self.javaSlider = QSlider(self.formLayoutWidget)
        self.javaSlider.setObjectName(u"javaSlider")
        sizePolicy3.setHeightForWidth(self.javaSlider.sizePolicy().hasHeightForWidth())
        self.javaSlider.setSizePolicy(sizePolicy3)
        self.javaSlider.setMaximumSize(QSize(16777215, 15))
        self.javaSlider.setMaximum(100)
        self.javaSlider.setOrientation(Qt.Horizontal)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.javaSlider)

        self.label_7 = QLabel(self.formLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_7)

        self.jsSlider = QSlider(self.formLayoutWidget)
        self.jsSlider.setObjectName(u"jsSlider")
        sizePolicy3.setHeightForWidth(self.jsSlider.sizePolicy().hasHeightForWidth())
        self.jsSlider.setSizePolicy(sizePolicy3)
        self.jsSlider.setMaximumSize(QSize(16777215, 15))
        self.jsSlider.setMaximum(100)
        self.jsSlider.setOrientation(Qt.Horizontal)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.jsSlider)

        self.label_8 = QLabel(self.formLayoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_8)

        self.phpSlider = QSlider(self.formLayoutWidget)
        self.phpSlider.setObjectName(u"phpSlider")
        sizePolicy3.setHeightForWidth(self.phpSlider.sizePolicy().hasHeightForWidth())
        self.phpSlider.setSizePolicy(sizePolicy3)
        self.phpSlider.setMaximumSize(QSize(16777215, 15))
        self.phpSlider.setMaximum(100)
        self.phpSlider.setOrientation(Qt.Horizontal)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.phpSlider)

        self.label_4 = QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_4)

        self.vbSlider = QSlider(self.formLayoutWidget)
        self.vbSlider.setObjectName(u"vbSlider")
        sizePolicy3.setHeightForWidth(self.vbSlider.sizePolicy().hasHeightForWidth())
        self.vbSlider.setSizePolicy(sizePolicy3)
        self.vbSlider.setMaximumSize(QSize(16777215, 15))
        self.vbSlider.setMaximum(100)
        self.vbSlider.setOrientation(Qt.Horizontal)

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.vbSlider)

        self.label_11 = QLabel(self.formLayoutWidget)
        self.label_11.setObjectName(u"label_11")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_11)

        self.scratchSlider = QSlider(self.formLayoutWidget)
        self.scratchSlider.setObjectName(u"scratchSlider")
        sizePolicy3.setHeightForWidth(self.scratchSlider.sizePolicy().hasHeightForWidth())
        self.scratchSlider.setSizePolicy(sizePolicy3)
        self.scratchSlider.setMaximumSize(QSize(16777215, 15))
        self.scratchSlider.setMaximum(100)
        self.scratchSlider.setOrientation(Qt.Horizontal)

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.scratchSlider)

        self.label_12 = QLabel(self.formLayoutWidget)
        self.label_12.setObjectName(u"label_12")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.label_12)

        self.sqlSlider = QSlider(self.formLayoutWidget)
        self.sqlSlider.setObjectName(u"sqlSlider")
        sizePolicy3.setHeightForWidth(self.sqlSlider.sizePolicy().hasHeightForWidth())
        self.sqlSlider.setSizePolicy(sizePolicy3)
        self.sqlSlider.setMaximumSize(QSize(16777215, 15))
        self.sqlSlider.setMaximum(100)
        self.sqlSlider.setOrientation(Qt.Horizontal)

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.sqlSlider)

        self.label_13 = QLabel(self.formLayoutWidget)
        self.label_13.setObjectName(u"label_13")

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.label_13)

        self.goSlider = QSlider(self.formLayoutWidget)
        self.goSlider.setObjectName(u"goSlider")
        sizePolicy3.setHeightForWidth(self.goSlider.sizePolicy().hasHeightForWidth())
        self.goSlider.setSizePolicy(sizePolicy3)
        self.goSlider.setMaximumSize(QSize(16777215, 15))
        self.goSlider.setMaximum(100)
        self.goSlider.setOrientation(Qt.Horizontal)

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.goSlider)

        self.label_15 = QLabel(self.formLayoutWidget)
        self.label_15.setObjectName(u"label_15")

        self.formLayout.setWidget(11, QFormLayout.LabelRole, self.label_15)

        self.fortranSlider = QSlider(self.formLayoutWidget)
        self.fortranSlider.setObjectName(u"fortranSlider")
        sizePolicy3.setHeightForWidth(self.fortranSlider.sizePolicy().hasHeightForWidth())
        self.fortranSlider.setSizePolicy(sizePolicy3)
        self.fortranSlider.setMaximumSize(QSize(16777215, 15))
        self.fortranSlider.setMaximum(100)
        self.fortranSlider.setOrientation(Qt.Horizontal)

        self.formLayout.setWidget(11, QFormLayout.FieldRole, self.fortranSlider)

        self.label_16 = QLabel(self.formLayoutWidget)
        self.label_16.setObjectName(u"label_16")

        self.formLayout.setWidget(12, QFormLayout.LabelRole, self.label_16)

        self.delphiSlider = QSlider(self.formLayoutWidget)
        self.delphiSlider.setObjectName(u"delphiSlider")
        sizePolicy3.setHeightForWidth(self.delphiSlider.sizePolicy().hasHeightForWidth())
        self.delphiSlider.setSizePolicy(sizePolicy3)
        self.delphiSlider.setMaximumSize(QSize(16777215, 15))
        self.delphiSlider.setMaximum(100)
        self.delphiSlider.setOrientation(Qt.Horizontal)

        self.formLayout.setWidget(12, QFormLayout.FieldRole, self.delphiSlider)

        self.label_17 = QLabel(self.formLayoutWidget)
        self.label_17.setObjectName(u"label_17")

        self.formLayout.setWidget(13, QFormLayout.LabelRole, self.label_17)

        self.matlabSlider = QSlider(self.formLayoutWidget)
        self.matlabSlider.setObjectName(u"matlabSlider")
        sizePolicy3.setHeightForWidth(self.matlabSlider.sizePolicy().hasHeightForWidth())
        self.matlabSlider.setSizePolicy(sizePolicy3)
        self.matlabSlider.setMaximumSize(QSize(16777215, 15))
        self.matlabSlider.setMaximum(100)
        self.matlabSlider.setOrientation(Qt.Horizontal)

        self.formLayout.setWidget(13, QFormLayout.FieldRole, self.matlabSlider)

        self.label_18 = QLabel(self.formLayoutWidget)
        self.label_18.setObjectName(u"label_18")

        self.formLayout.setWidget(14, QFormLayout.LabelRole, self.label_18)

        self.assemblySlider = QSlider(self.formLayoutWidget)
        self.assemblySlider.setObjectName(u"assemblySlider")
        sizePolicy3.setHeightForWidth(self.assemblySlider.sizePolicy().hasHeightForWidth())
        self.assemblySlider.setSizePolicy(sizePolicy3)
        self.assemblySlider.setMaximumSize(QSize(16777215, 15))
        self.assemblySlider.setMaximum(100)
        self.assemblySlider.setOrientation(Qt.Horizontal)

        self.formLayout.setWidget(14, QFormLayout.FieldRole, self.assemblySlider)

        self.label_19 = QLabel(self.formLayoutWidget)
        self.label_19.setObjectName(u"label_19")

        self.formLayout.setWidget(15, QFormLayout.LabelRole, self.label_19)

        self.swiftSlider = QSlider(self.formLayoutWidget)
        self.swiftSlider.setObjectName(u"swiftSlider")
        sizePolicy3.setHeightForWidth(self.swiftSlider.sizePolicy().hasHeightForWidth())
        self.swiftSlider.setSizePolicy(sizePolicy3)
        self.swiftSlider.setMaximumSize(QSize(16777215, 15))
        self.swiftSlider.setMaximum(100)
        self.swiftSlider.setOrientation(Qt.Horizontal)

        self.formLayout.setWidget(15, QFormLayout.FieldRole, self.swiftSlider)

        self.label_20 = QLabel(self.formLayoutWidget)
        self.label_20.setObjectName(u"label_20")

        self.formLayout.setWidget(16, QFormLayout.LabelRole, self.label_20)

        self.kotlinSlider = QSlider(self.formLayoutWidget)
        self.kotlinSlider.setObjectName(u"kotlinSlider")
        sizePolicy3.setHeightForWidth(self.kotlinSlider.sizePolicy().hasHeightForWidth())
        self.kotlinSlider.setSizePolicy(sizePolicy3)
        self.kotlinSlider.setMaximumSize(QSize(16777215, 15))
        self.kotlinSlider.setMaximum(100)
        self.kotlinSlider.setOrientation(Qt.Horizontal)

        self.formLayout.setWidget(16, QFormLayout.FieldRole, self.kotlinSlider)

        self.label_21 = QLabel(self.formLayoutWidget)
        self.label_21.setObjectName(u"label_21")

        self.formLayout.setWidget(17, QFormLayout.LabelRole, self.label_21)

        self.rubySlider = QSlider(self.formLayoutWidget)
        self.rubySlider.setObjectName(u"rubySlider")
        sizePolicy3.setHeightForWidth(self.rubySlider.sizePolicy().hasHeightForWidth())
        self.rubySlider.setSizePolicy(sizePolicy3)
        self.rubySlider.setMaximumSize(QSize(16777215, 15))
        self.rubySlider.setMaximum(100)
        self.rubySlider.setOrientation(Qt.Horizontal)

        self.formLayout.setWidget(17, QFormLayout.FieldRole, self.rubySlider)

        self.label_23 = QLabel(self.formLayoutWidget)
        self.label_23.setObjectName(u"label_23")

        self.formLayout.setWidget(18, QFormLayout.LabelRole, self.label_23)

        self.rustSlider = QSlider(self.formLayoutWidget)
        self.rustSlider.setObjectName(u"rustSlider")
        sizePolicy3.setHeightForWidth(self.rustSlider.sizePolicy().hasHeightForWidth())
        self.rustSlider.setSizePolicy(sizePolicy3)
        self.rustSlider.setMaximumSize(QSize(16777215, 15))
        self.rustSlider.setMaximum(100)
        self.rustSlider.setOrientation(Qt.Horizontal)

        self.formLayout.setWidget(18, QFormLayout.FieldRole, self.rustSlider)

        self.label_24 = QLabel(self.formLayoutWidget)
        self.label_24.setObjectName(u"label_24")

        self.formLayout.setWidget(19, QFormLayout.LabelRole, self.label_24)

        self.cobolSlider = QSlider(self.formLayoutWidget)
        self.cobolSlider.setObjectName(u"cobolSlider")
        sizePolicy3.setHeightForWidth(self.cobolSlider.sizePolicy().hasHeightForWidth())
        self.cobolSlider.setSizePolicy(sizePolicy3)
        self.cobolSlider.setMaximumSize(QSize(16777215, 15))
        self.cobolSlider.setMaximum(100)
        self.cobolSlider.setOrientation(Qt.Horizontal)

        self.formLayout.setWidget(19, QFormLayout.FieldRole, self.cobolSlider)

        self.label_22 = QLabel(self.formLayoutWidget)
        self.label_22.setObjectName(u"label_22")

        self.formLayout.setWidget(20, QFormLayout.LabelRole, self.label_22)

        self.pushButton = QPushButton(self.formLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.formLayout.setWidget(20, QFormLayout.FieldRole, self.pushButton)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"System Wnioskowania Optymalnego J\u0119zyka Programowania ", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Do\u015bwiadczenie programistyczne", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"System Wnioskowania Optymalnego J\u0119zyka Programowania ", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Python", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"C++", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"C#", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Java", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"JavaScript", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"PHP", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Visual Basic", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Scratch", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"SQL", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"GO", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Fortran", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Delphi/Object Pascal", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"MATLAB", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Assembly", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Swift", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Kotlin", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Ruby", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Rust", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"COBOL", None))
        self.label_22.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Oblicz", None))
    # retranslateUi

