# -*- coding: utf-8 -*-

from gui.qt_core import *

class Ui_MainStackedWidget(object):
    def setupUi(self, MainStackedWidget):
        if not MainStackedWidget.objectName():
            MainStackedWidget.setObjectName(u"MainStackedWidget")
        MainStackedWidget.setWindowTitle("StackedWidget")
        MainStackedWidget.resize(400, 300)

        # cp page
        self.cp_page = QWidget()
        self.cp_page.setObjectName(u"cp_page")
        MainStackedWidget.addWidget(self.cp_page)
        self.cp_page_layout = QHBoxLayout(self.cp_page)

        # cp page widgets and items
        self.test_label_1 = QLabel("Specific mean heat")
        self.test_label_1.setAlignment(Qt.AlignCenter)

        # Adding items to cp page layout
        self.cp_page_layout.addWidget(self.test_label_1)

        # Fuel page
        self.fuel_page = QWidget()
        self.fuel_page.setObjectName(u"fuel_page")
        MainStackedWidget.addWidget(self.fuel_page)
        self.fuel_page_layout = QHBoxLayout(self.fuel_page)

        # Fuel page widgets and items
        self.test_label_2 = QLabel("Fuel")
        self.test_label_2.setAlignment(Qt.AlignCenter)
        
        # Adding items to fuel page layout
        self.fuel_page_layout.addWidget(self.test_label_2)

        # About page
        self.about_page = QWidget()
        self.about_page.setObjectName(u"about_page")
        MainStackedWidget.addWidget(self.about_page)
        self.about_page_layout = QHBoxLayout(self.about_page)

        # About page widgets and items
        self.test_label_3 = QLabel("About page")
        self.test_label_3.setAlignment(Qt.AlignCenter)

        # Adding items to about page layout
        self.about_page_layout.addWidget(self.test_label_3)

        


        QMetaObject.connectSlotsByName(MainStackedWidget)
    # setupUi



