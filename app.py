import logging
import sys

# Erasing previous log
with open('log.log', 'w'):
    pass

# Setting the logger
logging.basicConfig(format="%(asctime)s %(levelname)-8s [%(filename)s:%(funcName)s:%(lineno)d] %(message)s", level=logging.DEBUG,
                    filename='log.log')
log = logging.getLogger('cp_flue_gases')

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

        # Showing the main window
        self.show()


# If we're on main, run the app
app = QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec())