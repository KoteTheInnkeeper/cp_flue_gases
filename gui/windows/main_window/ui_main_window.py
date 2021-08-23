from gui.qt_core import *
from gui.widgets.form_widgets import LeftMenuPushButton
from gui.gui_constants import *

class UIMainWindow(object):
    def setup_ui(self, parent: QMainWindow):
        if not parent.objectName():
            parent.setObjectName("MainWindow")

        # Set initial parameters (size and so on)
        parent.resize(800, 600)
        parent.setMinimumSize(640, 480)

        # Create central frame
        self.central_frame = QFrame()
        self.central_frame.setStyleSheet(f"background-color: {Color.CONTENT_BG}")

        # Layouts are used to organize our widgets within frames.
        # Create main layout
        self.main_layout = QHBoxLayout(self.central_frame)
        # Setting margins and spacing.
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        # Left menu
        self.left_menu = QFrame()
        self.left_menu.setStyleSheet(f"background-color: {Color.LEFT_MENU_BG_COLOR}")
        # Setting dimensions
        self.left_menu.setMaximumWidth(50)
        self.left_menu.setMinimumWidth(50)
        
        # Left menu layout
        self.left_menu_layout = QVBoxLayout(self.left_menu)
        self.left_menu_layout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_layout.setSpacing(0)

        # We will use a frame for the top buttons in this left menu.
        self.left_menu_top_frame = QFrame()
        self.left_menu_top_frame.setMinimumHeight(50)
        # In order to differentiate the widgets or items and be able to apply specifics stylesheet to each of them,
        # it is a good practice to 'set objects names' like so
        self.left_menu_top_frame.setObjectName("left_menu_top_frame")
       
        # Top button frame layout.
        self.left_menu_top_layout = QVBoxLayout(self.left_menu_top_frame)
        self.left_menu_top_layout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_top_layout.setSpacing(0)

        # Top left menu buttons
        self.toggle_btn = LeftMenuPushButton(text="Hide menu", icon_path="hamburger_icon.svg")
        self.cp_btn = LeftMenuPushButton(text="Specific heat", is_active=True, icon_path="fume_icon.svg")
        self.fuel_btn = LeftMenuPushButton(text="Fuel", icon_path="fuel_icon.svg")

        # Add buttons to the layout
        self.left_menu_top_layout.addWidget(self.toggle_btn)
        self.left_menu_top_layout.addWidget(self.cp_btn)
        self.left_menu_top_layout.addWidget(self.fuel_btn)

        # Spacer to separate the 'managing' buttons from the 'settings' one.
        self.left_menu_spacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        # Another frame for the bottom buttons.
        self.left_menu_bottom_frame = QFrame()
        self.left_menu_bottom_frame.setMinimumHeight(50)
        self.left_menu_bottom_frame.setObjectName("left_menu_bottom_frame")

        # Bottom button frame layout.
        self.left_menu_bottom_layout = QVBoxLayout(self.left_menu_bottom_frame)
        self.left_menu_bottom_layout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_bottom_layout.setSpacing(0)

        # Bottom left menu button
        self.about_btn = LeftMenuPushButton(text="About", icon_path="about_icon.svg")

        # Adding this button to the layout
        self.left_menu_bottom_layout.addWidget(self.about_btn)

        # Version label
        self.version_label = QLabel("v1.0.0")
        self.version_label.setAlignment(Qt.AlignCenter)
        self.version_label.setMinimumHeight(Dimension.BOT_BAR_HEIGHT)
        self.version_label.setMaximumHeight(Dimension.BOT_BAR_HEIGHT)
        self.version_label.setStyleSheet("color: #c3ccdf")

        # Add to the layout
        self.left_menu_layout.addWidget(self.left_menu_top_frame)
        self.left_menu_layout.addItem(self.left_menu_spacer)
        self.left_menu_layout.addWidget(self.left_menu_bottom_frame)
        self.left_menu_layout.addWidget(self.version_label)

        # Content frame
        self.content = QFrame()
        self.content.setStyleSheet(f"background-color: {Color.CONTENT_BG}")

        # Content layout. The following syntax reads as "create a vertical layout for the self.content frame"
        self.content_layout = QVBoxLayout(self.content)
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        self.content_layout.setSpacing(0)

        # Top bar within content frame
        self.top_bar = QFrame()
        self.top_bar.setMaximumHeight(Dimension.TOP_BAR_HEIGHT)
        self.top_bar.setMinimumHeight(Dimension.TOP_BAR_HEIGHT)
        self.top_bar.setStyleSheet(f"background-color: {Color.TOP_BOT_BAR_BG}; color: {Color.TOP_BOT_BAR_TEXT}")

        # Left label
        self.top_label_left = QLabel("Specific mean heat for flue gases calculator")

        # Top spacer
        self.top_spacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        # Right label
        self.top_label_right = QLabel("| Specific heat")
        self.top_label_right.setStyleSheet("font: 700 9pt 'Segoe UI'")

        # Top bar horizontal layout
        self.top_bar_layout = QHBoxLayout(self.top_bar)
        self.top_bar_layout.setContentsMargins(10, 0, 10, 0)
        
        # Adding widgets to the top bar layout
        self.top_bar_layout.addWidget(self.top_label_left)
                # All the 'QObjects' with classes ended in 'Item' (like the QSpacerItem) must be added with
                # the 'addItem' method.
        self.top_bar_layout.addItem(self.top_spacer)    
        self.top_bar_layout.addWidget(self.top_label_right)

        # Application pages ui_stacked_widget
        self.pages = QStackedWidget()
        self.pages.setStyleSheet("font-size: 12pt; color: #f8f8f2; ")
        """# Altough we created the 'stacked widget' here, we will use 'ui_pages.py' one to get the pages.
        self.ui_pages = Ui_stacked_pages()
        self.ui_pages.setupUi(self.pages)
        self.pages.setCurrentWidget(self.ui_pages.page_1)"""

        # Bottom bar within content frame
        self.bottom_bar = QFrame()
        self.bottom_bar.setMaximumHeight(Dimension.BOT_BAR_HEIGHT)
        self.bottom_bar.setMinimumHeight(Dimension.BOT_BAR_HEIGHT)
        self.bottom_bar.setStyleSheet(f"background-color: {Color.TOP_BOT_BAR_BG}; color: {Color.TOP_BOT_BAR_TEXT}")

        # Bottom bar layout
        self.bottom_bar_layout = QHBoxLayout(self.bottom_bar)
        self.bottom_bar_layout.setContentsMargins(10, 0, 10, 0)

        # Labels for this bottom bar layout.
        self.bottom_label_left = QLabel("Created by KoteTheInnkeeper.")
        self.bottom_label_right = QLabel("© 2021")

        # Spacer yo put between those labels
        self.bottom_spacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        # Adding this two widgets and the spacer item to the bottom bar layout
        self.bottom_bar_layout.addWidget(self.bottom_label_left)
        self.bottom_bar_layout.addItem(self.bottom_spacer)
        self.bottom_bar_layout.addWidget(self.bottom_label_right)

        # Adding to content layout
        self.content_layout.addWidget(self.top_bar)
        self.content_layout.addWidget(self.pages)
        self.content_layout.addWidget(self.bottom_bar)
        
        # Add widgets (both left and content frames) to our main layout.
        self.main_layout.addWidget(self.left_menu)
        self.main_layout.addWidget(self.content)

        # Set the 'central frame' as our central widget.
        parent.setCentralWidget(self.central_frame)
