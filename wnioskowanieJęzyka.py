# The above class is a PyQt5 application window that allows users to input information about their
# project and receive language recommendations based on their inputs.
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QListWidget, QListWidgetItem
from PyQt5.QtWidgets import QStackedWidget, QWidget, QVBoxLayout, QRadioButton, QSlider
from PyQt5.uic import loadUi
from inferenceApp import LanguageInferenceSystem
from tools.Enums import EnumUI, EnumLenType, EnumPrType, EnumSize

"""
AppWindow class.

This class represents the main application window for the language inference system.

Methods:
    retry(): Resets the system and returns to the main UI.
    init_results(): Initializes the results UI and displays the top 5 recommended languages.
    evaluateExp(expUi): Evaluates the experience input and proceeds to the next UI.
    evaluateForm(formUi): Evaluates the form input and proceeds to the next UI.
    assignProjectType(prType): Assigns the project type and switches to the form input UI.

"""
class AppWindow(QMainWindow):
    def __init__(self):
        super(AppWindow, self).__init__()
        self.system = LanguageInferenceSystem()
        self.setFixedSize(810, 600)

        # Create a stacked widget to hold the different UIs
        self.stacked_widget = QStackedWidget(self)

        # Load UIs from the files
        mainUi = loadUi('UIfiles/main.ui')
        typeUi = loadUi('UIfiles/projectType.ui')
        formUi = loadUi('UIfiles/form.ui')
        experienceUI = loadUi('UIfiles/exp.ui')
        self.resultsUI = loadUi('UIfiles/results.ui')

        # Add UIs to the stacked widget
        self.stacked_widget.addWidget(mainUi)   # EnumUI.MAIN = 0
        self.stacked_widget.addWidget(typeUi)   # EnumUI.PR_TYPE = 1
        self.stacked_widget.addWidget(formUi)   # EnumUI.FORM = ...
        self.stacked_widget.addWidget(experienceUI)
        self.stacked_widget.addWidget(self.resultsUI)

        startButton = mainUi.findChild(QPushButton, 'start')

        # Connect buttons to switch UIs
        startButton.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(EnumUI.PR_TYPE))

        embededButton = typeUi.findChild(QPushButton, 'embededButton')
        scriptButton = typeUi.findChild(QPushButton, 'scriptButton')
        gameButton = typeUi.findChild(QPushButton, 'gameButton')
        webButton = typeUi.findChild(QPushButton, 'webButton')
        mobileButton = typeUi.findChild(QPushButton, 'mobileButton')
        dataScienceButton = typeUi.findChild(QPushButton, 'dataScienceButton')
        desktopButton = typeUi.findChild(QPushButton, 'desktopButton')
        databaseButton = typeUi.findChild(QPushButton, 'databaseButton')
        otherButton = typeUi.findChild(QPushButton, 'otherButton')

        embededButton.clicked.connect(lambda: self.assignProjectType(EnumPrType.EMBEDDED))
        scriptButton.clicked.connect(lambda: self.assignProjectType(EnumPrType.SCRIPT))
        gameButton.clicked.connect(lambda: self.assignProjectType(EnumPrType.GAME))
        webButton.clicked.connect(lambda: self.assignProjectType(EnumPrType.WEB))
        mobileButton.clicked.connect(lambda: self.assignProjectType(EnumPrType.MOBILE))
        dataScienceButton.clicked.connect(lambda: self.assignProjectType(EnumPrType.DATA_SCIENCE))
        desktopButton.clicked.connect(lambda: self.assignProjectType(EnumPrType.DESKTOP))
        databaseButton.clicked.connect(lambda: self.assignProjectType(EnumPrType.DATABASE))
        otherButton.clicked.connect(lambda: self.assignProjectType(EnumPrType.OTHER))

        acceptButton = formUi.findChild(QPushButton, 'acceptButton')
        acceptButton.clicked.connect(lambda: self.evaluateForm(formUi))

        readyButton = experienceUI.findChild(QPushButton, 'pushButton')
        readyButton.clicked.connect(lambda: self.evaluateExp(experienceUI))

        backButton = self.resultsUI.findChild(QPushButton, 'pushButton')
        backButton.clicked.connect(lambda: self.retry())

        # Create a layout and add buttons and stacked widget
        layout = QVBoxLayout(self)
        layout.addWidget(self.stacked_widget)

        # Set the layout for the main window
        central_widget = QWidget(self)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    """
    retry method.

    Resets the system and returns to the main UI.
    """
    def retry(self):
        self.system = LanguageInferenceSystem()
        self.stacked_widget.setCurrentIndex(EnumUI.MAIN)

    """
    init_results method.

    Initializes the results UI and displays the top 5 recommended languages.
    """
    def init_results(self):
        listWidget = self.resultsUI.findChild(QListWidget, 'listWidget')
        listWidget.clear()
        for language in self.system.run():
            listWidget.addItem(QListWidgetItem(language))
        self.stacked_widget.setCurrentIndex(EnumUI.RESULTS)

    """
    evaluateExp method.

    Evaluates the experience input and proceeds to the next UI.

    Args:
        self: The AppWindow object.
        expUi: The experience input UI.
    """
    def evaluateExp(self, expUi):
        sliders = [expUi.findChild(QSlider, 'pythonSlider'),
            expUi.findChild(QSlider, 'cSlider'),
            expUi.findChild(QSlider, 'cppSlider'),
            expUi.findChild(QSlider, 'csSlider'),
            expUi.findChild(QSlider, 'javaSlider'),
            expUi.findChild(QSlider, 'jsSlider'),
            expUi.findChild(QSlider, 'phpSlider'),
            expUi.findChild(QSlider, 'vbSlider'),
            expUi.findChild(QSlider, 'scratchSlider'),
            expUi.findChild(QSlider, 'sqlSlider'),
            expUi.findChild(QSlider, 'goSlider'),
            expUi.findChild(QSlider, 'fortranSlider'),
            expUi.findChild(QSlider, 'delphiSlider'),
            expUi.findChild(QSlider, 'matlabSlider'),
            expUi.findChild(QSlider, 'assemblySlider'),
            expUi.findChild(QSlider, 'swiftSlider'),
            expUi.findChild(QSlider, 'kotlinSlider'),
            expUi.findChild(QSlider, 'rubySlider'),
            expUi.findChild(QSlider, 'rustSlider'),
            expUi.findChild(QSlider, 'cobolSlider')]

        for slider in sliders:
            if slider.value() != 0:
                self.system.userData["experience"][slider.objectName()[:len(slider.objectName())-6]] = slider.value()/100

        self.init_results()

    """
    evaluateForm method.

    Evaluates the form input and proceeds to the next UI.

    Args:
        self: The AppWindow object.
        formUi: The form input UI.
    """
    def evaluateForm(self, formUi):
        modernButton_0 = formUi.findChild(QRadioButton, 'modernButton_0')
        modernButton_1 = formUi.findChild(QRadioButton, 'modernButton_1')
        modernButton_2 = formUi.findChild(QRadioButton, 'modernButton_2')
        modernButton_3 = formUi.findChild(QRadioButton, 'modernButton_3')
        perfButton_0 = formUi.findChild(QRadioButton, 'perfButton_0')
        perfButton_1 = formUi.findChild(QRadioButton, 'perfButton_1')
        perfButton_2 = formUi.findChild(QRadioButton, 'perfButton_2')
        perfButton_3 = formUi.findChild(QRadioButton, 'perfButton_3')
        compexityButton_0 = formUi.findChild(QRadioButton, 'compexityButton_0')
        compexityButton_1 = formUi.findChild(QRadioButton, 'compexityButton_1')
        compexityButton_2 = formUi.findChild(QRadioButton, 'compexityButton_2')
        compexityButton_3 = formUi.findChild(QRadioButton, 'compexityButton_3')
        compexityButton_4 = formUi.findChild(QRadioButton, 'compexityButton_4')
        scalabilityButton_0 = formUi.findChild(QRadioButton, 'scalabilityButton_0')
        scalabilityButton_1 = formUi.findChild(QRadioButton, 'scalabilityButton_1')
        scalabilityButton_2 = formUi.findChild(QRadioButton, 'scalabilityButton_2')
        scalabilityButton_3 = formUi.findChild(QRadioButton, 'scalabilityButton_3')
        popularityButton_0 = formUi.findChild(QRadioButton, 'popularityButton_0')
        popularityButton_1 = formUi.findChild(QRadioButton, 'popularityButton_1')
        popularityButton_2 = formUi.findChild(QRadioButton, 'popularityButton_2')
        expButton_0 = formUi.findChild(QRadioButton, 'expButton_0')
        expButton_1 = formUi.findChild(QRadioButton, 'expButton_1')
        typeButton_1 = formUi.findChild(QRadioButton, 'typeButton_1')
        typeButton_2 = formUi.findChild(QRadioButton, 'typeButton_2')
        typeButton_0 = formUi.findChild(QRadioButton, 'typeButton_0')
        typeButton_3 = formUi.findChild(QRadioButton, 'typeButton_3')

