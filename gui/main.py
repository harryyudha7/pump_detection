import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QListWidgetItem, QWidget, QGridLayout, QFrame, QComboBox, QPushButton, QSpacerItem, QRadioButton
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QPixmap, QFont, QBrush, QColor

# Import the UI class from the 'main_ui' module
from main_ui import Ui_MainWindow
from views.price_db_status_views import price_db_ui
from views.pump_db_views import pump_db_ui
from views.technical_statistics_views import technical_statistics_ui
from views.coin_ranking_views import coin_ranking_ui


# Define a custom MainWindow class
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Initialize the UI from the generated 'main_ui' class
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Set window properties
        self.setWindowIcon(QIcon("./icon/Logo.png"))
        self.setWindowTitle("Coin Ranking Application")

        # Initialize UI elements
        self.title_label = self.ui.title_label
        self.title_label.setText("Harry Corp.")

        self.title_icon = self.ui.title_icon
        self.title_icon.setText("")
        self.title_icon.setPixmap(QPixmap("./icon/Logo.png"))
        self.title_icon.setScaledContents(True)

        self.side_menu = self.ui.listWidget
        self.side_menu.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.side_menu_icon_only = self.ui.listWidget_icon_only
        self.side_menu_icon_only.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.side_menu_icon_only.hide()

        self.menu_btn = self.ui.menu_btn
        self.menu_btn.setText("")
        self.menu_btn.setIcon(QIcon("./icon/close.svg"))
        self.menu_btn.setIconSize(QSize(30, 30))
        self.menu_btn.setCheckable(True)
        self.menu_btn.setChecked(False)

        self.main_content = self.ui.stackedWidget

        # Define a list of menu items with names and icons
        self.menu_list = [
            {
                "name": "Price Database Status",
                "icon": "./icon/dashboard.svg"
            },
            {
                "name": "Pumping Database",
                "icon": "./icon/orders.svg"
            },
            {
                "name": "Technical Statistics",
                "icon": "./icon/decline.svg"
            },
            {
                "name": "Coin Ranking",
                "icon": "./icon/decline.svg"
            }
        ]

        # Initialize the UI elements and slots
        self.init_list_widget()
        self.init_stackwidget()
        self.init_single_slot()
        # self.summary_page.table_summary_btn.clicked.connect(lambda: self.main_content.setCurrentWidget(self.table_summary_page))

    def init_single_slot(self):
        # Connect signals and slots for menu button and side menu
        self.menu_btn.toggled['bool'].connect(self.side_menu.setHidden)
        self.menu_btn.toggled['bool'].connect(self.title_label.setHidden)
        self.menu_btn.toggled['bool'].connect(self.side_menu_icon_only.setVisible)
        self.menu_btn.toggled['bool'].connect(self.title_icon.setHidden)

        # Connect signals and slots for switching between menu items
        self.side_menu.currentRowChanged['int'].connect(self.main_content.setCurrentIndex)
        self.side_menu_icon_only.currentRowChanged['int'].connect(self.main_content.setCurrentIndex)
        self.side_menu.currentRowChanged['int'].connect(self.side_menu_icon_only.setCurrentRow)
        self.side_menu_icon_only.currentRowChanged['int'].connect(self.side_menu.setCurrentRow)
        self.menu_btn.toggled.connect(self.button_icon_change)

    def init_list_widget(self):
        # Initialize the side menu and side menu with icons only
        self.side_menu_icon_only.clear()
        self.side_menu.clear()

        for menu in self.menu_list:
            # Set items for the side menu with icons only
            item = QListWidgetItem()
            item.setIcon(QIcon(menu.get("icon")))
            item.setSizeHint(QSize(40, 40))
            self.side_menu_icon_only.addItem(item)
            self.side_menu_icon_only.setCurrentRow(0)

            # Set items for the side menu with icons and text
            item_new = QListWidgetItem()
            item_new.setIcon(QIcon(menu.get("icon")))
            item_new.setText(menu.get("name"))
            # item_new.setForeground(QColor.black)
            self.side_menu.addItem(item_new)
            self.side_menu.setCurrentRow(0)

    def init_stackwidget(self):
        # Initialize the stack widget with content pages
        widget_list = self.main_content.findChildren(QWidget)
        for widget in widget_list:
            self.main_content.removeWidget(widget)

        # price db page
        self.price_db_page = price_db_ui()
        self.price_db_page.setup_ui()
        self.main_content.addWidget(self.price_db_page)

        db_status = self.price_db_page.df_table

        # print(db_status)

        # pump page
        self.pump_db_page = pump_db_ui()
        self.pump_db_page.setup_ui()
        self.main_content.addWidget(self.pump_db_page)
        
        #technical statistics page
        self.technical_statistics_page = technical_statistics_ui()
        self.technical_statistics_page.setup_ui(db_status=db_status)
        self.main_content.addWidget(self.technical_statistics_page)
        
        #coin ranking page
        self.coin_ranking_page = coin_ranking_ui()
        self.coin_ranking_page.setup_ui(self.technical_statistics_page.df_technical)
        self.main_content.addWidget(self.coin_ranking_page)

    def button_icon_change(self, status):
        # Change the menu button icon based on its status
        if status:
            self.menu_btn.setIcon(QIcon("./icon/open.svg"))
        else:
            self.menu_btn.setIcon(QIcon("./icon/close.svg"))

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Load style file
    with open("style.qss") as f:
        style_str = f.read()

    app.setStyleSheet(style_str)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
