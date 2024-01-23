# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QFormLayout, QFrame,
    QHBoxLayout, QLabel, QLayout, QMainWindow,
    QPushButton, QRadioButton, QSizePolicy, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(810, 600)
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
        self.formLayoutWidget = QWidget(self.centralwidget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 50, 686, 432))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.formLayout.setFieldGrowthPolicy(QFormLayout.FieldsStayAtSizeHint)
        self.formLayout.setRowWrapPolicy(QFormLayout.WrapAllRows)
        self.formLayout.setLabelAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.formLayout.setFormAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setBold(True)
        self.label.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(43)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(20, -1, -1, -1)
        self.modernButton_0 = QRadioButton(self.formLayoutWidget)
        self.buttonGroup = QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.modernButton_0)
        self.modernButton_0.setObjectName(u"modernButton_0")

        self.horizontalLayout.addWidget(self.modernButton_0)

        self.modernButton_1 = QRadioButton(self.formLayoutWidget)
        self.buttonGroup.addButton(self.modernButton_1)
        self.modernButton_1.setObjectName(u"modernButton_1")

        self.horizontalLayout.addWidget(self.modernButton_1)

        self.modernButton_2 = QRadioButton(self.formLayoutWidget)
        self.buttonGroup.addButton(self.modernButton_2)
        self.modernButton_2.setObjectName(u"modernButton_2")
        self.modernButton_2.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.modernButton_2)

        self.modernButton_3 = QRadioButton(self.formLayoutWidget)
        self.buttonGroup.addButton(self.modernButton_3)
        self.modernButton_3.setObjectName(u"modernButton_3")
        self.modernButton_3.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.modernButton_3)


        self.formLayout.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout)

        self.label_4 = QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(43)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(20, -1, -1, -1)
        self.perfButton_0 = QRadioButton(self.formLayoutWidget)
        self.buttonGroup_2 = QButtonGroup(MainWindow)
        self.buttonGroup_2.setObjectName(u"buttonGroup_2")
        self.buttonGroup_2.addButton(self.perfButton_0)
        self.perfButton_0.setObjectName(u"perfButton_0")

        self.horizontalLayout_5.addWidget(self.perfButton_0)

        self.perfButton_1 = QRadioButton(self.formLayoutWidget)
        self.buttonGroup_2.addButton(self.perfButton_1)
        self.perfButton_1.setObjectName(u"perfButton_1")

        self.horizontalLayout_5.addWidget(self.perfButton_1)

        self.perfButton_2 = QRadioButton(self.formLayoutWidget)
        self.buttonGroup_2.addButton(self.perfButton_2)
        self.perfButton_2.setObjectName(u"perfButton_2")

        self.horizontalLayout_5.addWidget(self.perfButton_2)

        self.perfButton_3 = QRadioButton(self.formLayoutWidget)
        self.buttonGroup_2.addButton(self.perfButton_3)
        self.perfButton_3.setObjectName(u"perfButton_3")

        self.horizontalLayout_5.addWidget(self.perfButton_3)


        self.formLayout.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout_5)

        self.label_7 = QLabel(self.formLayoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(34)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(20, -1, -1, -1)
        self.compexityButton_0 = QRadioButton(self.formLayoutWidget)
        self.buttonGroup_3 = QButtonGroup(MainWindow)
        self.buttonGroup_3.setObjectName(u"buttonGroup_3")
        self.buttonGroup_3.addButton(self.compexityButton_0)
        self.compexityButton_0.setObjectName(u"compexityButton_0")

        self.horizontalLayout_6.addWidget(self.compexityButton_0)

        self.compexityButton_1 = QRadioButton(self.formLayoutWidget)
        self.buttonGroup_3.addButton(self.compexityButton_1)
        self.compexityButton_1.setObjectName(u"compexityButton_1")

        self.horizontalLayout_6.addWidget(self.compexityButton_1)

        self.compexityButton_2 = QRadioButton(self.formLayoutWidget)
        self.buttonGroup_3.addButton(self.compexityButton_2)
        self.compexityButton_2.setObjectName(u"compexityButton_2")

        self.horizontalLayout_6.addWidget(self.compexityButton_2)

        self.compexityButton_3 = QRadioButton(self.formLayoutWidget)
        self.buttonGroup_3.addButton(self.compexityButton_3)
        self.compexityButton_3.setObjectName(u"compexityButton_3")

        self.horizontalLayout_6.addWidget(self.compexityButton_3)

        self.compexityButton_4 = QRadioButton(self.formLayoutWidget)
        self.buttonGroup_3.addButton(self.compexityButton_4)
        self.compexityButton_4.setObjectName(u"compexityButton_4")

        self.horizontalLayout_6.addWidget(self.compexityButton_4)


        self.formLayout.setLayout(2, QFormLayout.FieldRole, self.horizontalLayout_6)

        self.label_11 = QLabel(self.formLayoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_11)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(42)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(20, -1, -1, -1)
        self.scalabilityButton_0 = QRadioButton(self.formLayoutWidget)
        self.buttonGroup_4 = QButtonGroup(MainWindow)
        self.buttonGroup_4.setObjectName(u"buttonGroup_4")
        self.buttonGroup_4.addButton(self.scalabilityButton_0)
        self.scalabilityButton_0.setObjectName(u"scalabilityButton_0")

        self.horizontalLayout_10.addWidget(self.scalabilityButton_0)

        self.scalabilityButton_1 = QRadioButton(self.formLayoutWidget)
        self.buttonGroup_4.addButton(self.scalabilityButton_1)
        self.scalabilityButton_1.setObjectName(u"scalabilityButton_1")

        self.horizontalLayout_10.addWidget(self.scalabilityButton_1)

        self.scalabilityButton_2 = QRadioButton(self.formLayoutWidget)
        self.buttonGroup_4.addButton(self.scalabilityButton_2)
        self.scalabilityButton_2.setObjectName(u"scalabilityButton_2")

        self.horizontalLayout_10.addWidget(self.scalabilityButton_2)

        self.scalabilityButton_3 = QRadioButton(self.formLayoutWidget)
        self.buttonGroup_4.addButton(self.scalabilityButton_3)
        self.scalabilityButton_3.setObjectName(u"scalabilityButton_3")

        self.horizontalLayout_10.addWidget(self.scalabilityButton_3)


        self.formLayout.setLayout(3, QFormLayout.FieldRole, self.horizontalLayout_10)

        self.label_3 = QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(40)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(20, -1, -1, -1)
        self.popularityButton_0 = QRadioButton(self.formLayoutWidget)
        self.popularityButton_0.setObjectName(u"popularityButton_0")

        self.horizontalLayout_4.addWidget(self.popularityButton_0)

        self.popularityButton_1 = QRadioButton(self.formLayoutWidget)
        self.popularityButton_1.setObjectName(u"popularityButton_1")

        self.horizontalLayout_4.addWidget(self.popularityButton_1)

        self.popularityButton_2 = QRadioButton(self.formLayoutWidget)
        self.popularityButton_2.setObjectName(u"popularityButton_2")

        self.horizontalLayout_4.addWidget(self.popularityButton_2)


        self.formLayout.setLayout(5, QFormLayout.FieldRole, self.horizontalLayout_4)

        self.label_8 = QLabel(self.formLayoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(40)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(20, -1, -1, -1)
        self.expButton_0 = QRadioButton(self.formLayoutWidget)
        self.buttonGroup_6 = QButtonGroup(MainWindow)
        self.buttonGroup_6.setObjectName(u"buttonGroup_6")
        self.buttonGroup_6.addButton(self.expButton_0)
        self.expButton_0.setObjectName(u"expButton_0")

        self.horizontalLayout_9.addWidget(self.expButton_0)

        self.expButton_1 = QRadioButton(self.formLayoutWidget)
        self.buttonGroup_6.addButton(self.expButton_1)
        self.expButton_1.setObjectName(u"expButton_1")

        self.horizontalLayout_9.addWidget(self.expButton_1)


        self.formLayout.setLayout(6, QFormLayout.FieldRole, self.horizontalLayout_9)

        self.label_6 = QLabel(self.formLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.label_6)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(20, -1, -1, -1)
        self.typeButton_1 = QRadioButton(self.formLayoutWidget)
        self.buttonGroup_7 = QButtonGroup(MainWindow)
        self.buttonGroup_7.setObjectName(u"buttonGroup_7")
        self.buttonGroup_7.addButton(self.typeButton_1)
        self.typeButton_1.setObjectName(u"typeButton_1")

        self.horizontalLayout_8.addWidget(self.typeButton_1)

        self.typeButton_2 = QRadioButton(self.formLayoutWidget)
        self.buttonGroup_7.addButton(self.typeButton_2)
        self.typeButton_2.setObjectName(u"typeButton_2")

        self.horizontalLayout_8.addWidget(self.typeButton_2)

        self.typeButton_0 = QRadioButton(self.formLayoutWidget)
        self.buttonGroup_7.addButton(self.typeButton_0)
        self.typeButton_0.setObjectName(u"typeButton_0")

        self.horizontalLayout_8.addWidget(self.typeButton_0)

        self.typeButton_3 = QRadioButton(self.formLayoutWidget)
        self.buttonGroup_7.addButton(self.typeButton_3)
        self.typeButton_3.setObjectName(u"typeButton_3")

        self.horizontalLayout_8.addWidget(self.typeButton_3)


        self.formLayout.setLayout(8, QFormLayout.FieldRole, self.horizontalLayout_8)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(-20, 0, 821, 31))
        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(0, 0, 831, 31))
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy1)
        self.label_9.setMouseTracking(False)
        self.label_9.setLayoutDirection(Qt.LeftToRight)
        self.label_9.setAutoFillBackground(True)
        self.label_9.setLocale(QLocale(QLocale.Polish, QLocale.Poland))
        self.label_9.setFrameShape(QFrame.Box)
        self.label_9.setFrameShadow(QFrame.Plain)
        self.label_9.setTextFormat(Qt.AutoText)
        self.label_9.setScaledContents(False)
        self.label_9.setAlignment(Qt.AlignCenter)
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(-10, 30, 821, 20))
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy2)
        self.label_10.setMouseTracking(False)
        self.label_10.setLayoutDirection(Qt.LeftToRight)
        self.label_10.setAutoFillBackground(True)
        self.label_10.setLocale(QLocale(QLocale.Polish, QLocale.Poland))
        self.label_10.setFrameShape(QFrame.Box)
        self.label_10.setFrameShadow(QFrame.Plain)
        self.label_10.setTextFormat(Qt.AutoText)
        self.label_10.setScaledContents(False)
        self.label_10.setAlignment(Qt.AlignCenter)
        self.acceptButton = QPushButton(self.centralwidget)
        self.acceptButton.setObjectName(u"acceptButton")
        self.acceptButton.setGeometry(QRect(530, 480, 121, 31))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"System Wnioskowania Optymalnego J\u0119zyka Programowania ", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Czy zale\u017cy Ci na u\u017cywaniu najnowocze\u015bniejszych rozwi\u0105za\u0144?", None))
        self.modernButton_0.setText(QCoreApplication.translate("MainWindow", u"Nie", None))
        self.modernButton_1.setText(QCoreApplication.translate("MainWindow", u"Raczej nie", None))
        self.modernButton_2.setText(QCoreApplication.translate("MainWindow", u"Raczej tak", None))
        self.modernButton_3.setText(QCoreApplication.translate("MainWindow", u"Tak, to dla mnie wa\u017cne", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Czy istotna jest dla Ciebie wydajno\u015b\u0107 i optymalizacja projektu?", None))
        self.perfButton_0.setText(QCoreApplication.translate("MainWindow", u"Nie", None))
        self.perfButton_1.setText(QCoreApplication.translate("MainWindow", u"Raczej nie", None))
        self.perfButton_2.setText(QCoreApplication.translate("MainWindow", u"Raczej tak", None))
        self.perfButton_3.setText(QCoreApplication.translate("MainWindow", u"Tak, to dla mnie wa\u017cne", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Wybierz szacowan\u0105 z\u0142o\u017cono\u015b\u0107 projektu:", None))
        self.compexityButton_0.setText(QCoreApplication.translate("MainWindow", u"Ma\u0142y", None))
        self.compexityButton_1.setText(QCoreApplication.translate("MainWindow", u"Raczej ma\u0142y", None))
        self.compexityButton_2.setText(QCoreApplication.translate("MainWindow", u"Raczej du\u017cy", None))
        self.compexityButton_3.setText(QCoreApplication.translate("MainWindow", u"Du\u017cy", None))
        self.compexityButton_4.setText(QCoreApplication.translate("MainWindow", u"Ci\u0119\u017cko okre\u015bli\u0107", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Czy projekt musi by\u0107 skalowalny?", None))
        self.scalabilityButton_0.setText(QCoreApplication.translate("MainWindow", u"Nie", None))
        self.scalabilityButton_1.setText(QCoreApplication.translate("MainWindow", u"Raczej nie", None))
        self.scalabilityButton_2.setText(QCoreApplication.translate("MainWindow", u"Raczej tak", None))
        self.scalabilityButton_3.setText(QCoreApplication.translate("MainWindow", u"Tak, to dla mnie wa\u017cne", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Czy zale\u017cy Ci na popularno\u015bci j\u0119zyka programowania?", None))
        self.popularityButton_0.setText(QCoreApplication.translate("MainWindow", u"Nie", None))
        self.popularityButton_1.setText(QCoreApplication.translate("MainWindow", u"Troch\u0119 tak", None))
        self.popularityButton_2.setText(QCoreApplication.translate("MainWindow", u"Tak, to dla mnie wazne", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Czy posiadasz do\u015bwiadczenie programistyczne?", None))
        self.expButton_0.setText(QCoreApplication.translate("MainWindow", u"Tak", None))
        self.expButton_1.setText(QCoreApplication.translate("MainWindow", u"Nie", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Wybierz preferowany typ j\u0119zyka:", None))
        self.typeButton_1.setText(QCoreApplication.translate("MainWindow", u"Skryptowy", None))
        self.typeButton_2.setText(QCoreApplication.translate("MainWindow", u"Kompilowany", None))
        self.typeButton_0.setText(QCoreApplication.translate("MainWindow", u"Interpretowany", None))
        self.typeButton_3.setText(QCoreApplication.translate("MainWindow", u"Oboj\u0119tnie", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"System Wnioskowania Optymalnego J\u0119zyka Programowania ", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Odpowiedz na poni\u017csze pytania", None))
        self.acceptButton.setText(QCoreApplication.translate("MainWindow", u"Kontynuuj", None))
    # retranslateUi