# modernity (0, 0.3, 0.6, 1)
# performance (0, 0.3, 0.6, 1)
# complexity (TINY, TINY 0.5, BIG 0.5, BIG, 0) ???
# scalability (0, 0.3, 0,6, 1)
# popularity (0, 0.5, 1)
# Experienced (0, 1)
# LangType (SCRIPTED, COMPILED, INTERPRETED, 0)

        if modernButton_0.isChecked():
            self.system.userData["modernity"] = 0
        elif modernButton_1.isChecked():
            self.system.userData["modernity"] = 0.3
        elif modernButton_2.isChecked():
            self.system.userData["modernity"] = 0.6
        elif modernButton_3.isChecked():
            self.system.userData["modernity"] = 1
        if perfButton_0.isChecked():
            self.system.userData["performance"] = 0
        elif perfButton_1.isChecked():
            self.system.userData["performance"] = 0.3
        elif perfButton_2.isChecked():
            self.system.userData["performance"] = 0.6
        elif perfButton_3.isChecked():
            self.system.userData["performance"] = 1
        if compexityButton_0.isChecked():
            self.system.userData["complexity"] = EnumSize.TINY
        elif compexityButton_1.isChecked():
            self.system.userData["complexity"] = EnumSize.SMALL
        elif compexityButton_2.isChecked():
            self.system.userData["complexity"] = EnumSize.REGULAR
        elif compexityButton_3.isChecked():
            self.system.userData["complexity"] = EnumSize.BIG
        elif compexityButton_4.isChecked():
            self.system.userData["complexity"] = None
        if scalabilityButton_0.isChecked():
            self.system.userData["scalability"] = 0
        elif scalabilityButton_1.isChecked():
            self.system.userData["scalability"] = 0.3
        elif scalabilityButton_2.isChecked():
            self.system.userData["scalability"] = 0.6
        elif scalabilityButton_3.isChecked():
            self.system.userData["scalability"] = 1
        if popularityButton_0.isChecked():
            self.system.userData["popularity"] = 0
        elif popularityButton_1.isChecked():
            self.system.userData["popularity"] = 0.5
        elif popularityButton_2.isChecked():
            self.system.userData["popularity"] = 1
        if expButton_0.isChecked():
            self.system.userData["experienced"] = True
        elif expButton_1.isChecked():
            self.system.userData["experienced"] = False
        if typeButton_0.isChecked():
            self.system.userData["lenType"] = EnumLenType.SCRIPTED
        elif typeButton_1.isChecked():
            self.system.userData["lenType"] = EnumLenType.COMPILED
        elif typeButton_2.isChecked():
            self.system.userData["lenType"] = EnumLenType.INTERPRETED
        elif typeButton_3.isChecked():
            self.system.userData["lenType"] = None

        print(self.system.userData)

        if self.system.userData["experienced"]:
            self.stacked_widget.setCurrentIndex(EnumUI.EXP)
        else:
            self.init_results()
    """
    assignProjectType method.

    Assigns the project type and switches to the form input UI.

    Args:
        self: The AppWindow object.
        prType (EnumPrType): The project type to assign.
    """
    def assignProjectType(self, prType:EnumPrType):
        self.system.userData["projectType"] = prType
        self.stacked_widget.setCurrentIndex(EnumUI.FORM)

if __name__ == "__main__":
    app = QApplication([])
    main_window = AppWindow()
    main_window.show()
    app.exec_()
