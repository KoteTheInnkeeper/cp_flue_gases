from gui.gui_constants import *
import os

from gui.qt_core import *


class LeftMenuPushButton(QPushButton):
    def __init__(
        self,
        text: str="", 
        height: int=40, 
        minimum_width: int=50, 
        text_padding: int=55, 
        text_color: str="#c3ccdf", 
        icon_path: str="", 
        icon_color: str="#c3ccdf",
        btn_color="#44475a", 
        btn_hover="#4f5368",
        btn_pressed="#282a36",
        is_active= False
    ):
        super().__init__()

        # Set default parameters
        self.setText(text)
        self.setMaximumHeight(height)
        self.setMinimumHeight(height)
        self.setCursor(Qt.PointingHandCursor)

        # Custom parameters
        self.minimum_width = minimum_width
        self.text_padding = text_padding
        self.icon_path = icon_path
        self.text_color = text_color
        self.icon_color = icon_color
        self.btn_color = btn_color
        self.btn_hover = btn_hover
        self.btn_pressed = btn_pressed
        self.is_active = is_active

        # Set stylesheet according to what we've entered.
        self.set_style()

    def set_style(self):
        stylesheet_str = f"""
        QPushButton {{
            color: {self.text_color};
            background-color: {self.btn_color};
            padding-left: {self.text_padding}px;
            text-align: left;
            border: none;
        }}

        QPushButton:hover {{
            background-color: {self.btn_hover};
        }}
        
        QPushButton:pressed {{
            background-color: {self.btn_pressed};
        }}
        """

        active_str =f"""
        QPushButton {{
            background-color: {self.btn_hover};
            border-right: 5px solid {Color.LEFT_MENU_ACTIVE_BTN_COLOR};
        }}
        """

        if not self.is_active:
            self.setStyleSheet(stylesheet_str)
        else:
            self.setStyleSheet(stylesheet_str + active_str)
    
    def set_active(self, is_active_menu: bool) -> None:
        self.is_active = is_active_menu
        self.set_style()

    def paintEvent(self, event):
        # Without the following line, this method would've overwrite the QPushButton.paintEvent one, meaning we
        # would've lose all our 'formatting' done by using it (in the background, within the methods that are defined 
        # in the definition for QPushButton)
        QPushButton.paintEvent(self, event)

        # Painter -> a 'design workframe'
        qp = QPainter()
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing)
        qp.setPen(Qt.NoPen)

        # Reference rectangle for our icon
        rect = QRect(0, 0, self.minimum_width, self.minimumHeight())

        self.draw_icon(qp, self.icon_path, rect, self.icon_color)

        qp.end()

    def draw_icon(self, qp: QPainter, image: str, rect: QRect, color: str):
        # Format path
        app_path = os.path.abspath(os.getcwd())
        folder = "gui/images/icons"
        path = os.path.join(app_path, folder)
        icon_path = os.path.normpath(os.path.join(path, image))

         # Draw icon
        icon = QPixmap(icon_path)
        painter = QPainter(icon)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(icon.rect(), color)
        qp.drawPixmap(
            (rect.width() - icon.width()) / 2,
            (rect.height() - icon.height()) / 2,
            icon
        )
        painter.end()


class FormCombobox(QComboBox):
    def __init__(
        self,
        bg_color: str = Color.COMBOBOX_BG,
        border_color: str = Color.COMBOBOX_BORDER,
        hover_border: str = Color.COMBOBOX_HOVER_BORDER,
        text_color: str = Color.COMBOBOX_TEXT_COLOR,
        border_dropdown_color: str = Color.COMBOBOX_DROPDOWN_BORDER,
        dropdown_bg_color: str = Color.COMBOBOX_DROPDOWN_BG,
        selection_bg_color: str = Color.COMBOBOX_SELECTION_BG,
        dropdown_arrow_path: str = Paths.COMBOBOX_DROPDOWN_ARROW,
        is_editable: bool = False,
        is_enabled: bool = True
        ) -> None:
        super().__init__()        

        # Saving parameters within object
        self.bg_color = bg_color
        self.border_color = border_color
        self.hover_border = hover_border
        self.text_color = text_color
        self.border_dropdown_color = border_dropdown_color
        self.dropwdown_bg_color = dropdown_bg_color
        self.selection_bg_color = selection_bg_color
        self.dropdown_arrow_path = dropdown_arrow_path

        # Setting stylesheet
        self.set_style()
        # Setting size
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        # Enabling/disabling it
        self.setEnabled(is_enabled)
        # Making it editable/non-editable
        self.setEditable(is_editable)

    def set_style(self) -> None:
        self.setStyleSheet(f"""
        QComboBox{{
            background-color: {self.bg_color};
            border-radius: 5px;
            border: 2px solid {self.border_color};
            padding: 5px;
	        padding-left: 10px;
            color: {self.text_color};
        }}

        QComboBox:hover{{
            border: 2px solid {self.hover_border};
        }}

        QComboBox::drop-down {{
            subcontrol-origin: padding;
            subcontrol-position: top right;
            width: 25px; 
            border-left-width: 3px;
            border-left-color: {self.border_dropdown_color};
            border-left-style: solid;
            border-top-right-radius: 3px;
            border-bottom-right-radius: 3px;	
            background-image: url({self.dropdown_arrow_path});
            background-position: center;
            background-repeat: no-reperat;
        }}
        QComboBox QAbstractItemView {{
            color: {self.text_color};	
            background-color: {self.dropwdown_bg_color};
            padding: 10px;
            selection-background-color: {self.selection_bg_color};
        }}
            """)


