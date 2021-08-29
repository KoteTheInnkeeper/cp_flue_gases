from gui.qt_core import *
from gui.widgets.form_widgets import *
from gui.gui_constants import *

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
        # Setting layout
        self.cp_page_layout = QHBoxLayout(self.cp_page)

        # cp page widgets and items
        self.test_label_1 = QLabel("Specific mean heat")
        self.test_label_1.setAlignment(Qt.AlignCenter)

        # Adding items to cp page layout
        self.cp_page_layout.addWidget(self.test_label_1)
        
        ###########################
        ######## FUEL PAGE ########
        ###########################
        self.fuel_page = QWidget()
        self.fuel_page.setObjectName(u"fuel_page")
        MainStackedWidget.addWidget(self.fuel_page)
        # Setting layout
        self.fuel_page_layout = QVBoxLayout(self.fuel_page)
        ######################################
        ##### FUEL PAGE ITEMS AND WIDGETS ####
        ######################################

        #### FUEL SEARCH FRAME ####
        self.fuel_search_frame = QFrame()
        self.fuel_search_frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.fuel_search_layout = QHBoxLayout(self.fuel_search_frame)       
        # Search label
        self.search_label = FormLabel("Search: ")
        # Combobox to search for 
        self.search_fuel_combobox = FormCombobox(is_editable=True)
        # Spacer to distance the combobox from the 'add' btn
        self.search_spacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Maximum)
        # Add fuel btn
        self.add_fuel_btn = FormPushButton("Add fuel", icon_path="add_icon.svg")

        # Adding these items to this frame's layout
        self.fuel_search_layout.addWidget(self.search_label)
        self.fuel_search_layout.addWidget(self.search_fuel_combobox)
        self.fuel_search_layout.addItem(self.search_spacer)
        self.fuel_search_layout.addWidget(self.add_fuel_btn)

        # Table
        self.show_fuel_table = QTableWidget()
        self.show_fuel_table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.show_fuel_table.setColumnCount(len(TableColumns.SHOW_FUEL_COLUMNS))
        # Setting the horizontal header
        show_fuel_table_header = self.show_fuel_table.horizontalHeader()
        header_font = QFont()
        header_font.setFamily('Segoe UI')
        header_font.setPointSize(12)
        header_font.setBold(True)
        # Hiding the vertical header
        self.show_fuel_table.verticalHeader().setHidden(True)
        self.show_fuel_table.setStyleSheet("color: white; font: 10pt 'Segoe UI';")

        for i, column in enumerate(TableColumns.SHOW_FUEL_COLUMNS):
            item = QTableWidgetItem()
            item.setText(" " + column + " ")
            item.setTextAlignment(Qt.AlignCenter)
            item.setFont(header_font)
            self.show_fuel_table.setHorizontalHeaderItem(i, item)
            if i == 0:
                show_fuel_table_header.setSectionResizeMode(i, QHeaderView.Stretch)
            else:
                show_fuel_table_header.setSectionResizeMode(i, QHeaderView.ResizeToContents)



        # Adding items to fuel page layout
        self.fuel_page_layout.addWidget(self.fuel_search_frame)
        self.fuel_page_layout.addWidget(self.show_fuel_table)

        # About page
        self.about_page = QWidget()
        self.about_page.setObjectName(u"about_page")
        MainStackedWidget.addWidget(self.about_page)
        # Setting layout
        self.about_page_layout = QHBoxLayout(self.about_page)

        # About page widgets and items
        self.test_label_3 = QLabel("About page")
        self.test_label_3.setAlignment(Qt.AlignCenter)

        # Adding items to about page layout
        self.about_page_layout.addWidget(self.test_label_3)

        


        QMetaObject.connectSlotsByName(MainStackedWidget)
    # setupUi



