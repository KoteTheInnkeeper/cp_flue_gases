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
            border-right: 5px solid #282a36;
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
        folder = "gui/icons"
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