class FormLineEdit(QLineEdit):
    def __init__(self):
        super().__init__()

        # Setting stylesheet
        self.set_style()

    
    def set_style(self):
        self.setStyleSheet(f"""
        QLineEdit {{
            background-color: rgb(33, 37, 43);
            border-radius: 5px;
            border: 2px solid rgb(33, 37, 43);
            padding-left: 10px;
            selection-color: rgb(255, 255, 255);
            selection-background-color: rgb(255, 121, 198);
        }}
        QLineEdit:hover {{
            border: 2px solid rgb(64, 71, 88);
        }}
        QLineEdit:focus {{
            border: 2px solid rgb(91, 101, 124);
        }}
        """)


class FormCheckBox(QCheckBox):
    def __init__(
        self,
        text: str = "CHECKBOX_TEXT",
        check_path: str = Paths.CHECKBOX_CHECK,
        text_color: str = Color.CHECKBOX_TEXT_COLOR,
        border: str = Color.CHECKBOX_INDICATOR_BORDER,
        bg: str = Color.CHECKBOX_INDICATOR_BG,
        hover_border: str = Color.CHECKBOX_INDICATOR_HOVER_BORDER,
        checked_border: str = Color.CHECKBOX_INDICATOR_CHECKED_BORDER,
        checked_bg: str = Color.CHECKBOX_INDICATOR_CHECKED_BG
        
    ):
        super().__init__(text=text)

        # Saving parameters within object
        self.check_path = check_path
        self.text_color = text_color
        self.border = border
        self.bg = bg
        self.hover_border = hover_border
        self.checked_border = checked_border
        self.checked_bg = checked_bg

        # Setting stylesheet
        self.set_style()
        # Setting text
        

    def set_style(self):
        self.setStyleSheet(f"""
        QCheckBox{{
            color: {self.text_color};
        }}
        QCheckBox::indicator {{
            border: 3px solid {self.border};
            width: 15px;
            height: 15px;
            border-radius: 10px;
            background: {self.bg};
        }}
        QCheckBox::indicator:hover {{
            border: 3px solid {self.hover_border};
        }}
        QCheckBox::indicator:checked {{
            background: 3px solid {self.checked_bg};
            border: 3px solid {self.checked_border};	
            background-image: url({self.check_path});
        }}
        """
        )


class FormPushButton(QPushButton):
    def __init__(
        self,
        text: str="", 
        height: int=35, 
        minimum_width: int=125, 
        text_padding: int=50, 
        text_color: str=Color.FORM_BTN_TEXT, 
        icon_path: str="", 
        icon_color: str=Color.FORM_BTN_ICON_COLOR,
        btn_color=Color.FORM_BTN_COLOR, 
        btn_hover=Color.FORM_BTN_HOVER,
        btn_pressed=Color.FORM_BTN_PRESSED,
        hover_border=Color.COMBOBOX_HOVER_BORDER,
        pressed_border=Color.LEFT_MENU_BG_COLOR
    ):
        super().__init__()

        # Set default parameters
        self.setText(text)
        self.setMaximumHeight(height)
        self.setMinimumHeight(height)
        self.setMaximumWidth(minimum_width)
        self.setMinimumWidth(minimum_width)
        self.setCursor(Qt.PointingHandCursor)

        # Custom parameters
        self.minimum_width = minimum_width
        self.text_padding = text_padding
        self.icon_path = icon_path
        self.text_color = text_color
        self.icon_color = icon_color
        self.btn_color = btn_color
        self.btn_hover = btn_hover
        self.btn_pressed = btn_pressed
        self.hover_border = hover_border
        self.pressed_border = pressed_border

        # Set stylesheet according to what we've entered.
        self.set_style()

    def set_style(self):
        stylesheet_str = f"""
        QPushButton {{
            color: {self.text_color};
            background-color: {self.btn_color};
            padding-left: {self.text_padding}px;
            text-align: left;
            font: 100 12pt 'Segoe UI';
            border-radius: 5px;
            border: 2px solid {self.pressed_border};
        }}

        QPushButton:hover {{
            background-color: {self.btn_hover};
            border: 2px solid {self.hover_border};
        }}
        
        QPushButton:pressed {{
            background-color: {self.btn_pressed};
            border: 2px solid {self.pressed_border};
        }}
        """
        self.setStyleSheet(stylesheet_str)
    

    def paintEvent(self, event):
        # Without the following line, this method would've overwrite the QPushButton.paintEvent one, meaning we
        # would've lose all our 'formatting' done by using it (in the background, within the methods that are defined 
        # in the definition for QPushButton)
        QPushButton.paintEvent(self, event)

        # Painter -> a 'design workframe'
        qp = QPainter()
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing)
        qp.setPen(Qt.NoPen)

        # Reference rectangle for our icon
        rect = QRect(0, 0, 50, self.minimumHeight())

        self.draw_icon(qp, self.icon_path, rect, self.icon_color)

        qp.end()

    def draw_icon(self, qp: QPainter, image: str, rect: QRect, color: str):
        # Format path
        app_path = os.path.abspath(os.getcwd())
        folder = "gui/images/icons"
        path = os.path.join(app_path, folder)
        icon_path = os.path.normpath(os.path.join(path, image))

         # Draw icon
        icon = QPixmap(icon_path)
        painter = QPainter(icon)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(icon.rect(), color)
        qp.drawPixmap(
            (rect.width() - icon.width()) / 2,
            (rect.height() - icon.height()) / 2,
            icon
        )
        painter.end()


