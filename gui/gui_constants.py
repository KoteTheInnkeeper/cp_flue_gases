class Dimension:
    BOT_BAR_HEIGHT = 30
    TOP_BAR_HEIGHT = 30

    LEFT_MENU_MIN_WIDTH = 50
    LEFT_MENU_MAX_WIDTH = 160

    COMBOBOX_PADDING = 5
    COMBOBOX_LEFT_PADDING = 10


class Color:
    LEFT_MENU_BG_COLOR = "#44475a"

    TOP_BOT_BAR_BG = "#21232d"
    TOP_BOT_BAR_TEXT = "#6272a4"

    CONTENT_BG = "#282c34"
    LEFT_MENU_ACTIVE_BTN_COLOR = CONTENT_BG

    COMBOBOX_BG = "rgb(27, 29, 35)"
    COMBOBOX_BORDER = "rgb(33, 37, 43)"
    COMBOBOX_HOVER_BORDER = "rgb(64, 71, 88)"
    COMBOBOX_TEXT_COLOR = "white"
    COMBOBOX_DROPDOWN_BORDER = "rgba(39, 44, 54, 150)"
    COMBOBOX_DROPDOWN_BG = "rgb(33, 37, 43)"
    COMBOBOX_SELECTION_BG = "rgb(39, 44, 54)"

    CHECKBOX_TEXT_COLOR = "white"
    CHECKBOX_INDICATOR_BORDER = "rgb(52, 59, 72)"
    CHECKBOX_INDICATOR_BG = "rgb(44, 49, 60)"
    CHECKBOX_INDICATOR_HOVER_BORDER = "rgb(58, 66, 81)"
    CHECKBOX_INDICATOR_CHECKED_BG = "rgb(52, 59, 72)"
    CHECKBOX_INDICATOR_CHECKED_BORDER = "rgb(52, 59, 72)"

    FORM_BTN_TEXT = "#c3ccdf"
    FORM_BTN_ICON_COLOR = "#c3ccdf"
    FORM_BTN_COLOR = "#44475a"
    FORM_BTN_HOVER = "#4f5368"
    FORM_BTN_PRESSED = "#44475a"


class Paths:
    COMBOBOX_DROPDOWN_ARROW = "./gui/images/icons/cil-arrow-bottom.png"
    CHECKBOX_CHECK = "./gui/images/icons/cil-check-alt.png"


class TableColumns:
    SHOW_FUEL_COLUMNS = ("Fuel", "Carbon", "Hydrogen", "Oxygen", "Nitrogen", "Sulfur", "Moisture", "Ashes")