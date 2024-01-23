# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'projectType.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
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
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-10, 230, 811, 31))
        self.label.setMouseTracking(False)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAutoFillBackground(True)
        self.label.setLocale(QLocale(QLocale.Polish, QLocale.Poland))
        self.label.setFrameShape(QFrame.Box)
        self.label.setFrameShadow(QFrame.Plain)
        self.label.setTextFormat(Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignCenter)
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 260, 781, 71))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.embededButton = QPushButton(self.horizontalLayoutWidget)
        self.embededButton.setObjectName(u"embededButton")
        self.embededButton.setMinimumSize(QSize(90, 40))
        self.embededButton.setBaseSize(QSize(90, 40))
        self.embededButton.setAutoRepeatDelay(300)

        self.horizontalLayout.addWidget(self.embededButton)

        self.scriptButton = QPushButton(self.horizontalLayoutWidget)
        self.scriptButton.setObjectName(u"scriptButton")
        self.scriptButton.setMinimumSize(QSize(90, 40))

        self.horizontalLayout.addWidget(self.scriptButton)

        self.gameButton = QPushButton(self.horizontalLayoutWidget)
        self.gameButton.setObjectName(u"gameButton")
        self.gameButton.setMinimumSize(QSize(90, 40))

        self.horizontalLayout.addWidget(self.gameButton)

        self.webButton = QPushButton(self.horizontalLayoutWidget)
        self.webButton.setObjectName(u"webButton")
        self.webButton.setMinimumSize(QSize(90, 40))

        self.horizontalLayout.addWidget(self.webButton)

        self.mobileButton = QPushButton(self.horizontalLayoutWidget)
        self.mobileButton.setObjectName(u"mobileButton")
        self.mobileButton.setMinimumSize(QSize(90, 40))

        self.horizontalLayout.addWidget(self.mobileButton)

        self.dataScienceButton = QPushButton(self.horizontalLayoutWidget)
        self.dataScienceButton.setObjectName(u"dataScienceButton")
        self.dataScienceButton.setMinimumSize(QSize(90, 40))

        self.horizontalLayout.addWidget(self.dataScienceButton)

        self.desktopButton = QPushButton(self.horizontalLayoutWidget)
        self.desktopButton.setObjectName(u"desktopButton")
        self.desktopButton.setMinimumSize(QSize(90, 40))

        self.horizontalLayout.addWidget(self.desktopButton)

        self.databaseButton = QPushButton(self.horizontalLayoutWidget)
        self.databaseButton.setObjectName(u"databaseButton")
        self.databaseButton.setMinimumSize(QSize(90, 40))

        self.horizontalLayout.addWidget(self.databaseButton)

        self.otherButton = QPushButton(self.centralwidget)
        self.otherButton.setObjectName(u"otherButton")
        self.otherButton.setGeometry(QRect(350, 330, 101, 40))
        self.otherButton.setMinimumSize(QSize(90, 40))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"System Wnioskowania Optymalnego J\u0119zyka Programowania ", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Wybierz rodzaj projektu, kt\u00f3ry chcesz zrealizowa\u0107", None))
        self.embededButton.setText(QCoreApplication.translate("MainWindow", u"IoT, Embedded", None))
        self.scriptButton.setText(QCoreApplication.translate("MainWindow", u"Automation\n"
"Scripting", None))
        self.gameButton.setText(QCoreApplication.translate("MainWindow", u"Game", None))
        self.webButton.setText(QCoreApplication.translate("MainWindow", u"WEB", None))
        self.mobileButton.setText(QCoreApplication.translate("MainWindow", u"Mobile App", None))
        self.dataScienceButton.setText(QCoreApplication.translate("MainWindow", u"Data Science\n"
"AI, ML", None))
        self.desktopButton.setText(QCoreApplication.translate("MainWindow", u"Desktop App", None))
        self.databaseButton.setText(QCoreApplication.translate("MainWindow", u"Database", None))
        self.otherButton.setText(QCoreApplication.translate("MainWindow", u"Inne", None))
    # retranslateUi