class FormLabel(QLabel):
    def __init__(
        self,
        text: str = "",
        text_color: str = Color.COMBOBOX_TEXT_COLOR,
    ):
        super().__init__(text=text)

        # Saving parameters within object
        self.text_color = text_color

        # Setting stylesheet
        self.set_style()

    def set_style(self):
        self.setStyleSheet(f"""
        QLabel {{
            color: {self.text_color};
        }}
        """)


class FormTableWidget(QTableWidget):
    def __init__(self):
        super().__init__()
        # Setting the style
        self.set_style()

    def set_style(self):
        
        stylesheet_str = f"""
QTableWidget {{	
    color: white;
	background-color: transparent;
	padding: 10px;
	border-radius: 5px;
	gridline-color: rgb(44, 49, 58);
	border-bottom: 1px solid rgb(44, 49, 60);
}}
QTableWidget::item{{
	border-color: grey;
	padding-left: 5px;
	padding-right: 5px;
	gridline-color: grey;
}}
QTableWidget::item:selected{{
	background-color: rgb(189, 147, 249);
}}
QHeaderView::section{{
	background-color: rgb(33, 37, 43);
	max-width: 30px;
	border: 1px solid grey;
	border-style: none;
    border-bottom: 1px solid rgb(44, 49, 60);
    border-right: 1px solid rgb(44, 49, 60);
}}
QTableWidget::horizontalHeader {{	
    font: 100 12pt 'Segoe UI';
	background-color: rgb(33, 37, 43);
}}
QHeaderView::section:horizontal
{{
    color: white;
    font: 75 12pt 'Segoe UI';
    border: 1px solid rgb(33, 37, 43);
	background-color: rgb(33, 37, 43);
	padding: 3px;
	border-top-left-radius: 7px;
    border-top-right-radius: 7px;
}}
QHeaderView::section:vertical
{{
    border: 1px solid rgb(44, 49, 60);
}}

QScrollBar:horizontal {{
    border: none;
    background: rgb(52, 59, 72);
    height: 8px;
    margin: 0px 21px 0 21px;
	border-radius: 0px;
}}
QScrollBar::handle:horizontal {{
    background: rgb(189, 147, 249);
    min-width: 25px;
	border-radius: 4px
}}
QScrollBar::add-line:horizontal {{
    border: none;
    background: rgb(55, 63, 77);
    width: 20px;
	border-top-right-radius: 4px;
    border-bottom-right-radius: 4px;
    subcontrol-position: right;
    subcontrol-origin: margin;
}}

QScrollBar::sub-line:horizontal {{
    border: none;
    background: rgb(55, 63, 77);
    width: 20px;
	border-top-left-radius: 4px;
    border-bottom-left-radius: 4px;
    subcontrol-position: left;
    subcontrol-origin: margin;
}}
QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal
{{
     background: none;
}}
QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal
{{
     background: none;
}}
 QScrollBar:vertical {{
	border: none;
    background: rgb(52, 59, 72);
    width: 8px;
    margin: 21px 0 21px 0;
	border-radius: 0px;
 }}
 QScrollBar::handle:vertical {{	
	background: rgb(189, 147, 249);
    min-height: 25px;
	border-radius: 4px
 }}
 QScrollBar::add-line:vertical {{
     border: none;
    background: rgb(55, 63, 77);
     height: 20px;
	border-bottom-left-radius: 4px;
    border-bottom-right-radius: 4px;
     subcontrol-position: bottom;
     subcontrol-origin: margin;
 }}
 QScrollBar::sub-line:vertical {{
	border: none;
    background: rgb(55, 63, 77);
     height: 20px;
	border-top-left-radius: 4px;
    border-top-right-radius: 4px;
     subcontrol-position: top;
     subcontrol-origin: margin;
 }}
 QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {{
     background: none;
 }}

 QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {{
     background: none;
 }}
"""
        self.setStyleSheet(stylesheet_str)


