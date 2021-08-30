import logging
import sys

# Erasing previous log
with open('log.log', 'w'):
    pass

# Setting the logger
logging.basicConfig(format="%(asctime)s %(levelname)-8s [%(filename)s:%(funcName)s:%(lineno)d] %(message)s", level=logging.DEBUG,
                    filename='log.log')
log = logging.getLogger('cp_flue_gases')
from gui.widgets.form_widgets import FormCheckBox, FormCombobox
from utils.errors import *
from gui.gui_constants import Dimension


# Other imports
from gui.qt_core import *
from gui.windows.main_window.ui_main_window import UIMainWindow
# Test Area
from data.db_manager import Database
from utils.fuel import Fuel
from utils.combustion import MultipleTCombustion, SingleTCombustion

host_name = 'stored_info'

app_db = Database(host_name)


# Main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Setting title
        self.setWindowTitle("Specific mean heat for flue gases")

        # Setup the main window
        self.ui = UIMainWindow()
        self.ui.setup_ui(self)

        # Signal for hamburger button
        self.ui.toggle_btn.clicked.connect(self.hamburger_btn)
        
        # Signal for other btns
        self.ui.cp_btn.clicked.connect(self.cp_btn)
        self.ui.fuel_btn.clicked.connect(self.fuel_btn)
        self.ui.about_btn.clicked.connect(self.about_btn)

        # Signal for the checkbox
        self.ui.ui_pages.show_all_checkbox.toggled.connect(self.show_all_checkbox_toggled)

        # Signal combobox text has changed
        self.ui.ui_pages.search_fuel_combobox.currentTextChanged.connect(self.combobox_text_changed)

        # Showing the main window
        self.show()

    def hamburger_btn(self):
        """Changes the menu width"""
        log.debug("Playing the animation for the left menu.")
        # Animation needed parameters
        # Get the menu's width
        menu_width = self.ui.left_menu.width()
        
        # Check width
        width = Dimension.LEFT_MENU_MIN_WIDTH
        if menu_width == Dimension.LEFT_MENU_MIN_WIDTH:
            width = Dimension.LEFT_MENU_MAX_WIDTH
    
        # Start animation
        self.animation = QPropertyAnimation(self.ui.left_menu, b"minimumWidth")
        self.animation.setStartValue(menu_width)
        self.animation.setEndValue(width)
        self.animation.setDuration(500)
        self.animation.setEasingCurve(QEasingCurve.InOutCirc)
        self.animation.start()

    def reset_selection(self):
        """Clears all selections"""
        for btn in self.ui.left_menu.findChildren(QPushButton):
            try:
                btn.set_active(False)
            except Exception:
                log.critical("An exception was raised.")
                pass

    def cp_btn(self):
        """Changes the page to the specific mean heat page."""
        try:
            self.reset_selection()
            self.ui.cp_btn.set_active(True)
            self.ui.top_label_right.setText("| Specific heat")
            self.ui.pages.setCurrentWidget(self.ui.ui_pages.cp_page)
        except Exception:
            log.critical("An exception was raised.")
            raise
    
    def about_btn(self):
        """Changes the page to the specific mean heat page."""
        try:
            self.reset_selection()
            self.ui.about_btn.set_active(True)
            self.ui.top_label_right.setText("| About")
            self.ui.pages.setCurrentWidget(self.ui.ui_pages.about_page)
        except Exception:
            log.critical("An exception was raised.")
            raise
    
    def fuel_btn(self):
        """Changes the page to the specific mean heat page."""
        try:
            self.reset_selection()
            self.ui.fuel_btn.set_active(True)
            self.ui.top_label_right.setText("| Fuel")
            self.populate_fuels_table(self.ui.ui_pages.search_fuel_combobox, self.ui.ui_pages.show_all_checkbox)
            self.populate_fuels_combobox(self.ui.ui_pages.search_fuel_combobox)
            self.ui.ui_pages.search_fuel_combobox.setEnabled(False)
        except FuelNotFound:
            QMessageBox.critical(self, "Running out of fuel!", "There isn't any fuel stored in database. You will need to add one of those.")
        except Exception:
            log.critical("An exception was raised.")
            raise
        finally:
            self.ui.pages.setCurrentWidget(self.ui.ui_pages.fuel_page)            

    def combobox_text_changed(self) -> None:
        """The combobox text has changed"""
        try:
            self.populate_fuels_table(self.ui.ui_pages.search_fuel_combobox, False)
        except FuelNotFound:
            log.critical("There's no fuel named like so.")
        except Exception:
            log.critical("An exception was raised.")

    def populate_fuels_table(self, combobox: FormCombobox, checkbox_state: bool) -> None:
        """Populates the fuel's table."""
        try:
            name = "*" if checkbox_state else combobox.currentText().lower()
            found_fuels = app_db.get_fuels(name)
            self.ui.ui_pages.show_fuel_table.clearContents()
            self.ui.ui_pages.show_fuel_table.setRowCount(len(found_fuels))
            for fuel in found_fuels:
                for i, found_fuel in enumerate(found_fuels):
                    for ii, fuel_field in enumerate(found_fuel, 0):
                        if ii == 0:
                            item = QTableWidgetItem(fuel_field.title())
                        else:
                            item = QTableWidgetItem("%.2f" %round(float(fuel_field) * 100, 2) + "%")
                            item.setTextAlignment(Qt.AlignCenter)
                        item.setFlags(Qt.ItemIsEnabled)
                        self.ui.ui_pages.show_fuel_table.setItem(i, ii, item)
        except NoFuelsFound:
            log.critical("There were no fuels to add to the table.")
            raise
    
    def populate_fuels_combobox(self, combobox: FormCombobox) -> None:
        """Populates the combobox with the fuel's names.
        :param combobox: QComboBox object to be populated."""
        try:
            log.debug("Populating a combobox. Getting the fuel's names.")
            fuels_names = app_db.get_fuels_names()
            combobox.addItems(fuels_names)
        except NoFuelsFound:
            log.critical("No fuels were found.")
        except Exception:
            log.critical("An exception was raised.")
            raise
        else:
            log.debug("Combobox successfully updated.")
        finally:
            log.debug("Enabling or disabling the combobox, according to what's in storage.")
            combobox.setEnabled(bool(combobox.count()))
    
    def show_all_checkbox_toggled(self, state: bool) -> None:
        """Changes the combobox state and population of the table settings."""
        try:
            log.debug("The 'Show all' checkbox was toggled.")
            self.ui.ui_pages.search_fuel_combobox.setEnabled(not state)
            self.populate_fuels_table(self.ui.ui_pages.search_fuel_combobox, state)
        except Exception:
            log.critical("An exception was raised.")
            raise

        
            



# If we're on main, run the app
app = QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec())