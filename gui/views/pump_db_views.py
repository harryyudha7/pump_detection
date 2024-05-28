import sys
from PyQt6.QtWidgets import QVBoxLayout, QTableView, QHeaderView, QProgressBar, QWidget, QGridLayout, QFrame, QComboBox, QPushButton, QSpacerItem, QRadioButton
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QPixmap, QFont
import pandas as pd
import numpy as np
from views.price_db_status_views import PandasModel

class pump_db_ui(QWidget):
    def setup_ui(self):
        layout = QVBoxLayout()
        # layout.addWidget(self.text_place)
        self.setLayout(layout)

        self.df_pump = pd.read_csv('data_pump.csv')

        self.df_pump = self.df_pump.drop(columns=['Unnamed: 0'])

        self.df_pump['increase'] = np.around(self.df_pump['increase'],2)

        model = PandasModel(self.df_pump)
        self.tableView = QTableView()
        self.tableView.setModel(model)
        header = self.tableView.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(4, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(5, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(6, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(7, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(8, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(9, QHeaderView.ResizeMode.ResizeToContents)
        # header.setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)
        layout.addWidget(self.tableView)

        self.update_btn = QPushButton()
        self.update_btn.setText('Update Database')
        layout.addWidget(self.update_btn)

        self.progress = QProgressBar()
        layout.addWidget(self.progress)

        # self.setObjectName("summary_page")
        # self.summary_grid = QGridLayout()
        # self.summary_grid.setContentsMargins(0, 0, 0, 0)
        # self.summary_grid.setSpacing(0)
        # self.summary_grid.setObjectName("summary_grid")
        # self.summary_title = QLabel(parent=self)
        # self.summary_title.setText("Summary")
        # self.summary_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # font = QFont()
        # font.setPointSize(12)
        # self.summary_title.setFont(font)
        # self.summary_title.setObjectName("summary_title")
        # self.summary_grid.addWidget(self.summary_title,0,0,1,1, Qt.AlignmentFlag.AlignCenter)
        
        # self.comboBox = QComboBox(parent=self)
        # self.comboBox.setObjectName("comboBox")
        # self.comboBox.addItem("Separator-1")
        # self.comboBox.addItem("Separator-2")
        # self.comboBox.addItem("Separator-3")
        # self.comboBox.addItem("Steam Vessel")
        # self.summary_grid.addWidget(self.comboBox,1,0,1,1)

        # self.get_data_summary_btn = QPushButton(parent=self)
        # self.get_data_summary_btn.setText('Get Data')
        # self.get_data_summary_btn.setObjectName("get_data_summary_btn")
        # self.summary_grid.addWidget(self.get_data_summary_btn,1,1,1,1)

        # self.table_summary_btn = QPushButton(parent=self)
        # self.table_summary_btn.setText('Table Summary')
        # self.table_summary_btn.setObjectName("table_summary_btn")
        # self.summary_grid.addWidget(self.table_summary_btn,1,2,1,1)

        # self.graphicsView = QLabel(parent=self)
        # self.graphicsView.setObjectName("graphicsView")
        # self.graphicsView.setText('Chart')
        # self.summary_grid.addWidget(self.graphicsView,2,0,3,3,Qt.AlignmentFlag.AlignCenter)
        # self.setLayout(self.summary_grid)